## Valid values for Settings INI

**LimitMinWave <= StartWave <= LimitMaxWave**
- Floor StartWave to LimitMinWave

**LimitMinWave <= StopWave <= LimitMaxWave**
- Ceiling StopWave to LimitMaxWave

**StartWave >= StopWave**
- If not valid, set StartWave and StopWave to LimitMinWave and LimitMaxWave resp.

**1350 <= StartWave <= 1420, 1350 <= StopWave <= 1420**
- Water Absorption Wavelengths
- If not valid, set to LimitMinWave and LimitMaxWave

**MeasurementMode: 0, 1, 2, 3** <br>
0 = Port 1, 1 = Port 2, 3 = Port 1+2 (if supported), 4 = IL (Transmission)

**DefaultRefractiveIndexValue >= 1**
- If not valid, set to 1

**AverageCount >= 1**
- If not valid, set to 1

**-3 <= Power <= 10**
- If not valid, set to -3

**Gain: 0, 1, 2, 3, 4** <br>
0 = auto, 1 = 0 dB, 2 = 4 dB, 3 = 9 dB, 4 = 13 dB

**DistanceRange: 5.0, 14.0, 30.0** <br>
This is based on the Distance Range Table from `GetDistanceRangeFunction`.

<br>

## Valid values for Connection INI

**TSL Communication: `USB`, `GPIB`, `LAN`**

If _TSL Communication = GPIB_, <br>
   GPIBAddress = 0 - 30 <br>  

If _TSL Communication = USB_, <br>
   USBDeviceID > 0 <br>  

If _TSL Communication = LAN_, <br>
   IP and Port must be valid 

SPA Device ID must be of form `Dev#`, where # is > 1.

**WDLResolution: 0 - 10** <br>

0 = w2500fm, <br>
1 = w5pm, <br>
2 = w10pm, <br>
3 = w20pm, <br>
4 = w40pm, <br>
5 = w80pm, <br>
6 = w160pm, <br>
7 = w320pm, <br>
8 = w640pm, <br>
9 = w1281pm, <br>
10 = w2564pm
