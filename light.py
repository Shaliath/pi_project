lightStatus = False

def checkLightStatus():
	if lightStatus:
		return "On"
	return "Off"

def switchingOnTheLight():
	global lightStatus
	if lightStatus:
		return "Light is already switched on"
	else:
		#Switching on the light
		lightStatus = True
		return "Light switching on"

def switchingOffTheLight():
	global lightStatus
	if lightStatus:
		#Switching off the light
		lightStatus = False
		return "Light switching off"
	else:
		return "Light is already switched off"