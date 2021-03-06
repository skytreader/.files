# Krita and libz

When trying to run the Krita appimage in 16.04, I ran into problems about my
libz dependency. An update is not available in the official repositories so I
had to manually compile an update (from 1.2.8 to 1.2.9). Then symlink it...

```
cd /lib/x86_64-linux-gnu/
ln -s -f /usr/local/lib/libz.so.1.2.9/lib libz.so.1
```

(The old 1.2.8 would be in `/lib/x86_64-linux-gnu`.)

So, Krita runs! But now I find the following in my syslog:

```
Dec  5 20:03:57 scheherazade mysqld[7723]: /usr/sbin/mysqld: error while loading shared libraries: libz.so.1: cannot open shared object file: Error 20
```

Just to note this development. I don't really use mysql in this machine anymore
so this is not much of a concern.

This also seems to have caused a conflict for my WiFi drivers. The next time I
booted up after I did this, my WiFi drivers can't establish a connection. The
problem promptly went away when I relinked the 1.2.8 version of libz.

Fortunately, it seems after that initial launch the Krita appimage no longer
needs libz. Or...?

(Ideally, there should be a way to tell the Krita appimage to use a specific
static libz, instead of hoping `/lib/x86_64-linux-gnu/lib.so.1` is pointing to
the exact version that it requires.)
