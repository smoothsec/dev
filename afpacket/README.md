This folder is designed for SmoothSec 3.4 or higher.  This folder is under heavy development.  Changes and bugs may be expected.

The following scripts are for delopying Suricata inline mode and IDS mode with AF_PACKET.  The Snort version is devleoping.

<h3>Download and install the scripts</3>

<code>wget https://github.com/smoothsec/dev/archive/samiux.zip

apt-get install unzip
unzip samiux.zip

cd dev-samiux/afpacket/

./smoothsec.afpacket.initialize</code>

<h3>Delopying Suricata with AF_PACKET</h3>

You need 3 network interface cards, such as eth0, eth1 and eth2.  If you want to use eth0 and eth1 for the AF_PACKET capture, you should use eth2 as management interface.

router -- Smoothsec -- switch -- computers

First of all, you need to run smoothsec.first.setup but no need to reboot.

Make sure you are root.  Then run smoothsec.afpacket.setup.  A nano editor will be shown up with the afpacket.cfg file.

Just edit when necessary.

AF_MODE - when deploying Suricata with AF_PACKET in IPS mode, you need to type ips while IDS mode you need to type tap.

AF_ENGINE - you can select suricata or snort.  However, snort version is under development.

AF_CORE - it will find out how many core of your CPU.

AF_IFACE_0 - this is the first network interface for AF_PACKET capture.

AF_IFACE_1 - this is the second network interface for AF_PACKET capture.

AF_MANAGE_IFACE - this is network interface for management purpose.

AF_SENSOR_IP - exactly this is not the sensor IP address but management interface IP address.

AF_GATEWAY - the gateway IP address of your network.

AF_HOME_NETWORK - the subnet of your network.

AF_SETUP - DO NOT TOUCH THIS SETTINGS; OTHERWISE, YOUR SYSTEM WILL BE BROKEN.

<h3>Reset the deployment</h3>

When you want to reset the AF_PACKET deployment back to the smoothsec.first.setup environment, you just run the following command :

<code>smoothsec.afpacket.reset</code>

If you want to reset the box to the fresh install, you can run the following command then :

<code>smoothsec.reset</code>

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

suricata-afpacket.yaml.template - /etc/suricata/suricata.yaml template file.  This file is placed at /usr/local/smoothsec/confs/afpacket/.



