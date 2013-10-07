SmoothSec - Intrusion Detection/Prevention Made Simple

Website : http://www.smoothsec.org

<h3>Something You Should Know Before Installing SmoothSec</h3>

<b>(A) Intrusion Detection System (IDS)</b>

First of all, you are required to have ONLY ONE network interface for the 
SmoothSec IDS.  There is NO so-called management interface in our design.  
Meanwhile, the cable of that network interface is NOT required to connect
to the SPAN (or Port Mirroring) port.

Secondary, the IP address of that network interface should be assigned by
DHCP.  Otherwise, the SmoothSec will be broken or acting abnormal.

Finally, you should at least equipped with 4GB RAM and 300GB hard drive.  
In our lab, we have tested Intel Atom D510 and D2250 with 4GB RAM which are 
running properly and smooth for a home or SOHO environment.  That is the hints
for purchasing hardware for deploying SmoothSec.

<b>(B) Intrusion Prevention System (IPS)</b> 

First of all, you are required THREE network interfaces.  Two for the incoming
and outgoing traffic capture; the other ONE is for management purpose.

Secondary, the IP address of the management network interface is a static IP
which will be set while running "smoothsec.first.setup" script.

Thirdly, make sure you change the configure file when setting up the SmoothSec.
For example, which engine?  Snort or Suricata?

Finally, you should at least equipped with 4GB RAM and 300GB hard drive.
In our lab, we have tested Intel Atom D510 and D2250 with 4GB RAM which are
running properly and smooth for a home or SOHO environment.  That is the hints
for purchasing hardware for deploying SmoothSec.

<b>(C) General Information</b>

Suricata does not come with port scanning module.  Therefore, it will not
response to any NMAP scanning.

Both Snort and Suricata in SmoothSec are using Emergening Threat rules by 
default.  If you want to use purchased version of the rules, you should 
change something in the configure file of Snort or Suricata.

For IDS, you can install both Snort and Suricata engines in one box.  You
just install one of the engines and then run "smoothsec.switch.engine" to
install the other engine or switch to another engine when need.

For IPS, you can also deploy both Snort and Suricata.  However, you need two
boxes.  One for Snort and one for Suricata.  One is installed as "ips-standard" 
and the other is installed as "ips-sensor".  The management interface will be 
at "ips-standard" box.

Samiux
October 8, 2013

