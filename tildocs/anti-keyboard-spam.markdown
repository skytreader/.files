# Anti Keyboard Spam

Got a rogue keyboard problem in a Linux laptop (so switching keyboards is not an
option): a key (in this case, `F4` key, keycode 62) is repeatedly sending out a
signal. This causes unexpected effects like a window closing when the `ALT` key
is pressed. This is verified by `showkey`.

    chad@zangetsu:kalibrr$ sudo showkey
    kb mode was ?UNKNOWN?
    [ if you are trying this under X, it might not work
    since the X server is also reading /dev/console ]

    press any key (program terminates 10s after last keypress)...
    keycode  62 release
    keycode  28 release
    ^[OSkeycode  62 press
    keycode  62 release
    ^[OSkeycode  62 press
    keycode  62 release
    ^[OSkeycode  62 press
    keycode  62 release
    ^[OSkeycode  62 press
    ^[OS^[OS^[OS^[OS^[OS^[OS^[OS^[OS^[OS^[OS^[OSkeycode  62 press
    keycode  62 press
    keycode  62 press
    keycode  62 press
    keycode  62 press
    keycode  62 press
    keycode  62 press
    keycode  62 press
    # ad infinitum

The solution is to remap the scan code of the physical `F4` key to something
else (the distinction between scan codes and key codes is in the man page for
`setkeycodes`). I ultimately chose the `Num Lock` key.

    sudo setkeycodes 3e 69

[There may be other options though.](http://www.comptechdoc.org/os/linux/howlinuxworks/linux_hlkeycodes.html)

Not yet sure if this will solve `F4` effects on startup.

See also:

- [Linux password changed. Is this an attack or a hardware glitch?](http://security.stackexchange.com/questions/67845/linux-password-changed-is-this-an-attack-or-a-hardware-glitch)
