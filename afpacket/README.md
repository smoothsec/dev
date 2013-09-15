<h2>SmoothSec 3.4 with AF_PACKET</h2>

The folder contents all files for Snort/Suricata Inline mode with AF_PACKET.

<h3>Features</h3>

Standard - Web Console and Sensor in one box

Distributed - One Web Console and many Sensors in the network

Easy to configure and deploy.  Working on phyiscal hardware and virtual machines.

Supports Snort and Suricata in Inline mode (IPS - Intrusion Prevention System)

<h3>Configuration</h3>

During the installation, you are required to configure a config file by editor.

Three network interfaces are required to this setup.  If you are running SmoothSec in virtual machine, this setup will require 4 network interfaces.

You may need to change the following values when setting up the IPS :

AF_ENGINE - Select snort or suricata (default is snort).  When selected suricata, a new kernel will be downloaded and installed automatically.

RULES - et or vrt (default is et, if you select vrt you need get the code to operate)


- This section may require to edit when setting up Standard and Distributed (Sensor)

AF_IFACE_0 - One of the AF_PACKET capture interfaces, default is eth0

AF_IFACE_1 - The other AF_PACKET capture interfaces, default is eth1

AF_MANAGE_IFACE - The interface to manage the IPS, default is eth2


- This section may require to edit when setting up Standard and Distributed (Sensor)

AF_SENSOR_IP - The sensor IP address, which is also the IP address of AF_MANAGE_IFACE and Console IP address

AF_GATEWAY - The gateway of the AF_SENSOR_IP (or AF_MANAGE_IFACE) network

AF_HOME_NETWORK - The subnet of AF_SENSOR_IP

The editor to edit the config file is namely nano.  You can save the content with 
CTRL+o and exit with CTRL+x.

<h3>Remarks</h3>

Normally, all the required files are in position.  If there are some fixes, you can
download them and install them yourself.

<code>wget https://github.com/smoothsec/dev/archive/samiux.zip</code>

<code>unzip samiux.zip</code>

<code>cd dev-samiux/afpacket/3.4/</code>

<code>sudo ./smoothsec.afpacket.initialize</code>


