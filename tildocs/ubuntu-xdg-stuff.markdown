# Ubuntu XDG

Say, you have an executable binary (hopefully in `/opt/bin`), you can make it
appear in in the Applications menu (and have a user-friendlier experience) by
creating a `.desktop` file in `~/.local/share/applications/`.

The template is as follows:

```
[Desktop Entry]
Version=1.0
Type=Application
Name=...
Icon=...
Exec="/opt/bin/exec-path" %f
Comment=...
Categories=Development;IDE;
Terminal=false
StartupWMClass=...
```

**Notes:**

- [These are the registered
  categories.](https://specifications.freedesktop.org/menu-spec/latest/apa.html)
- [`StartupWMClass` is explained
  here.](https://askubuntu.com/questions/367396/what-does-the-startupwmclass-field-of-a-desktop-file-represent)

Afterwards, invoke `xdg-desktop-menu forceupdate`.
