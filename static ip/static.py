import subprocess

def sub_process(Param):
	return subprocess.Popen(Param, shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

def generate_uuid(Param):
	return sub_process("uuidgen " + Param)

def ip_up(Param):
	return sub_process("ifup " + Param)

def ip_down(Param):
	return sub_process("ifdown " + Param)

interface = "ifcfg-" + raw_input("Interface name?: ")
ip = raw_input("Insert Static IP: ")
ifcfg,enp0 = interface.split("-")

file = open("/etc/sysconfig/network-scripts/" + interface, "w")
file.write("TYPE=Ethernet\n")
file.write("PROXY_METHOD=none\n")
file.write("BROWSER_ONLY=no\n")
file.write("BOOTPROTO=static\n")
file.write("IPADDR=" + ip + "\n")
file.write("NETMASK=255.255.255.0\n")
file.write("NM_CONTROLLED=no\n")
file.write("DEFROUTE=yes\n")
file.write("IPV4_FAILURE_FATAL=no\n")
file.write("IPV6INIT=no\n")
file.write("IPV6_AUTOCONF=yes\n")
file.write("IPV6_DEFROUTE=yes\n")
file.write("IPV6_FAILURE_FATAL=no\n")
file.write("IPV6_ADDR_GEN_MODE=stable-privacy\n")
file.write("NAME=" + enp0 + "\n")
file.write("UUID=" + generate_uuid(enp0) + "\n")
file.write("DEVICE=" + enp0 + "\n")
file.write("USERCTL=no\n")
file.write("ONBOOT=yes\n")
file.close

print "Creating " + interface + "in /etc/sysconfig/network-scripts"
print "Restarting " + enp0
ip_down(enp0)
ip_up(enp0)
print "Done"