# ffmpeg wonders

[Convert .webp to .jpg](https://unix.stackexchange.com/a/349116)

```
ffmpeg -i file.webp file.jpg
```

---

Compile a bunch of JPEGs to a slideshow movie

```
ffmpeg -framerate 2 -pattern_type glob -i "DSC*.JPG" -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
```

---

[Convert a video file to an animated GIF](https://superuser.com/a/556031/309635)

```
ffmpeg -ss 383 -t 15 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```

`-ss` means the timestamp in the video to start cutting, in seconds.

`-t` is the length of the clip to cut. So this example cuts 15 seconds from the
`383` second timestamp.

`-loop` is a weird parameter. Check the link. But this one sets an infinite
loop.
