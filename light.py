lightStatus = False

def checkLightStatus():
	if lightStatus:
		return "On"
	return "Off"

def switchingOnTheLight():
	if lightStatus:
		return "Light is already switched on"
	else:
		#Switching on the light
		return "Light switching on"

def switchingOffTheLight():
	if lightStatus:
		#Switching off the light
		return "Light switching off"
	else:
		return "Light is already switched off"