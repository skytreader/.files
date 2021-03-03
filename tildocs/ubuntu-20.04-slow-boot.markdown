# Ubuntu 20.04 is sluggish at start

20.04 seems considerably slower than 16.04 at least when it starts. So I did a
bit of digging and figured that systemctl services on boot take a long time to
start up.

Important disclaimer: I haven't compared it with 16.04. The only other Linux
system I have access to is my work laptop which has 20.04 too _but it is on
SSD_.

With `systemd-analyze blame` I figured out that `docker` is taking a hell lot
of time to start up (at least 7 minutes). So I disabled it on start-up.
Unfortunately, it doesn't have that much of an effect.

After it was disabled I tried to time starting it on my own:

```
chad@scheherazade:~$ time sudo systemctl start docker

real	4m43.506s
user	0m0.026s
sys	0m0.020s
```

Next candidate: `mysql`.

Also note:

```
chad@scheherazade:~$ systemd-analyze time
Startup finished in 4.946s (firmware) + 12.968s (loader) + 5.363s (kernel) + 10min 20.576s (userspace) = 10min 43.854s
graphical.target reached after 5min 22.414s in userspace
```

I wonder if those userspace numbers are normal?

## Two Different Problems

There seems to be two different instances where I observe sluggishness:

- When starting a fresh terminal it takes _ages_ for the prompt to be ready.
This noticeably only happens the first time the terminal is invoked.
- Starting browsers (Firefox and Chrome) seem unresponsive, at least initially.
It seems to take a longer time than 16.04!

The first problem seems to have been alleviated by [lazy loading NodeJS stuff](http://broken-by.me/lazy-load-nvm/)
implemented in a1197c4ca1b.

The second problem is still ongoing and I have no idea yet how to handle it.
Maybe really finally disable mysql (I use docker too much and, as noted above,
starting it really seems to take time. Which is disruptive for my workflow!)
