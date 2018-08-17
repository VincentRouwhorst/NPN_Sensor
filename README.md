# NPN_Sensor
Domoticz update script for NPN sensor

https://www.domoticz.com/forum/viewtopic.php?t=17123

===================================
Sensor aansluiten
===================================
Sensor met een beugeltje aan de watermeter bevestigen en aansluiten op de raspberry pi:
Blauw = GND (b.v. pin 39)
Bruin = 5V (b.v. pin 2 of 4)
Zwart = GPIO (b.v. GPIO 21 / Pin 40)
Het is een 6-36 volt sensor maar werkt bij mij perfect op 5v van de raspberry.


=================================
Domoticz Teller aanmaken
=================================
Ik heb niet kunnen vinden hoe je dit via Domoticz web kan doen. Het lukte mij alleen om via json de RFXmeter aan te maken.
1 = maak sensor
2 = lees IDX
3 = maak RFXMeter aan met juiste IDX
Gebruik je eigen IP en poort nummer.
Let op dat je in domoticz settings, de deler van water op 1000 zet => RFXMeter/Meter delers water: 1000