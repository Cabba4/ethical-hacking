## Network topology and connections

AirPortSys, airport bulletin board and control/management system are on externally maintained system.


## HaiTek pcap analysis Time -> From 17:35:28 onwards(lmao)

1) Starts with SSDP protocol requests using ipv6 (so most probably a streaming service or so going out to some in network device mayhaps the bulletin board?)
2) Packet 5 has DHCP stream starting tons of UDP packets on following stream

SSDP protocol requests info -  Their purpose is to discover UPnP devices like home routers or media servers. Ok on large networks but if 18-20 requests from one device per second thats bad!

Acc to SNort Image CVE-2016-0189 Exploit at 2018-07-26 time -> 16:06:46 from 185.17.122.212 to 10.5.8.105

Frame 17
Sender IP - 198.51.100.20 
Target IP - 198.51.100.254 

198.51.100.20 connected to 203.0.113.210 (why)

Frame 23 - OpenVPN so maybe vpn connection initiated(time in frame - 17:36:19)

NanInt VPN logs - Connection established at 16:32:21 to 198.51.100.20 

SO VPN DID CONNECT! Time diff of 1 hour so diff time zones obv

Frame 62-70 vpn shifts group change in vpn ip (17:36:21)

Frame 73 - query for admin-PC

-- goes on for some time 

Frame 228 - NBNS request (done when LLMNR fails also NBNS spoof attack is a thing)

Frame 272 - Local Master announcement admin-PC 'Browse Mail Slot'

Frame 384 - VPN group changed again time - 17:36:32

Frame 485 - garbage in NBNS request

NBNS request is just logged in user making website visits :/

Lot of requests to wpad btw 

Apache log ip - 10.20.31.2



