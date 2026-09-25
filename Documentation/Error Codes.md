## Error Codes

### Settings Error Codes

#### `SetOperationSettings()` or `LoadOperationSettingsINI()`

Get a list of encountered error codes using GetSettingsErrors

-10 = StartWave not in limits
-11 = StopWave not in limits
-12 = StartWave >= StopWave
-13 = StartWave or StopWave in water absorption region
-14 = Measurement Mode not valid (valid 0 - 3)
-15 = Refractive Index not valid (valid > 1)
-16 = Power not valid (valid -3 to 10)
-17 = StartWave or StopWave <= 0

### Connection Error Codes

#### `LoadConnectionSettingsFromFile()`

-1 = File does not exist
-2 = Invalid file format
-3 = Unable to parse file
-4 = Invalid TSL Type
-5 = Invalid GPIB Address
-6 = Invalid USB Device ID

### Instrument Error Codes

#### `SetScanSettings()` and `StartScan()`

-1 = Unable to read information from device
-10 = Unable to read information from device
-14 = Unable to read information from device
-40 = Unable to start measurement (check TSL is not dark)
-200 = TSL is currently not in a sweepable state
-222 = Out of settable range
int.MinValue = Unexpected exception

#### `GetSamplingData()`

-1 = Sample count = 0
-2 = High-frequency triggering error
