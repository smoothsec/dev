# SmoothSec Without Tears

Editor  : Samiux<br>
Version : 0.3<br>
Dated   : January 30, 2014<br>
 
## Part I - Introduction

SmoothSec is a lightweight and fully-ready IDS/IPS (Intrusion Detection/Prevention System) Linux distribution based on Debian, available for 32 and 64-bit architecture.  An easy setup process allows to deploy a complete IDS/IPS system within minutes, even for security beginners with minimal Linux experience.

The current version of SmoothSec is 3.4-1.


Main components :

Debian 7 with Backports kernel<br>
Snorby - a web interface to manage the captured traffic data<br>
Snort - a IDS/IPS Engine<br>
Suricata - a IDS/IPS Engine<br>
Sagan - a HIDS Engine (installed by default)<br>
PulledPork - a Snort/Suricata rules management tool<br>
Pigsty - a traffic spooler<br>

Additional tools :

tcpxtract - a tool for extracting files from network traffic<br>
netdiscover - an active/passive address reconnaissance tool<br>
ngrep - a pcap-aware tool which search data payloads of packets by regular exprssions<br>
nast - a packet sniffer and a LAN analyzer<br>
ipgrab - a verbose packet sniffer<br>
tshark - dump and analyze network traffic<br>
greppcap.py - a tool to find data in a pcap format using regular expression<br>
percona-toolkit - a MySQL collection of advanced command-line tools<br>
percona-xtrabackup - a MySQL backup tool<br>

### (A) Minimum Hardware Requirement

At least an Atom D510 CPU with 2 GB RAM and 20 GB storage.  Two network interfaces for IDS and Three network interfaces for IPS setup.  For IDS setup, a switch with SPAN (or port mirroring) port is required.  If you have a home switch (so-called switch) or virtual switch (running on a virtual machine), you are not required a SPAN port as those are not a REAL switches.

The better hardware is the better performance.

### (B) Structure 

If you are going to set up a distributed IDS, the CONSOLE requires ONE network interface and the SENSORS require TWO network interfaces.  The SPAN port is required for SENSORS.

If you are going to set up a distributed IPS, the CONSOLE requires ONE network interface and the SENSORS require THREE network interfaces. 

You can also combine CONSOLE and SENSOR into one box, as known as STANDARD.  While STANDARD can also act as "CONSOLE" to handle other distributed SENSORS.  We call this setup as Nested Distributed System.

For IDS, you can have Snort and Suricata in one box.  The web interface (Snorby) will handle them without any problem.

For IPS, you must set Snort and Suricata in two different boxes.  However, you can have one web interface (Snorby) to handle the two sensors (boxes).  The web interface can be at either one of the boxes, that is a nested distributed system.

## Part II - Maintenance

To run the following commands, make sure you have root privileges.

### SmoothSec update/upgrade

To update or upgrade the SmoothSec, you can issue the following commands with root privileges.

sudo apt-get update<br>
sudo apt-get upgrade<br>

To update or upgrade the scripts, you can issue the following commands with root privileges.

cd /root/updates<br>
git pull<br>

(Then run the scripts that downloaded.)

### Pigsty update/upgrade

npm update -g pigsty<br>
npm update -g pigsty-mysql<br>

### Snorby update/upgrade

cd /var/www/snorby<br>
git pull origin master<br>
rake snorby:update<br>

### Snort and Suricata update/upgrade

apt-get update<br>
apt-get dist-upgrade<br>

## Part III - Intrusion Detection System

Make sure you do not enter a wrong answer as the setup script has no error checking feature.

### (C) Standard

eth0 - interface for capture (monitoring)<br>
eth1 - interface for management (for web interface access)<br>

Make sure eth0 is connected to SPAN (or port mirroring) port.

To run the following commands, you should have root privileges.

smoothsec.first.setup<br>
standard<br>
reboot<br>

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset<br>
reboot<br>

### (D) Console

eth0 - interface for management (for web interface access and SSH tunnel)

To run the following commands, you should have root privileges.

smoothsec.first.setup<br>
console<br>
reboot<br>

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset<br>
reboot<br>

### (E) Sensor

eth0 - interface for capture (or monitoring)<br>
eth1 - interface for management (for SSH tunnel)<br>

Make sure eth0 is connected to SPAN (or port mirroring) port.

To run the following commands, you should have root privileges.

smoothsec.first.setup<br>
sensor<br>
reboot<br>

Then answer the questions on the screen according to your network as well as the setting of "console".

To reset back to the fresh install, you can issue the following command.

smoothsec.reset<br>
reboot<br>

### (F) Switch Engines

You can switch to Snort from Suricata or vice versa.  Or even you can install both of them by issue the following command.

To run the following command, you should have root privileges.

smoothsec.switch.engine

## Part IV - Intrusion Prevention System

The setup may be something like this.

internet -- SmoothSec (IPS) router (with firewall) -- switch -- computers

Update the kernel to backports version as Suricata (af_packet) only works on kernel 3.6 or later :

sudo nano /etc/apt/sources.list

Append the following line to the /etc/apt/source.list -

deb http://ftp.debian.org/debian/ wheezy-backports main non-free contrib

Save and exit by Ctrl-o and Ctrl-x.

Then run the following command -

sudo apt-get update<br>
sudo apt-get -t wheezy-backports install linux-image-amd64 linux-headers-amd64<br>

After that, reboot the Smoothsec.<br>

After the reboot, you need to update the Smoothsec script to version 3.6 -

wget https://github.com/smoothsec/dev/archive/samiux.zip<br>
unzip samiux.zip<br>
cd dev-samiux/afpacket/3.6/<br>
rm README.md<br>
sudo cp -Ra * /<br>

cd ..<br>
rm -R dev-samiux<br>
rm samiux.zip<br>

The script is updated.


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

### (G) IPS Standard

eth0 - interface for capture (incoming monitoring)<br>
eth1 - interface for capture (outgoing monitoring)<br>
eth2 - interface for management (for web interface access)<br>

To run the following commands, you should have root privileges.

smoothsec.first.setup<br>
ips-standard<br>
reboot<br>

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset<br>
reboot<br>

### (H) IPS Console

eth0 - interface for management (for web interface access and SSH tunnel)

To run the following commands, you should have root privileges.

smoothsec.first.setup<br>
ips-console<br>
reboot<br>

Then answer the questions on the screen according to your network.

To reset back to the fresh install, you can issue the following command.

smoothsec.reset<br>
reboot<br>

### (I) IPS Sensor

eth0 - interface for capture (incoming monitoring)<br>
eth1 - interface for capture (outgoing monitoring)<br>
eth2 - interface for management (for SSH tunnel)<br>

To run the following commands, you should have root privileges.

smoothsec.first.setup<br>
ips-sensor<br>
reboot<br>

Then answer the questions on the screen according to your network as well as the setting of "console".

To reset back to the fresh install, you can issue the following command.

smoothsec.reset<br>
reboot<br>

## Part V - Rules Handling

If you want to disable some rules as they are false positive, you can edit the disablesid.conf of pulledpork.

For Snort -

cd /etc/pulledpork/snort<br>
nano disablesid.conf<br>

For Suricata -

cd /etc/pulledpork/suricata<br>
nano disablesid.conf<br>

If you are running IPS and you want to drop some traffic, you can edit the dropsid.conf of pulledpork.

For Snort -

cd /etc/pulldpork/snort<br>
nano dropsid.conf<br>

For Suricata -

cd /etc/pulledpork/suricata<br>
nano dropsid.conf<br>

If you want to modify some rules, you can edit the modifysid.conf of pulledpork.

For Snort -

cd /etc/pulledpork/snort<br>
nano modifysid.conf<br>

For Suricata -

cd /etc/pulledpork/suricata<br>
nano modifysid.conf<br>

After updated the pulledpork, you should run the following command to make the changes effective.

For Snort -

smoothsec.snort.rules.update

For Suricata -

smoothsec.suricata.rules.update

## Part VI - Signatures Lookup url (Snorby)

[Signatures Lookup URL](https://github.com/Snorby/snorby/wiki/Rule-lookups)

For ET rules signatures lookup URL :

http://doc.emergingthreats.net/bin/view/Main/$$sid$$

## Part VII - Hardening SmoothSec

You may consider to jail root Apache of the SmoothSec with Apparmor.

sudo apt-get update<br>
sudo apt-get install apparmor apparmor-profiles apparmor-utils<br>

Please refer the documentation of Debian for using/setup Apparmor with Apache.

You may consider to activate the fail2ban application to protect your SSH connection.

In addition, make sure your passwords are very strong to prevent from being brute forcing.

## Part VIII - General Information

Suricata comes without scanner module.  Therefore, it will not response to any NMAP scanning or likewise.


