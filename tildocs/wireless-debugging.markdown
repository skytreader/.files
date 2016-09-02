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
