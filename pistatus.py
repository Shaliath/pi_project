import subprocess

def cpuTemp():
	first = int(subprocess.Popen("cat /sys/devices/virtual/thermal/thermal_zone1/temp", shell = True, stdout = subprocess.PIPE).stdout.read())
	second = int(subprocess.Popen("cat /sys/devices/virtual/thermal/thermal_zone0/temp", shell = True, stdout = subprocess.PIPE).stdout.read())
	return str((first + second)/2.0)