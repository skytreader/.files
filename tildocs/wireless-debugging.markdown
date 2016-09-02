# Ubuntu Wireless Problems

Aside from checking the logs in `/var/log/syslog`, check your wireless driver
as well.

    chad@zangetsu:~$ sudo lshw -C network
    [sudo] password for chad: 
      *-network               
           description: Wireless interface
           product: Wireless 7260
           vendor: Intel Corporation
           physical id: 0
           bus info: pci@0000:08:00.0
           logical name: wlan0
           version: 83
           serial: e8:b1:fc:86:f6:f5
           width: 64 bits
           clock: 33MHz
           capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless
           configuration: broadcast=yes driver=iwlwifi driverversion=4.4.0-34-generic firmware=16.242414.0 ip=192.168.0.100 latency=0 link=yes multicast=yes wireless=IEEE 802.11abgn
           resources: irq:33 memory:d1600000-d1601fff
      *-network
           description: Ethernet interface
           product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
           vendor: Realtek Semiconductor Co., Ltd.
           physical id: 0
           bus info: pci@0000:09:00.0
           logical name: eth0
           version: 10
           serial: f0:76:1c:22:85:3f
           size: 10Mbit/s
           capacity: 1Gbit/s
           width: 64 bits
           clock: 33MHz
           capabilities: pm msi pciexpress msix vpd bus_master cap_list ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd 1000bt 1000bt-fd autonegotiation
           configuration: autonegotiation=on broadcast=yes driver=r8169 driverversion=2.3LK-NAPI duplex=half firmware=rtl8168g-3_0.0.1 04/23/13 latency=0 link=no multicast=yes port=MII speed=10Mbit/s
           resources: irq:30 ioport:3000(size=256) memory:d1504000-d1504fff memory:d1500000-d1503fff

Needless to mention (but mentioned anyway), how to debug network problems:

- `ping` as a quick (but not rigorous) check on general connectivity.
- `traceroute` to check where the bottleneck is (hitting the router? DNS? ISP routes?).

## Possible triggers

I am not joking with this list

1. Me leaving my chair.
2. Closing the door.

## Sample Logs

**Ubuntu 14.04, weird wireless problem**

Symptom: Ubuntu can't find a particular wireless AP.

    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> enable requested (sleeping: no  enabled: no)
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> waking up and re-enabling...
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): device state change: unmanaged -> unavailable (reason 'managed') [10 20 2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): bringing up device.
    Sep  3 06:21:41 zangetsu kernel: [ 1987.951048] iwlwifi 0000:08:00.0: L1 Enabled - LTR Disabled
    Sep  3 06:21:41 zangetsu kernel: [ 1987.951311] iwlwifi 0000:08:00.0: L1 Enabled - LTR Disabled
    Sep  3 06:21:41 zangetsu kernel: [ 1988.146289] iwlwifi 0000:08:00.0: L1 Enabled - LTR Disabled
    Sep  3 06:21:41 zangetsu kernel: [ 1988.146550] iwlwifi 0000:08:00.0: L1 Enabled - LTR Disabled
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): preparing device.
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): deactivating device (reason 'managed') [2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)
    Sep  3 06:21:41 zangetsu NetworkManager[909]: message repeated 5 times: [ <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> NetworkManager state is now CONNECTED_GLOBAL
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)
    Sep  3 06:21:41 zangetsu NetworkManager[909]: message repeated 2 times: [ <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (eth0): device state change: unmanaged -> unavailable (reason 'managed') [10 20 2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (eth0): bringing up device.
    Sep  3 06:21:41 zangetsu kernel: [ 1988.161062] IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (eth0): preparing device.
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (eth0): deactivating device (reason 'managed') [2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (/hfp/E8B1FC86F6F9_307512D819CE): device state change: unmanaged -> unavailable (reason 'managed') [10 20 2]
    Sep  3 06:21:41 zangetsu kernel: [ 1988.172360] r8169 0000:09:00.0 eth0: link down
    Sep  3 06:21:41 zangetsu kernel: [ 1988.172449] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (/hfp/E8B1FC86F6F9_307512D819CE): deactivating device (reason 'managed') [2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> Unmanaged Device found; state CONNECTED forced. (see http://bugs.launchpad.net/bugs/191889)
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (30:75:12:D8:19:CE): device state change: unmanaged -> unavailable (reason 'managed') [10 20 2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (30:75:12:D8:19:CE): deactivating device (reason 'managed') [2]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> NetworkManager state is now DISCONNECTED
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (/hfp/E8B1FC86F6F9_307512D819CE): device state change: unavailable -> disconnected (reason 'none') [20 30 0]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (30:75:12:D8:19:CE): device state change: unavailable -> disconnected (reason 'none') [20 30 0]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0) supports 5 scan SSIDs
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: starting -> ready
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): device state change: unavailable -> disconnected (reason 'supplicant-available') [20 30 42]
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <warn> Trying to remove a non-existant call id.
    Sep  3 06:20:50 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:21:41 zangetsu wpa_supplicant[1074]: wlan0: Reject scan trigger since one is already pending
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: ready -> disconnected
    Sep  3 06:21:41 zangetsu NetworkManager[909]: <info> (wlan0) supports 5 scan SSIDs
    Sep  3 06:21:41 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:21:44 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: disconnected -> inactive

What is `wlan0: link is not ready`?

This happens when I restart the router:

    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Auto-activating connection 'urrutia'.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) starting connection 'urrutia'
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): device state change: disconnected -> prepare (reason 'none') [30 40 0]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> NetworkManager state is now CONNECTING
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) scheduled...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) started...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) scheduled...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) complete.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) starting...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): device state change: prepare -> config (reason 'none') [40 50 0]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless): access point 'urrutia' has security, but secrets are required.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): device state change: config -> need-auth (reason 'none') [50 60 0]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) complete.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) scheduled...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) started...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): device state change: need-auth -> prepare (reason 'none') [60 40 0]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) scheduled...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) complete.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) starting...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): device state change: prepare -> config (reason 'none') [40 50 0]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless): connection 'urrutia' has security, and secrets exist.  No new secrets needed.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Config: added 'ssid' value 'urrutia'
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Config: added 'scan_ssid' value '1'
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Config: added 'key_mgmt' value 'WPA-PSK'
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Config: added 'psk' value '<omitted>'
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) complete.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Config: set interface ap_scan to 1
    Sep  3 06:24:03 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:24:06 zangetsu wpa_supplicant[1074]: wlan0: SME: Trying to authenticate with ac:f1:df:cc:b0:54 (SSID='urrutia' freq=2412 MHz)
    Sep  3 06:24:06 zangetsu kernel: [ 2133.549396] wlan0: authenticate with ac:f1:df:cc:b0:54
    Sep  3 06:24:06 zangetsu kernel: [ 2133.551752] wlan0: send auth to ac:f1:df:cc:b0:54 (try 1/3)
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: disconnected -> authenticating
    Sep  3 06:24:06 zangetsu wpa_supplicant[1074]: wlan0: Trying to associate with ac:f1:df:cc:b0:54 (SSID='urrutia' freq=2412 MHz)
    Sep  3 06:24:06 zangetsu kernel: [ 2133.689115] wlan0: send auth to ac:f1:df:cc:b0:54 (try 2/3)
    Sep  3 06:24:06 zangetsu kernel: [ 2133.690915] wlan0: authenticated
    Sep  3 06:24:06 zangetsu kernel: [ 2133.692302] wlan0: associate with ac:f1:df:cc:b0:54 (try 1/3)
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: authenticating -> associating
    Sep  3 06:24:06 zangetsu kernel: [ 2133.696340] wlan0: RX AssocResp from ac:f1:df:cc:b0:54 (capab=0x431 status=0 aid=1)
    Sep  3 06:24:06 zangetsu kernel: [ 2133.700313] wlan0: associated
    Sep  3 06:24:06 zangetsu wpa_supplicant[1074]: wlan0: Associated with ac:f1:df:cc:b0:54
    Sep  3 06:24:06 zangetsu kernel: [ 2133.700362] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: associating -> 4-way handshake
    Sep  3 06:24:06 zangetsu wpa_supplicant[1074]: wlan0: WPA: Key negotiation completed with ac:f1:df:cc:b0:54 [PTK=CCMP GTK=TKIP]
    Sep  3 06:24:06 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-CONNECTED - Connection to ac:f1:df:cc:b0:54 completed [id=0 id_str=]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: 4-way handshake -> completed
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless) Stage 2 of 5 (Device Configure) successful.  Connected to wireless network 'urrutia'.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) scheduled.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) started...
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): device state change: config -> ip-config (reason 'none') [50 70 0]
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Beginning DHCPv4 transaction (timeout in 45 seconds)
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> dhclient started with pid 4715
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Beginning IP6 addrconf.
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) complete.
    Sep  3 06:24:06 zangetsu dhclient: Internet Systems Consortium DHCP Client 4.2.4
    Sep  3 06:24:06 zangetsu dhclient: Copyright 2004-2012 Internet Systems Consortium.
    Sep  3 06:24:06 zangetsu dhclient: All rights reserved.
    Sep  3 06:24:06 zangetsu dhclient: For info, please visit https://www.isc.org/software/dhcp/
    Sep  3 06:24:06 zangetsu dhclient: 
    Sep  3 06:24:06 zangetsu NetworkManager[909]: <info> (wlan0): DHCPv4 state changed nbi -> preinit
    Sep  3 06:24:06 zangetsu dhclient: Listening on LPF/wlan0/e8:b1:fc:86:f6:f5
    Sep  3 06:24:06 zangetsu dhclient: Sending on   LPF/wlan0/e8:b1:fc:86:f6:f5
    Sep  3 06:24:06 zangetsu dhclient: Sending on   Socket/fallback
    Sep  3 06:24:06 zangetsu dhclient: DHCPREQUEST of 192.168.0.100 on wlan0 to 255.255.255.255 port 67 (xid=0x77248379)
    Sep  3 06:24:10 zangetsu dhclient: DHCPREQUEST of 192.168.0.100 on wlan0 to 255.255.255.255 port 67 (xid=0x77248379)
    Sep  3 06:24:10 zangetsu dhclient: DHCPACK of 192.168.0.100 from 192.168.0.1
    Sep  3 06:24:10 zangetsu dhclient: bound to 192.168.0.100 -- renewal in 32739 seconds.
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info> (wlan0): DHCPv4 state changed preinit -> reboot
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info>   address 192.168.0.100
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info>   prefix 24 (255.255.255.0)
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info>   gateway 192.168.0.1
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info>   nameserver '192.168.0.1'
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 5 of 5 (IPv4 Configure Commit) scheduled...
    Sep  3 06:24:10 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 5 of 5 (IPv4 Commit) started...
    Sep  3 06:24:11 zangetsu NetworkManager[909]: <info> (wlan0): device state change: ip-config -> secondaries (reason 'none') [70 90 0]
    Sep  3 06:24:11 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 5 of 5 (IPv4 Commit) complete.
    Sep  3 06:24:11 zangetsu NetworkManager[909]: <info> (wlan0): device state change: secondaries -> activated (reason 'none') [90 100 0]
    Sep  3 06:24:11 zangetsu NetworkManager[909]: <info> NetworkManager state is now CONNECTED_GLOBAL
    Sep  3 06:24:11 zangetsu NetworkManager[909]: <info> Policy set 'urrutia' (wlan0) as default for IPv4 routing and DNS.
    Sep  3 06:24:11 zangetsu NetworkManager[909]: <info> Writing DNS information to /sbin/resolvconf
    Sep  3 06:24:11 zangetsu dnsmasq[2525]: setting upstream servers from DBus
    Sep  3 06:24:11 zangetsu dnsmasq[2525]: using nameserver 192.168.0.1#53
    Sep  3 06:24:14 zangetsu whoopsie[1221]: Could not get the list of active connections: Timeout was reached
    Sep  3 06:24:16 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-DISCONNECTED bssid=ac:f1:df:cc:b0:54 reason=4 locally_generated=1
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535410] cfg80211: World regulatory domain updated:
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535415] cfg80211:  DFS Master region: unset
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535418] cfg80211:   (start_freq - end_freq @ bandwidth), (max_antenna_gain, max_eirp), (dfs_cac_time)
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535422] cfg80211:   (2402000 KHz - 2472000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535424] cfg80211:   (2457000 KHz - 2482000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535427] cfg80211:   (2474000 KHz - 2494000 KHz @ 20000 KHz), (300 mBi, 2000 mBm), (N/A)
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535429] cfg80211:   (5170000 KHz - 5250000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)
    Sep  3 06:24:16 zangetsu kernel: [ 2143.535431] cfg80211:   (5735000 KHz - 5835000 KHz @ 40000 KHz), (300 mBi, 2000 mBm), (N/A)
    Sep  3 06:24:16 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:24:20 zangetsu wpa_supplicant[1074]: wlan0: SME: Trying to authenticate with ac:f1:df:cc:b0:54 (SSID='urrutia' freq=2412 MHz)
    Sep  3 06:24:20 zangetsu kernel: [ 2147.028398] wlan0: authenticate with ac:f1:df:cc:b0:54
    Sep  3 06:24:20 zangetsu kernel: [ 2147.030850] wlan0: send auth to ac:f1:df:cc:b0:54 (try 1/3)
    Sep  3 06:24:20 zangetsu kernel: [ 2147.091026] wlan0: send auth to ac:f1:df:cc:b0:54 (try 2/3)
    Sep  3 06:24:20 zangetsu kernel: [ 2147.153264] wlan0: send auth to ac:f1:df:cc:b0:54 (try 3/3)
    Sep  3 06:24:20 zangetsu kernel: [ 2147.219255] wlan0: authentication with ac:f1:df:cc:b0:54 timed out
    Sep  3 06:24:20 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> (wlan0): roamed from BSSID AC:F1:DF:CC:B0:54 (urrutia) to (none) ((none))
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> Activation (wlan0) successful, device activated.
    Sep  3 06:24:21 zangetsu dbus[597]: [system] Activating service name='org.freedesktop.nm_dispatcher' (using servicehelper)
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <warn> Connection disconnected (reason -4)
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: completed -> disconnected
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: disconnected -> scanning
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: scanning -> authenticating
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: authenticating -> disconnected
    Sep  3 06:24:21 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: disconnected -> scanning
    Sep  3 06:24:21 zangetsu dbus[597]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
    Sep  3 06:24:27 zangetsu NetworkManager[909]: <info> (wlan0): IP6 addrconf timed out or failed.
    Sep  3 06:24:27 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 4 of 5 (IPv6 Configure Timeout) scheduled...
    Sep  3 06:24:27 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 4 of 5 (IPv6 Configure Timeout) started...
    Sep  3 06:24:27 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 4 of 5 (IPv6 Configure Timeout) complete.
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <warn> (wlan0): link timed out.
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <info> (wlan0): device state change: activated -> failed (reason 'SSID not found') [100 120 53]
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <info> NetworkManager state is now DISCONNECTED
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <warn> Activation (wlan0) failed for connection 'urrutia'
    Sep  3 06:24:36 zangetsu dbus[597]: [system] Activating service name='org.freedesktop.nm_dispatcher' (using servicehelper)
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <info> (wlan0): device state change: failed -> disconnected (reason 'none') [120 30 0]
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <info> (wlan0): deactivating device (reason 'none') [0]
    Sep  3 06:24:36 zangetsu dbus[597]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <info> (wlan0): canceled DHCP transaction, DHCP client pid 4715
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <warn> DNS: plugin dnsmasq update failed
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <info> Removing DNS information from /sbin/resolvconf
    Sep  3 06:24:36 zangetsu dnsmasq[2525]: setting upstream servers from DBus
    Sep  3 06:24:36 zangetsu NetworkManager[909]: <warn> Couldn't disconnect supplicant interface: This interface is not connected.
    Sep  3 06:24:36 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:24:39 zangetsu wpa_supplicant[1074]: wlan0: Reject scan trigger since one is already pending
    Sep  3 06:24:40 zangetsu wpa_supplicant[1074]: wlan0: Failed to initiate sched scan
    Sep  3 06:24:40 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: scanning -> inactive
    Sep  3 06:24:41 zangetsu ntpdate[4809]: Can't find host ntp.ubuntu.com: Name or service not known (-2)
    Sep  3 06:24:41 zangetsu ntpdate[4809]: no servers can be used, exiting
    Sep  3 06:25:01 zangetsu CRON[4858]: (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ))
    Sep  3 06:25:02 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:25:05 zangetsu wpa_supplicant[1074]: wlan0: Failed to initiate sched scan
    Sep  3 06:25:35 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:25:38 zangetsu wpa_supplicant[1074]: wlan0: Failed to initiate sched scan
    Sep  3 06:26:18 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:26:21 zangetsu wpa_supplicant[1074]: wlan0: Failed to initiate sched scan

Notice how it says `Activation (wlan0) successful, device activated`.

Logs of success:

    Sep  3 06:27:11 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED 
    Sep  3 06:27:14 zangetsu wpa_supplicant[1074]: wlan0: Failed to initiate sched scan
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Auto-activating connection 'urrutia'.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) starting connection 'urrutia'
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): device state change: disconnected -> prepare (reason 'none') [30 40 0]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> NetworkManager state is now CONNECTING
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) scheduled...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) started...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) scheduled...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) complete.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) starting...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): device state change: prepare -> config (reason 'none') [40 50 0]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless): access point 'urrutia' has security, but secrets are required.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): device state change: config -> need-auth (reason 'none') [50 60 0]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) complete.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) scheduled...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) started...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): device state change: need-auth -> prepare (reason 'none') [60 40 0]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) scheduled...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) complete.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) starting...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): device state change: prepare -> config (reason 'none') [40 50 0]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless): connection 'urrutia' has security, and secrets exist.  No new secrets needed.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Config: added 'ssid' value 'urrutia'
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Config: added 'scan_ssid' value '1'
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Config: added 'key_mgmt' value 'WPA-PSK'
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Config: added 'psk' value '<omitted>'
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) complete.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Config: set interface ap_scan to 1
    Sep  3 06:27:14 zangetsu wpa_supplicant[1074]: wlan0: SME: Trying to authenticate with ac:f1:df:cc:b0:54 (SSID='urrutia' freq=2412 MHz)
    Sep  3 06:27:14 zangetsu kernel: [ 2321.536555] wlan0: authenticate with ac:f1:df:cc:b0:54
    Sep  3 06:27:14 zangetsu wpa_supplicant[1074]: wlan0: Trying to associate with ac:f1:df:cc:b0:54 (SSID='urrutia' freq=2412 MHz)
    Sep  3 06:27:14 zangetsu kernel: [ 2321.538691] wlan0: send auth to ac:f1:df:cc:b0:54 (try 1/3)
    Sep  3 06:27:14 zangetsu kernel: [ 2321.540398] wlan0: authenticated
    Sep  3 06:27:14 zangetsu kernel: [ 2321.540607] wlan0: associate with ac:f1:df:cc:b0:54 (try 1/3)
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: inactive -> associating
    Sep  3 06:27:14 zangetsu wpa_supplicant[1074]: wlan0: Associated with ac:f1:df:cc:b0:54
    Sep  3 06:27:14 zangetsu kernel: [ 2321.544789] wlan0: RX AssocResp from ac:f1:df:cc:b0:54 (capab=0x431 status=0 aid=1)
    Sep  3 06:27:14 zangetsu kernel: [ 2321.547076] wlan0: associated
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: associating -> 4-way handshake
    Sep  3 06:27:14 zangetsu wpa_supplicant[1074]: wlan0: WPA: Key negotiation completed with ac:f1:df:cc:b0:54 [PTK=CCMP GTK=TKIP]
    Sep  3 06:27:14 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-CONNECTED - Connection to ac:f1:df:cc:b0:54 completed [id=0 id_str=]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: 4-way handshake -> completed
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless) Stage 2 of 5 (Device Configure) successful.  Connected to wireless network 'urrutia'.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) scheduled.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) started...
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): device state change: config -> ip-config (reason 'none') [50 70 0]
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Beginning DHCPv4 transaction (timeout in 45 seconds)
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> dhclient started with pid 4872
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Beginning IP6 addrconf.
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 3 of 5 (IP Configure Start) complete.
    Sep  3 06:27:14 zangetsu dhclient: Internet Systems Consortium DHCP Client 4.2.4
    Sep  3 06:27:14 zangetsu dhclient: Copyright 2004-2012 Internet Systems Consortium.
    Sep  3 06:27:14 zangetsu dhclient: All rights reserved.
    Sep  3 06:27:14 zangetsu dhclient: For info, please visit https://www.isc.org/software/dhcp/
    Sep  3 06:27:14 zangetsu dhclient: 
    Sep  3 06:27:14 zangetsu NetworkManager[909]: <info> (wlan0): DHCPv4 state changed nbi -> preinit
    Sep  3 06:27:14 zangetsu dhclient: Listening on LPF/wlan0/e8:b1:fc:86:f6:f5
    Sep  3 06:27:14 zangetsu dhclient: Sending on   LPF/wlan0/e8:b1:fc:86:f6:f5
    Sep  3 06:27:14 zangetsu dhclient: Sending on   Socket/fallback
    Sep  3 06:27:14 zangetsu dhclient: DHCPREQUEST of 192.168.0.100 on wlan0 to 255.255.255.255 port 67 (xid=0x49ea0f87)
    Sep  3 06:27:20 zangetsu dhclient: message repeated 2 times: [ DHCPREQUEST of 192.168.0.100 on wlan0 to 255.255.255.255 port 67 (xid=0x49ea0f87)]
    Sep  3 06:27:20 zangetsu dhclient: DHCPNAK from 192.168.0.1 (xid=0x870fea49)
    Sep  3 06:27:20 zangetsu NetworkManager[909]: <info> (wlan0): DHCPv4 state changed preinit -> expire
    Sep  3 06:27:20 zangetsu dhclient: DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 3 (xid=0x754fc15)
    Sep  3 06:27:20 zangetsu NetworkManager[909]: <info> (wlan0): DHCPv4 state changed expire -> preinit
    Sep  3 06:27:22 zangetsu dhclient: DHCPREQUEST of 192.168.0.100 on wlan0 to 255.255.255.255 port 67 (xid=0x15fc5407)
    Sep  3 06:27:22 zangetsu dhclient: DHCPOFFER of 192.168.0.100 from 192.168.0.1
    Sep  3 06:27:22 zangetsu dhclient: DHCPACK of 192.168.0.100 from 192.168.0.1
    Sep  3 06:27:22 zangetsu dhclient: bound to 192.168.0.100 -- renewal in 35392 seconds.
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info> (wlan0): DHCPv4 state changed preinit -> bound
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info>   address 192.168.0.100
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info>   prefix 24 (255.255.255.0)
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info>   gateway 192.168.0.1
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info>   nameserver '192.168.0.1'
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 5 of 5 (IPv4 Configure Commit) scheduled...
    Sep  3 06:27:22 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 5 of 5 (IPv4 Commit) started...
    Sep  3 06:27:23 zangetsu NetworkManager[909]: <info> (wlan0): device state change: ip-config -> secondaries (reason 'none') [70 90 0]
    Sep  3 06:27:23 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 5 of 5 (IPv4 Commit) complete.
    Sep  3 06:27:23 zangetsu NetworkManager[909]: <info> (wlan0): device state change: secondaries -> activated (reason 'none') [90 100 0]
    Sep  3 06:27:23 zangetsu NetworkManager[909]: <info> NetworkManager state is now CONNECTED_GLOBAL
    Sep  3 06:27:23 zangetsu NetworkManager[909]: <info> Policy set 'urrutia' (wlan0) as default for IPv4 routing and DNS.
    Sep  3 06:27:23 zangetsu NetworkManager[909]: <info> Writing DNS information to /sbin/resolvconf
    Sep  3 06:27:23 zangetsu dnsmasq[2525]: setting upstream servers from DBus
    Sep  3 06:27:23 zangetsu dnsmasq[2525]: using nameserver 192.168.0.1#53
    Sep  3 06:27:24 zangetsu NetworkManager[909]: <info> Activation (wlan0) successful, device activated.
    Sep  3 06:27:24 zangetsu dbus[597]: [system] Activating service name='org.freedesktop.nm_dispatcher' (using servicehelper)
    Sep  3 06:27:24 zangetsu dbus[597]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'
    Sep  3 06:27:24 zangetsu whoopsie[1221]: online
    Sep  3 06:27:31 zangetsu ntpdate[4954]: adjust time server 91.189.89.198 offset 0.059324 sec
    Sep  3 06:27:35 zangetsu NetworkManager[909]: <info> (wlan0): IP6 addrconf timed out or failed.
    Sep  3 06:27:35 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 4 of 5 (IPv6 Configure Timeout) scheduled...
    Sep  3 06:27:35 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 4 of 5 (IPv6 Configure Timeout) started...
    Sep  3 06:27:35 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 4 of 5 (IPv6 Configure Timeout) complete.
    Sep  3 06:28:14 zangetsu wpa_supplicant[1074]: wlan0: CTRL-EVENT-SCAN-STARTED

Situation: Ubuntu can detect the AP (it shows up in the WiFi AP list) but it
cannot connect to it for some reason. Logs when attempting to connect are as follows.

    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) starting connection 'urrutia'
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> (wlan0): device state change: disconnected -> prepare (reason 'none') [30 40 0]
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> NetworkManager state is now CONNECTING
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) scheduled...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) started...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) scheduled...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) complete.
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) starting...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> (wlan0): device state change: prepare -> config (reason 'none') [40 50 0]
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless): access point 'urrutia' has security, but secrets are required.
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> (wlan0): device state change: config -> need-auth (reason 'none') [50 60 0]
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) complete.
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) scheduled...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) started...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> (wlan0): device state change: need-auth -> prepare (reason 'none') [60 40 0]
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) scheduled...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 1 of 5 (Device Prepare) complete.
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) starting...
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> (wlan0): device state change: prepare -> config (reason 'none') [40 50 0]
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0/wireless): connection 'urrutia' has security, and secrets exist.  No new secrets needed.
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Config: added 'ssid' value 'urrutia'
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Config: added 'scan_ssid' value '1'
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Config: added 'key_mgmt' value 'WPA-PSK'
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Config: added 'psk' value '<omitted>'
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Activation (wlan0) Stage 2 of 5 (Device Configure) complete.
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> Config: set interface ap_scan to 1
    Sep  3 06:43:20 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: disconnected -> scanning
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <warn> Activation (wlan0/wireless): association took too long, failing activation.
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <info> (wlan0): device state change: config -> failed (reason 'SSID not found') [50 120 53]
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <info> NetworkManager state is now DISCONNECTED
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <info> Marking connection 'urrutia' invalid.
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <warn> Activation (wlan0) failed for connection 'urrutia'
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <info> (wlan0): device state change: failed -> disconnected (reason 'none') [120 30 0]
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <info> (wlan0): deactivating device (reason 'none') [0]
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <info> (wlan0): supplicant interface state: scanning -> disconnected
    Sep  3 06:43:45 zangetsu NetworkManager[909]: <warn> Couldn't disconnect supplicant interface: This interface is not connected.
