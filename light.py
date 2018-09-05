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
		return "Light switching on"
		lightStatus = True

def switchingOffTheLight():
	global lightStatus
	if lightStatus:
		#Switching off the light
		return "Light switching off"
		lightStatus = False
	else:
		return "Light is already switched off"