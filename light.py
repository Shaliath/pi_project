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
		lightStatus = True

def switchingOffTheLight():
	if lightStatus:
		#Switching off the light
		return "Light switching off"
		lightStatus = False
	else:
		return "Light is already switched off"