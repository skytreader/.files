# Wacom on Ubuntu 16.04

Wrestled hard against Ubuntu just to get my new Wacom Intuos Pro to work. First
I was hoping [this](https://medium.com/@microaeris/setting-up-wacom-tablets-with-ubuntu-16-04-d7277e4a595d)
would be enough. But no! This is Linux you have to suffer when integrating
hardware, right?

In the end I just had to manually install the [kernel driver](https://linuxwacom.github.io/)
(having already done the steps in the Medium post). I also switched to GNOME
from Unity, which comes by default with Ubuntu 16.04; apparently there's a known
[bug](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1498664) with Unity
and Wacom compatibility. Given that Unity is an abandoned project, odds are this
won't be fixed anymore.

(Moving to GNOME has its own problems but I've mostly managed to set-up GNOME to
look as pretty/native as Unity did. But there are still some problems that seems
to be [caused by GNOME](https://askubuntu.com/a/951162/36150).)

## Configuration

Although I can now use my Wacom tablet in Ubuntu, it's still not as convenient.
For instance, I can't remap the buttons at the side of the tablet.

Remapping is done through the `xsetwacom` command. I can no longer find what
enlightened me to this arcane syntax but

```
xsetwacom set "Wacom Intuos Pro M Pad pad" "Button" "2" "key +ctrl z -ctrl"
```

is supposed to map button 2 of the tablet to `CTRL + Z`. (The resulting entry
in `xsetwacom -s get "Wacom Intuos Pro M Pad pad" all` will be slightly
different.).

_However_, it does not work! I have no idea why.

---

**Update:** Looks like there's just something wrong with Button 2 mapping. Doing
the same but for Button 3, i.e.,

```
xsetwacom set "Wacom Intuos Pro M Pad pad" "Button" "3" "key +ctrl z -ctrl"
```

gave me the undo button but in the second-from-top button (instead of topmost).
I can live with that.

---

For more debugging, [this](https://askubuntu.com/questions/183354/configuring-wacom-tablet-buttons-and-options/660063#660063)
is a pretty good explanation of how to figure out valid values for `xsetwacom`
commands.

## Disable touch input

You can thank me after your celebrations.

```
xsetwacom --set "Wacom Intuos Pro M Finger touch" Touch off
```
