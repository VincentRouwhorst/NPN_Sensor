#!/usr/bin/python
#https://www.domoticz.com/wiki/Domoticz_API/JSON_URL's#Update_devices.2Fsensors

import requests

DOMOTICZ_IP = 'http://127.0.0.1:8080'
IDX = '1'
TEMP = '2'
HUM = '3'
HUM_STAT = '4'
BAR = '5'
BAR_FOR = '6'
ALTITUDE = '7'
RAINRATE = '8'
RAINCOUNTER = '9'
MOISTURE = '10'
WB = '11' #Wind bearing (0-359)
WD = '12' #Wind direction (S, SW, NNW, etc.)
WS = '13' #10 * Wind speed [m/s]
WG = '14' #10 * Gust [m/s]
TEMPUV = '0' #Temperature
WINDCHILL = '16' #Temperature Windchill
UV = '17'
COUNTER = '18'
POWER = '19'
ENERGY = '20'
Ampere1 = '21'
Ampere2 = '22'
Ampere3 = '23'
USAGE1 = '24'
USAGE2 = '25'
RETURN1 = '26'
RETURN2 ='27'
CONS = '28'
PROD = '29'
PPM = '30'
PERCENTAGE = '31'
VISIBILITY ='32'
USAGE = '33'
VALUE = '34'
VOLTAGE = '35'
TEXT = '36'
LEVEL = '37'
DISTANCE = '38'


Domoticz_SensorDict = {
    'Temperature' :     ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + TEMP),
    'Humidity' :        ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=' + HUM + '&svalue=' + HUM_STAT),
    'Barometer' :       ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + BAR + ';' + BAR_FOR),
    'Temp/humidity' :   ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + TEMP + ';' + HUM + ';' + HUM_STAT),
    'Temp/humidity/barometer' : ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + TEMP + ';' + HUM + ';' + HUM_STAT + ';' + BAR + ';' + BAR_FOR),
    'Temp/barometer' :  ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + TEMP + ';' + BAR + ';' + BAR_FOR + ';' + ALTITUDE),
    'Rain' :            ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + RAINRATE + ';' + RAINCOUNTER),
    'Soil Moisture' :   ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=' + MOISTURE),
    'Wind' :            ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + WB +';' + WD + ';' + WS + ';' + WG + ';' + TEMP + ';' + WINDCHILL),
    'UV' :              ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + UV + ';' + TEMPUV),
    'Counter' :         ('/json.htm?type=command&param=udevice&idx=' + IDX + '&svalue=' + COUNTER),
    'Electricity' :     ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + POWER + ';' + ENERGY),
    'Elect Current/Ampere' : ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + Ampere1 + ';=' + Ampere2 + ';=' + Ampere3 + ';'),
    'Electricity P1' :  ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + USAGE1 + ';' + USAGE2 + ';' + RETURN1 + ';' + RETURN2 + ';' + CONS + ';' + PROD),
    'Air quality' :     ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=' + PPM),
    'Pressure' :        ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + BAR),
    'Percentage' :      ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + PERCENTAGE),
    'Visibility' :      ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + VISIBILITY),
    'Gas' :             ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + USAGE),
    'Lux' :             ('/json.htm?type=command&param=udevice&idx=' + IDX + '&svalue=' + VALUE),
    'Voltage' :         ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + VOLTAGE),
    'Text' :            ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + TEXT),
    'Alert' :           ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=' + LEVEL + '&svalue=' + TEXT),
    'Distance' :        ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + DISTANCE),
    'Selector' :        ('/json.htm?type=command&param=switchlight&idx=' + IDX + '&switchcmd=Set%20Level&level=' + LEVEL),
    'Custom' :          ('/json.htm?type=command&param=udevice&idx=' + IDX + '&nvalue=0&svalue=' + VALUE),
    }




# Imput validation Functions

# minmax inputvalue is between these two values and awnsers with True or False
def minmax(min, max, inputval):
    if inputval >= min and inputval <= max:
        return True
    else:
        return False


# Global update script with error handeling
# def Domoticz_UpdateSensor(DOMOTICZ_IP = "127.0.0.1", str(idx), str(value)):
#         print(DOMOTICZ_IP + "/json.htm?type=command&param=udevice&idx=" + idx + "&nvalue=0&svalue=" + str(temp))
#                r = requests.get(DOMOTICZ_IP + "/json.htm?type=command&param=udevice&idx=" + idx_list[loopcounter] + "&nvalue=0&svalue=" + str(temp))
#            siteresponse = r.json()
#                if siteresponse["status"] == 'OK':
#             print('Response = OK')
#            if siteresponse["status"] == 'ERR':
#             # Write to Domoticz log
#             message = "ERROR writing sensor " + id_name[loopcounter]
#             print(message)
#             requests.get(DOMOTICZ_IP + "/json.htm?type=command&param=addlogmessage&message=" + message)


def Domoticz_logwr(message = "ERROR writing sensor "):
    print(message)
    #requests.get(DOMOTICZ_IP + "/json.htm?type=command&param=addlogmessage&message=" + str(message))



# Domoticz JSON 
def Temperature(IDX, TEMP):
    print('/json.htm?type=command&param=udevice&idx=' + str(IDX) + '&nvalue=0&svalue=' + str(TEMP))
    r = requests.get(DOMOTICZ_IP + '/json.htm?type=command&param=udevice&idx=' + str(IDX) + '&nvalue=0&svalue=' + str(TEMP))
    siteresponse = r.json()
    if siteresponse["status"] == 'OK':
        print('Response = OK')
    if siteresponse["status"] == 'ERR':
        # Write to Domoticz log
        Domoticz_logwr("ERROR writing sensor TEMP value " + str(TEMP))

def main():
    for i in Domoticz_SensorDict:
        print(Domoticz_SensorDict[i])
    
    # Test1
    testvar = 50.567
    if minmax(10, 60, testvar) == True:
        print('Waar')
        TEMP = testvar
        Temperature(IDX, TEMP)
    else:
        print('Onwaar')
    # end Test1


TEMP = '99'

main()
