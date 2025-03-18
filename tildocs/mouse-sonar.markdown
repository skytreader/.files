# Locate Mouse Pointer

```
gsettings set org.gnome.desktop.interface locate-pointer true
gsettings set org.gnome.mutter locate-pointer-key Shift_R
```

I'd have really wanted to keep the locate-pointer-key to one of the controls.
The problem is, it seems to override the base functionality of the control key
to the point where I can't copy-paste (or shift workspaces). It doesn't seem to
do so for the Shift key, however. Besides, I'm not sure what the proper value is
to indicate either one of the Control keys. :sad:
