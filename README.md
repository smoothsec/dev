dev
===

SmoothSec development.
Branch - samiux

email - runnersa {at} gmail {dot} com

Blog - samiux.blogspot.com

irc - freenode

channel - #smooth-sec

Files Description :

ips-queue - Config file for suricata-ips-nfqueue.  It works with suricata-ips-nfqueue.
            It is placed at /etc/ and assumed the monitor interfaces is br0.

smoothsec.debian.update - Bash script for updating Debian 7 (Wheezy) only but NOT the SmoothSec components.
                          It can be placed at /root/.

smoothsec.first.setup - SmoothSec installer.  It can be running for more than one time.
                        However, the Snorby database content, Snorby user email and password remained unchange.
                        It is placed at /usr/local/sbin/.  This script is designed for version 3.2+.

suricata-ips-afpacket - Init script of Suricata for IPS running AF_PACKET.  It works with 
                        suricata-ips-afpacket.yaml.  It is placed at /etc/init.d/.
                        However, it should not be execuable when it is not implemented.
                        You can replace the original suricata init script with this script when AF_PACKET
                        is implemented.  Make sure to make it execuable before use.

suricata-ips-afpacket.yaml - YAML config file of Suricata that running IPS (AF_PACKET).
                             It works with suricata-ips-afpacket.  It is placed at /etc/suricata/.
                             Assumed that eth0 and eth1 are used for monitoring interfaces.
                             
suricata-ips-nfqueue - Init script for Suricata that running IPS (NFQUEUE).  It works with ips-queue and
                       /etc/init.d/bridge.  Assumed eth0 and eth1 are bridged as br0.
                       It is placed at /etc/init.d/.  However, it should not be execuable when it is not implemented.
                       You can replace the original suricata init script with this script when
                       it is implemented.  Make sure to make it execuable before use.

