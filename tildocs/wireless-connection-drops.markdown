# Wireless Connection is Dropping

Version tested: Virtually every Ubuntu I've used so far but this account is
triggered from 16.04.3.

For some reason, after months and months of just working, wireless sometimes
just drops. Of course, after giving `/var/log/syslog` the customary glance, the
first thing to do is to restart network manager:

    sudo service network-manager restart

However, this will also kill the network manager applet at the Ubuntu taskbar.
To get this back, invoke nm-applet:

    daemonize nm-applet

Note that [this](https://askubuntu.com/a/529287/36150) suggests using
`dbus-launch` but, at least for 16.04.3, this does not do anything.

Finally, it seems that when the wireless network is stuck in this kind of loop,
only a restart can save it but I found out that suspend-start could also work.
