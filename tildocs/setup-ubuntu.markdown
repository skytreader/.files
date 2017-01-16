# Additional Set-up documentation for Ubuntu

Specific version where this was tested: 16.04.1

Looks like the following lines:

    # From http://askubuntu.com/a/447677/36150
    echo "Resizing workspaces"
    dconf write /org/compiz/profiles/unity/plugins/core/hsize 3
    dconf write /org/compiz/profiles/unity/plugins/core/vsize 3

Isn't doing what they are supposed/claimed to do which is to automagically give
me a 3x3 workspace. The following steps were necessary to get those workspaces:

1. Unity Tweak Tool is absolutely not helpful in doing this. None of the settings
there did what they are supposed to do. **TODO:** Remove `unity-tweak-tool` from
the installables of `setup/ubuntu`.
2. The initial workspaces was toggled via All Settings > Appearance > Behavior.
This gives a 2x2 workspace.
3. The correct number of workspaces was configured via CompizConfig Settings
Manager (CCSM). Go to "General Options" then "Desktop Size". Interestingly,
there's no way to install CCSM from the command line. I was expecting
[this](https://www.howtoinstall.co/en/ubuntu/xenial/compizconfig-settings-manager)
to work, but nope!
4. Wrap around behavior is available at CCSM > Desktop Wall > Viewport Switching.
