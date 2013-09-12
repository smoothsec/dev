This folder is designed for SmoothSec 3.4 or higher.  This folder is under heavy development.  Changes and bugs may be expected.

You can download the Alpha3 version of SmoothSec 3.4 at <code>http://bailey.st/files/alpha3.smoothsec-3.4-amd64.iso</code>.

The following scripts are for delopying Suricata (inline mode and IDS mode) and Snort (inline mode)  with AF_PACKET.

<h3>Download and install the scripts</h3>

<code>wget https://github.com/smoothsec/dev/archive/samiux.zip</code>

<code>apt-get install unzip</code>

<code>unzip samiux.zip</code>

<code>cd dev-samiux/afpacket/</code>

<code>./smoothsec.afpacket.initialize</code>

<h3>Delopying Suricata with AF_PACKET</h3>

You need 3 network interface cards, such as eth0, eth1 and eth2.  If you want to use eth0 and eth1 for the AF_PACKET capture, you should use eth2 as management interface.

router -- Smoothsec -- switch -- computers

First of all, you need to run <code>smoothsec.first.setup</code>.  Answer <code>eth0</code> for the monitor interface and complete the installation.  
Make sure you select same engine here and <code>smoothsec.afpacket.setup</code>.  After that, you need to reboot.

Make sure you are root.  Then run <code>smoothsec.afpacket.setup</code>.  A nano editor will be shown up with the <code>afpacket.cfg</code> file.

Just edit when necessary.

AF_MODE - when deploying Suricata with AF_PACKET in IPS mode, you need to type ips while IDS mode you need to type tap.

AF_ENGINE - you can select suricata or snort.  However, snort version is under development.

AF_CORE - it will find out how many core of your CPU.

AF_BUFFER_SIZE - the buffer size of Snort afpacket mode.  Default is 128MB.  If you have more than 4GB RAM, you can adjust to larger number of MB.
                 If you not sure, DO NOT change it.

AF_IFACE_0 - this is the first network interface for AF_PACKET capture.

AF_IFACE_1 - this is the second network interface for AF_PACKET capture.

AF_MANAGE_IFACE - this is network interface for management purpose.

AF_SENSOR_IP - exactly this is not the sensor IP address but management interface IP address.

AF_GATEWAY - the gateway IP address of your network.

AF_HOME_NETWORK - the subnet of your network.

AF_SETUP - DO NOT TOUCH THIS SETTINGS; OTHERWISE, YOUR SYSTEM WILL BE BROKEN.

<h3>Reset the deployment</h3>

When you want to reset the AF_PACKET deployment back to the <code>smoothsec.first.setup</code> environment, you just run the following command :

Make sure you are root.

<code>smoothsec.afpacket.reset</code>

If you want to reset the box to the fresh install, you can run the following command then :

Make sure you are root.

<code>smoothsec.reset</code>

<h3>Remarks</h3>

Snort and Suricata cannot be co-existence in inline mode (IPS mode).  If you want to have both engines, you may consider to deploy distributed IDS/IPS, then you will need at least 3 machines, 
one for Snort, one for Suricata and one for management.  However, they can be co-existence in IDS mode.  

Snorby web interface cannot show the dropped traffic at the moment.  If you want, please ask developers of Snorby to do so.

<h3>File Description</h3>

smoothsec.afpacket.setup - This is a setup script for Suricata with AF_PACKET.  Please run smoothsec.first.setup before running this script.
                           This file is placed at /usr/local/sbin/.

smoothsec.afpacket.reset - This is a uninstall script for the purpose.  This file is placed at /usr/local/sbin/.

afpacket.cfg - This is a configure file and it is placed at /etc/.

interfaces.afpacket.template - /etc/network/interface template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.

sagan.conf.template - /etc/sagan/sagan.conf template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.

sagan.template - /etc/init.d/sagan template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.

smoothsec.afpacket.initialize - This is a initialize file and designed for this download version.  The official SmoothSec 3.4 or higher will not come with this file.

suricata-afpacket.template - /etc/init.d/suricata template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.

snort-afpacket.template - /etc/init.d/snort template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.

suricata-afpacket.yaml.template - /etc/suricata/suricata.yaml template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.



