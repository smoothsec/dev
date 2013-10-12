<h1>SmoothSec Without Tears</h1>

Editor  : Samiux</br>
Version : 0.1</br>
Dated   : October 12, 2013</br>
 
<h3>Part I - Introduction</h3>

SmoothSec is a lightweight and fully-ready IDS/IPS (Intrusion Detection/Prevention System) Linux distribution based on Debian, available for 32 and 64-bit architecture.  An easy setup process allows to deploy a complete IDS/IPS system within minutes, even for security beginners with minimal Linux experience.

The current version of SmoothSec is 3.6 which is released on October ??, 2013.

Main components :

Debian 7 with Backports kernel
Snorby - a web interface to manage the captured traffic data
Snort - a IDS/IPS Engine
Suricata - a IDS/IPS Engine
Sagan - a HIDS Engine (installed by default)
PulledPork - a Snort/Suricata rules management tool
Pigsty - a traffic spooler

Additional tools :

tcpxtract - a tool for extracting files from network traffic
netdiscover - an active/passive address reconnaissance tool
ngrep - a pcap-aware tool which search data payloads of packets by regular exprssions
nast - a packet sniffer and a LAN analyzer
ipgrab - a verbose packet sniffer
tshark - dump and analyze network traffic
greppcap.py - a tool to find data in a pcap format using regular expression
percona-toolkit - a MySQL collection of advanced command-line tools 
percona-xtrabackup - a MySQL backup tool

(A) Minimum Hardware Requirement

At least an Atom D510 CPU with 2 GB RAM and 20 GB storage.  Two network interfaces for IDS and Three network interfaces for IPS setup.  For IDS setup, a switch with SPAN (or port mirroring) port is required.  If you have a home switch (so-called switch) or virtual switch (running on a virtual machine), you are not required a SPAN port as those are not a REAL switches.

The better hardware is the better performance.

(B) Structure 

If you are going to set up a distributed IDS, the CONSOLE requires ONE network interface and the SENSORS require TWO network interfaces.  The SPAN port is required for SENSORS.

If you are going to set up a distributed IPS, the CONSOLE requires ONE network interface and the SENSORS require THREE network interfaces. 

You can also combine CONSOLE and SENSOR into one box, as known as STANDARD.  While STANDARD can also act as "CONSOLE" to handle other distributed SENSORS.  We call this setup as Nested Distributed System.

For IDS, you can have Snort and Suricata in one box.  The web interface (Snorby) will handle them without any problem.

For IPS, you must set Snort and Suricata in two different boxes.  However, you can have one web interface (Snorby) to handle the two sensors (boxes).  The web interface can be at either one of the boxes, that is a nested distributed system.

<h3>Part II - Maintenance</h3>

To update or upgrade the SmoothSec, you can issue the following commands with root privileges.

sudo apt-get update
sudo apt-get dist-upgrade

To update or upgrade the scripts, you can issue the following commands with root privileges.

cd /root/updates
git pull

(Then run the scripts that downloaded.)

<h3>Part III - Intrusion Detection System</h3>

Make sure you do not enter a wrong answer as the setup script has no error checking feature.

(C) Standard

eth0 - interface for capture (monitoring)
eth1 - interface for management (for web interface access)

Make sure eth0 is connected to SPAN (or port mirroring) port.

To run the following commands, you should have root privileges.

smoothsec.first.setup
standard

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset
reboot

(D) Console

eth0 - interface for management (for web interface access and SSH tunnel)

To run the following commands, you should have root privileges.

smoothsec.first.setup
console

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset
reboot

(E) Sensor

eth0 - interface for capture (or monitoring)
eth1 - interface for management (for SSH tunnel)

Make sure eth0 is connected to SPAN (or port mirroring) port.

To run the following commands, you should have root privileges.

smoothsec.first.setup
sensor

Then answer the questions on the screen according to your network as well as the setting of "console".

To reset back to the fresh install, you can issue the following command.

smoothsec.reset
reboot

(F) Switch Engines

You can switch to Snort from Suricata or vice versa.  Or even you can install both of them by issue the following command.

To run the following command, you should have root privileges.

smoothsec.switch.engine

<h3>Part IV - Intrusion Prevention System</h3>

The setup may be something like this.

internet -- router (with firewall) -- SmoothSec (IPS) -- switch -- computers

Before going to set up an Intrusion Prevention System with SmoothSec, you should understand the following variables.

AF_ENGINE - Select snort or suricata (default is snort). When selected suricata, a new kernel will be downloaded and installed automatically.

RULES - et or vrt (default is et, if you select vrt you need get the code to operate)

(a) This section may require to edit when setting up Standard and Distributed (Sensor)

AF_IFACE_0 - One of the AF_PACKET capture interfaces, default is eth0

AF_IFACE_1 - The other AF_PACKET capture interfaces, default is eth1

AF_MANAGE_IFACE - The interface to manage the IPS (web interface when Standard), default is eth2

(b) This section may require to edit when setting up Standard and Distributed (Sensor)

AF_SENSOR_IP - The sensor IP address, which is also the IP address of AF_MANAGE_IFACE and Console IP address

AF_GATEWAY - The gateway of the AF_SENSOR_IP (or AF_MANAGE_IFACE) network

AF_HOME_NETWORK - The subnet of AF_SENSOR_IP (or AF_MANAGE_IFACE)

In the middle of the setup, you will ask to edit the captioned variables according to your network setting.

The editor to edit the config file is namely nano. You can save the content with CTRL+o and exit with CTRL+x.

Make sure you do not enter a wrong answer as the setup script has no error checking feature.

(G) Standard

eth0 - interface for capture (incoming monitoring)
eth1 - interface for capture (outgoing monitoring)
eth2 - interface for management (for web interface access)

To run the following commands, you should have root privileges.

smoothsec.first.setup
ips-standard

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset
reboot

(H) Console

eth0 - interface for management (for web interface access and SSH tunnel)

To run the following commands, you should have root privileges.

smoothsec.first.setup
ips-console

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset
reboot

(I) Sensor

eth0 - interface for capture (incoming monitoring)
eth1 - interface for capture (outgoing monitoring)
eth2 - interface for management (for SSH tunnel)

To run the following commands, you should have root privileges.

smoothsec.first.setup
ips-sensor

Then answer the questions on the screen according to your network as well as the setting of "console".

To reset back to the fresh install, you can issue the following command.

smoothsec.reset
reboot

<h3>Part V - Rules Handling</h3>

If you want to disable some rules as they are false positive, you can edit the disablesid.conf of pulledpork.

For Snort -

cd /etc/pulledpork/snort
nano disablesid.conf

For Suricata -

cd /etc/pulledpork/suricata
nano disablesid.conf

If you are running IPS and you want to drop some traffic, you can edit the dropsid.conf of pulledpork.

For Snort -

cd /etc/pulldpork/snort
nano dropsid.conf

For Suricata -

cd /etc/pulledpork/suricata
nano dropsid.conf

If you want to modify some rules, you can edit the modifysid.conf of pulledpork.

For Snort -

cd /etc/pulledpork/snort
nano modifysid.conf

For Suricata -

cd /etc/pulledpork/suricata
nano modifysid.conf

After updated the pulledpork, you should run the following command to make the changes effective.

For Snort -

smoothsec.snort.rules.update

For Suricata -

smoothsec.suricata.rules.update

<h3>Part VI - Hardening SmoothSec</h3>

You may consider to jail root Apache of the SmoothSec with Apparmor.

sudo apt-get update
sudo apt-get install apparmor apparmor-profiles apparmor-utils

Please refer the documentation of Debian for using/setup Apparmor with Apache.

You may consider to activate the fail2ban application to protect your SSH connection.

In addition, make sure your passwords are very strong to prevent from being brute forcing.

<h3>Part VII - General Information</h3>

Suricata comes without scanner module.  Therefore, it will not response to any NMAP scanning or likewise.


- END -
