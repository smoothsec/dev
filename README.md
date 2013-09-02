dev
===

SmoothSec development.

<b>Branch - samiux</b>

email - runnersam {at} gmail {dot} com

Blog - <a href="http://samiux.blogspot.com">Samiux's Blog</a>

irc - freenode

channel - #smooth-sec

<h2><b>Files Description :</b></h2>


<b>ips-queue</b> - Config file for suricata-ips-nfqueue.  It works with suricata-ips-nfqueue.
            It is placed at <code>/etc/</code> and assumed the monitor interfaces is br0.

<b>local.rules</b> - Drop rule for testing.  All traffic related to port 80 will be blocked.

<b>smoothsec.debian.update</b> - Bash script for updating Debian 7 (Wheezy) only but NOT the SmoothSec components.
                          It can be placed at <code>/root/</code>.

<b>smoothsec.first.setup</b> - SmoothSec installer.  It can be running for more than one time.
                        However, the Snorby database content, Snorby user email and password remained unchange.
                        It is placed at <code>/usr/local/sbin/</code>.  This script is designed for version 3.2+.

<b>suricata-ips-afpacket</b> - Init script of Suricata for IPS running AF_PACKET.  It works with 
                        suricata-ips-afpacket.yaml.  It is placed at <code>/etc/init.d/</code>.
                        However, it should not be execuable when it is not implemented.
                        You can replace the original suricata init script with this script when AF_PACKET
                        is implemented.  Make sure to make it execuable before use.

<b>suricata-ips-afpacket.yaml</b> - YAML config file of Suricata that running IPS (AF_PACKET).
                             It works with suricata-ips-afpacket.  It is placed at <code>/etc/suricata/</code>.
                             Assumed that eth0 and eth1 are used for monitoring interfaces.
                             
<b>suricata-ips-nfqueue</b> - Init script for Suricata that running IPS (NFQUEUE).  It works with ips-queue and
                       <code>/etc/init.d/bridge</code>.  Assumed eth0 and eth1 are bridged as br0.
                       It is placed at /etc/init.d/.  However, it should not be execuable when it is not implemented.
                       You can replace the original suricata init script with this script when
                       it is implemented.  Make sure to make it execuable before use.

<b>tips.info</b> - Tips for using and manage SmoothSec
