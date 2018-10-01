from flask import Flask
from flask_restful import Resource, Api
import sys
import smtplib
import chk

#silent = sys.argv[1]
 
app = Flask(__name__)
api = Api(app)

if len(sys.argv) > 1:
	get_silent = sys.argv[1]

	if get_silent == "--silent":
		silent = "yes"
		print("Starting in silent mode")
else:
	silent = "no"

if silent == "no":
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.starttls()
	#mail.login("email@gmail.com", "password")
	mail_sender = "send@gmail.com"
	mail_receiver = "recv@gmail.com"
	mail.login(mail_sender, "pass")

class SysInfo(Resource):
	def md5_new(self, Path, Var):
		if chk.get_md5_sum(Path) != Var:
			Var = chk.get_md5_sum(Path)

			global secure_old_md5
			global passwd_old_md5
			global wtmp_old_md5

			global count_secure
			global count_passwd
			global count_wtmp

			if Var != secure_old_md5 and Path == "/var/log/secure":
				print("changes on secure")

				if silent == "no":
					msg = "\nchanges on /var/log/secure on machine:"
					msg += chk.get_hostname()
					mail.sendmail(mail_sender, mail_receiver, msg)
		
				count_secure += 1
				secure_old_md5 = Var

			if Var != passwd_old_md5 and Path == "/etc/passwd":
				print("changes on passwd")
				
				if silent == "no":
					msg = "\nchanges on /etc/passwd on machine:"
					msg += chk.get_hostname()
					mail.sendmail(mail_sender, mail_receiver, msg)
	
				count_passwd += 1
				passwd_old_md5 = Var

			if Var != wtmp_old_md5 and Path == "/var/log/wtmp":
				print("changes on wtmp")

				if silent == "no":
					msg = "\nchanges on /var/log/wtmp on machine:"
					msg += chk.get_hostname()
					mail.sendmail(mail_sender, mail_receiver, msg)
			
				count_wtmp += 1
				wtmp_old_md5 = Var

			return Var
		else:
			return chk.get_md5_sum(Path)

	def trigger_percent(self, Param):
		if Param == "cpu":
			message = "\ncpu overflow"
			percent = float(chk.get_cpu_percent())
	
		elif Param == "memory":
			message = "\nmemory overflow"
			percent = float(chk.get_virtual_memory("percent"))

		elif Param == "swap":
			message = "\nswap overflow"
			percent = float(chk.get_swap_memory("percent"))

		print(message)
		if silent == "no":
			if percent > 80.0:
				msg += " on machine:"
				msg += chk.get_hostname()
				mail.sendmail(mail_sender, mail_receiver, msg)

		return percent	
	
	def get(self):
		return {
			'hostname': chk.get_hostname(),
			'os': chk.get_kernel_os(),
			'architecture': chk.get_kernel_architecture(),
			'kernel': chk.get_kernel_release(),
			'ip_public': chk.get_public_ip(),
			'ip_local': chk.get_local_ip(),
			'load': chk.get_load(),
			'cpu':{
				'logical':  chk.get_cpu_logical(),
				'psychical': chk.get_cpu_psychical(),
				'percent':  self.trigger_percent("cpu")
			},
			'hdd':{
				'total': chk.get_disk_total(),
				'available': chk.get_disk_available()
			},
			'memory':{
				'total': chk.get_virtual_memory("total"),
				'percent': self.trigger_percent("memory"),
				'available': chk.get_virtual_memory("available"), 
				'used': chk.get_virtual_memory("used"),
				'free': chk.get_virtual_memory("free")
			},
			'swap':{
				'total': chk.get_swap_memory("total"),
				'percent': self.trigger_percent("swap"),
				'used': chk.get_swap_memory("used"),
				'free': chk.get_swap_memory("free")
			},
			'logs':{
				'/etc/passwd':{
					'old_md5': passwd_old_md5,
					'new_md5': self.md5_new("/etc/passwd", passwd_old_md5),
					'changes': count_passwd
				},
				'/var/log/secure':{
					'old_md5': secure_old_md5,
					'new_md5': self.md5_new("/var/log/secure", secure_old_md5),
					'changes': count_secure
				},
				'/var/log/wtmp':{
					'old_md5': wtmp_old_md5,
					'new_md5': self.md5_new("/var/log/wtmp", wtmp_old_md5),
					'changes': count_wtmp
				}
			},
			'silent': silent
			}

sys = SysInfo()
count_secure = 0
count_passwd = 0
count_wtmp = 0
secure_old_md5 = chk.get_md5_sum('/var/log/secure')
passwd_old_md5 = chk.get_md5_sum('/etc/passwd')
wtmp_old_md5 = chk.get_md5_sum('/var/log/wtmp')
api.add_resource(SysInfo, '/api')

if __name__ == '__main__':
	app.run(host='vm1.incrys.com', debug=True)

	if silent == "no":
		mail.quit()	
