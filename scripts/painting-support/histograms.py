# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "pillow==11.3.0"
# ]
# ///

"""
Process a JPG image and write a PNG with transparency:
1) Keep only pixels whose HSV Value (brightness) lies within [low, high] (floats in [0, 1]).
2) Optionally, also keep only pixels that are (fuzzily) Red, Green, or Blue.
   Everything else becomes fully transparent.

Notes:
- The "value" range here uses HSV Value (V), normalized to [0,1].
- The color check uses a fuzzy hue-based metric with saturation gating.
- You can tweak the fuzziness with --sigma, and gating floors with --min-sat/--min-val.
"""

from PIL import Image
import argparse
import colorsys
import math
from typing import Tuple, Literal, Optional

ColorName = Literal["red", "green", "blue"]

def clamp(val, _min, _max):
    return max(_min, min(_max, val))

def hue_membership_hsv(
    rgb: Tuple[int, int, int],
    target: ColorName,
    *,
    threshold: float = 0.5
    sigma_deg: float = 20.0,
    min_s: float = 0.20,
    min_v: float = 0.05,
    sat_power: float = 1.0
) -> bool:
    """
    Fuzzily determine whether a color is red blue or green

    Approach:
      - Convert RGB -> HSV.
      - Compute circular hue distance (in degrees) from canonical hue:
           red=0°, green=120°, blue=240° (with wrap-around for red near 360°).
      - Convert distance to a Gaussian membership: exp(-(d^2)/(2*sigma^2)).
      - Multiply by a saturation gate to suppress grays/whites, and a tiny value gate to avoid near-black.

    Parameters:
      rgb       : pixel value in 0 <= rgb <= 255.
      target    : the color we want to determine.
      threshold : how much of the final score before given rgb value is considered the target color.
      sigma_deg : controls hue tolerance (larger = softer, smaller = stricter).
      min_s     : saturation floor (0..1). Below this, membership smoothly trends toward 0.
      min_v     : value floor (0..1). Below this, membership trends toward 0.
      sat_power : exponent on the saturation gate (>=1 for harder gating).

    Returns:
      float in [0,1]
    """
    r, g, b = rgb
    # Normalize to [0,1] for colorsys
    rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(rf, gf, bf)  # h in [0,1), s,v in [0,1]
    hue_deg = (h * 360.0)

    target_hues = {
        "red": 0.0,
        "green": 120.0,
        "blue": 240.0
    }
    target_hue = target_hues[target]

    # Circular hue distance (degrees), taking care for red spanning 0/360
    diff = abs(hue_deg - target_hue)
    if target == "red":
        # For red, wrap-around is especially important (e.g., 359° is very red)
        diff = min(diff, 360.0 - diff)
    else:
        # This also works for green/blue, but red has the classic 0/360 edge
        diff = min(diff, 360.0 - diff)

    # Gaussian decay by hue distance
    if sigma_deg <= 0:
        hue_score = 1.0 if diff == 0 else 0.0
    else:
        hue_score = math.exp(-0.5 * (diff / sigma_deg) ** 2)

    # Saturation gate: below min_s, suppress; above min_s, scale up to 1
    if s <= min_s:
        sat_gate = 0.0
    else:
        # Smooth ramp normalized to [0,1], optional exponent for sharper falloff
        sat_gate = ((s - min_s) / (1.0 - min_s)) ** sat_power

    # Value gate: crush near-black (keeps colored highlights, ignores dark noise)
    if v <= min_v:
        val_gate = 0.0
    else:
        val_gate = (v - min_v) / (1.0 - min_v)

    # Final membership
    membership = hue_score * sat_gate * val_gate
    # Clamp for safety
    return clamp(membership, 0, 1) >= threshold


def is_color(
    rgb: Tuple[int, int, int],
    target: ColorName,
) -> bool:
    """Convenience boolean check using the fuzzy membership above."""
    return hue_membership_hsv(rgb, target)


def process_image(
    input_path: str,
    low: float,
    high: float,
    color: Optional[ColorName] = None,
) -> None:
    """
    Load a JPG and write a PNG (same size).
    Pixels outside the [low, high] HSV Value range become transparent.
    If 'color' is set, only pixels matching that color (by the fuzzy metric) are kept.
    """
    # Sanity & clamping
    low = max(0.0, min(1.0, low))
    low = clamp(low, 0, 1)
    high = clamp(high, 0, 1)
    if low > high:
        low, high = high, low

    img = Image.open(input_path).convert("RGB")
    w, h = img.size

    out = Image.new("RGBA", (w, h))
    in_px = img.load()
    out_px = out.load()

    for y in range(h):
        for x in range(w):
            r, g, b = in_px[x, y]

            # HSV brightness check for the range filter
            rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
            _, _, v = colorsys.rgb_to_hsv(rf, gf, bf)

            keep = (low <= v <= high)

            # Optional color constraint
            if keep and color is not None:
                keep = is_color((r, g, b), color)

            if keep:
                out_px[x, y] = (r, g, b, 255)
            else:
                out_px[x, y] = (0, 0, 0, 0)

    out.save(input_path, "PNG")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Filter an image by HSV Value range and optional color.")
    p.add_argument("input", help="Input JPG path")
    p.add_argument("--low", type=float, required=True, help="Lower bound for HSV Value (0..1)")
    p.add_argument("--high", type=float, required=True, help="Upper bound for HSV Value (0..1)")
    p.add_argument("--color", choices=["red", "green", "blue"], default=None, help="Optional color constraint")
    args = p.parse_args()
    process_image(
        args.input,
        args.low,
        args.high,
        color=args.color,
        threshold=args.threshold,
        sigma_deg=args.sigma,
        min_s=args.min_sat,
        min_v=args.min_val,
        sat_power=args.sat_power,
    )
