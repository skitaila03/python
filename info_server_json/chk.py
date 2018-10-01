import os
import psutil
import sys
import subprocess
import socket
import hashlib 

def console_print(Message):
	return print(Message)

def sub_process(Param):
	return subprocess.Popen(Param, shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

def get_md5_sum(filePath):
	with open(filePath, 'rb') as fh:
		m = hashlib.md5()
		while True:
			data = fh.read(8192)
			if not data:
				break

			m.update(data)

		return m.hexdigest()

def get_hostname():
	return socket.gethostname()

def get_cpu_percent(Interval=None):
	return psutil.cpu_percent(Interval)

def get_cpu_logical():
	return psutil.cpu_count(logical=True)

def get_cpu_psychical():
	return psutil.cpu_count(logical=False)

def get_virtual_memory(Params = False):
	mem = psutil.virtual_memory()
	
	if Params == False or Params == "total":
		total = mem.total >> 20
	elif Params == "percent":
		total = mem.percent
	elif Params == "available":
		total = mem.total >> 20
	elif Params == "used":
		total = mem.used >> 20
	elif Params == "free":
		total = mem.free >> 20

	return total

def get_swap_memory(Params = False):
	swap = psutil.swap_memory()

	if Params == False or Params == "total":
		total = swap.total >> 20
	elif Params == "percent":
		total = swap.percent
	elif Params == "used":
		total = swap.used >> 20
	elif Params == "free":
		total = swap.free >> 20

	return total

def get_disk_usage(Path = False, Params = False):
	if Path:
		if Params == False:
			return psutil.disk_usage(Path)
		elif Params == "total":
			return psutil.disk_usage(Path).total >> 20
		elif Params == "used":
			return psutil.disk_usage(Path).used >> 20
		elif Params == "free":
			return psutil.disk_usage(Path).free >> 20
	else:
                if Params == False:
                        return psutil.disk_usage("/")
                elif Params == "total":
                        return psutil.disk_usage("/").total >> 20
                elif Params == "used":
                        return psutil.disk_usage("/").used >> 20
                elif Params == "free":
                        return psutil.disk_usage("/").free >> 20

def get_disk_partitions(Params=False):
	return psutil.disk_partitions(Params)

def get_disk_total():
	return sub_process("df -h --output=size --total | awk 'END {print $1}'")

def get_disk_available():
	return sub_process("df -h --output=avail --total | awk 'END {print $1}'")

def get_load():
	return sub_process("cat /proc/loadavg")

def get_local_ip():
	return sub_process("hostname -I | cut -d' ' -f1")

def get_public_ip():		
	return sub_process("curl ipinfo.io/ip"),

def get_pwd():
	return os.getcwd()

def get_kernel_os():
	return sub_process("uname -s")

def get_kernel_release():
	return sub_process("uname -r")

def get_kernel_architecture():
	return sub_process("uname -i")

def get_kernel():
	return os.uname()

def get_login():
	return os.getlogin()

def get_group_id():
	return os.getpgrp()

