# Eurosport is Down

Version tested: 16.04.3

Eurosport.com is having weird problems lately. Isup.me (and other checkers)
report it as down while it can be accessed in Scheherazade. Zangetsu, on the
other hand, keep coming back with "DNS address could not be found" _in Chrome_
(wait for it, this will turn out to be significant later).

I'm unable to completely rule out PLDt on the other hand. So I try to debug.
After making sure that my DNS is set to 8.8.8.8, I try out some DNS queries,

    chad@zangetsu:~$ nslookup eurosport.com
    Server:     127.0.1.1
    Address:    127.0.1.1#53

    Non-authoritative answer:
    *** Can't find eurosport.com: No answer

    chad@zangetsu:~$ 
    chad@zangetsu:~$ nslookup google.com
    Server:     127.0.1.1
    Address:    127.0.1.1#53

    Non-authoritative answer:
    Name:   google.com
    Address: 122.2.153.221
    Name:   google.com
    Address: 122.2.153.231
    Name:   google.com
    Address: 122.2.153.246
    Name:   google.com
    Address: 122.2.153.232
    Name:   google.com
    Address: 122.2.153.216
    Name:   google.com
    Address: 122.2.153.236
    Name:   google.com
    Address: 122.2.153.222
    Name:   google.com
    Address: 122.2.153.217
    Name:   google.com
    Address: 122.2.153.242
    Name:   google.com
    Address: 122.2.153.247
    Name:   google.com
    Address: 122.2.153.241
    Name:   google.com
    Address: 122.2.153.227
    Name:   google.com
    Address: 122.2.153.212
    Name:   google.com
    Address: 122.2.153.226
    Name:   google.com
    Address: 122.2.153.251
    Name:   google.com
    Address: 122.2.153.237

    chad@zangetsu:~$

It would seem that my DNS queries are intercepted locally/cached. To invalidate
the cache, I had to kill `dnsmasq` and let it auto restart.

    chad@zangetsu:~$ pid dnsmasq
    nobody    1957  1193  0 17:42 ?        00:00:00 /usr/sbin/dnsmasq --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/var/run/NetworkManager/dnsmasq.pid --listen-address=127.0.1.1 --cache-size=0 --conf-file=/dev/null --proxy-dnssec --enable-dbus=org.freedesktop.NetworkManager.dnsmasq --conf-dir=/etc/NetworkManager/dnsmasq.d
    chad@zangetsu:~$ sudo kill 1957
    chad@zangetsu:~$ pid dnsmasq
    nobody    6504  1193  0 18:00 ?        00:00:00 /usr/sbin/dnsmasq --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/var/run/NetworkManager/dnsmasq.pid --listen-address=127.0.1.1 --cache-size=0 --conf-file=/dev/null --proxy-dnssec --enable-dbus=org.freedesktop.NetworkManager.dnsmasq --conf-dir=/etc/NetworkManager/dnsmasq.d

After this,

    chad@zangetsu:~$ nslookup eurosport.com
    Server:     8.8.8.8
    Address:    8.8.8.8#53

    Non-authoritative answer:
    *** Can't find eurosport.com: No answer

    chad@zangetsu:~$ 

We are now hitting 8.8.8.8 for DNS queries but even then, still can't find
Eurosport's IP. This looks like it really is Eurosport's problem.

## Resolution (sort of)

Still puzzled as to how Scheherazade (and my Android phone) can actually access
Eurosport (coupled with the fact that this problem has been observed since last
week--kinda unusual for a site to stay down _that_ long), I try loading Eurosport
in Firefox...and it works.

Lastly, I try to set `eurosport.com` to whatever IP I see on Firefox's network
tab but it does not work (browsers complain about malformed URLs or something).
Note that upon checking, the IP seems to be registered with Akamai.

**Bonus, unrelated TIL:** `man hier` explains what the whole Linux directory
structure is about.
