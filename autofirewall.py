#!/usr/bin/python
# AutoFirewall Layer4/Layer3 Protec/Shld.
# Coded by Ertugrul TURAN / T13R / V4
# NinjaNetwork - www.Obir.Ninja
import os
import time
timer = time.sleep
os.system("clear")
timer(0.25)
os.system("curl -O http://www.inetbase.com/scripts/ddos/install.sh || wget http://www.inetbase.com/scripts/ddos/install.sh")
os.system("bash install.sh > /dev/null 2>/dev/null &")
print("Waiting..")
timer(5.25)
os.system("pkill install.sh")
os.system("curl -O http://www.rfxn.com/downloads/apf-current.tar.gz || wget http://www.rfxn.com/downloads/apf-current.tar.gz")
os.system("tar -xzf apf-current.tar.gz")
os.system("rm -rf apf-current.tar.gz")
os.system("mv apf-1.7.6 .fw")
os.system("bash .fw/install.sh")
os.system("echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts")
os.system("echo 0 > /proc/sys/net/ipv4/conf/all/accept_source_route")
os.system("echo 1 > /proc/sys/net/ipv4/tcp_syncookies")
os.system("echo 0 > /proc/sys/net/ipv4/conf/all/accept_redirects")
os.system("echo 0 > /proc/sys/net/ipv4/conf/all/send_redirects")
os.system("echo 1 > /proc/sys/net/ipv4/conf/all/rp_filter")
os.system("echo 1 > /proc/sys/net/ipv4/conf/all/log_martians")
os.system("/sbin/iptables --flush")
os.system("/sbin/iptables -A INPUT -i lo -j ACCEPT")
os.system("/sbin/iptables -A OUTPUT -o lo -j ACCEPT")
os.system("/sbin/iptables --policy INPUT DROP")
os.system("/sbin/iptables --policy OUTPUT DROP")
os.system("/sbin/iptables --policy FORWARD DROP")
os.system("/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
os.system("/sbin/iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT")
os.system("/sbin/iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP")
os.system("/sbin/iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set")
os.system("/sbin/iptables -A INPUT -p tcp --dport 22 -m state --state NEW -j ACCEPT")
os.system("/sbin/iptables -A INPUT -p tcp --dport 25565 -m state --state NEW -j ACCEPT") 
os.system("/sbin/iptables -A INPUT -p tcp --dport 8123 -m state --state NEW -j ACCEPT")
os.system("/sbin/iptables -A INPUT -p tcp --dport 80 -m state --state NEW -j ACCEPT")
os.system("/sbin/iptables -A INPUT -p tcp --dport 443 -m state --state NEW -j ACCEPT")
os.system("/sbin/iptables -A INPUT -p udp --dport 5021 -m state --state NEW -j ACCEPT")
os.system("/sbin/iptables -A INPUT -p icmp --icmp-type 8 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT")
os.system("/sbin/iptables -A INPUT -j DROP")
os.system("/sbin/iptables -nL")
timer(3.25)
os.system("clear")
timer(1.25)
print("Edit Rule /usr/local/ddos/ddos.conf")
