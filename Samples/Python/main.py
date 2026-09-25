"""
SPA DLL
python code examples

Last updated: Feb 21, 2025 | 16:00:00 JST

@organization: Santec Holdings Corp.
"""

"""
--------------------------------------------------------------------
Initialization and Settings
--------------------------------------------------------------------
"""

# Basic imports (or dependencies)
import clr
import sys

# Checking and Accessing the DLL (SantecSPA) [make sure the DLL folder is in the same directory as the script]
dll_path = r"..\sdk"
sys.path.append(dll_path)
clr.AddReference(r"SantecSPA")

# Importing the main method from the DLL
import SantecSPA

# Creating an object for the SPAModule class
spa = SantecSPA.SPAModule()

# Initialize and connect to instruments using a connection file
spa.Initialize("connection.ini")

# Initialize and connect to instruments using TSL GPIB on address = 1 and SPA as Dev1
spa.Initialize("Dev1", "GPIB", 1, 0, "", 0)

# Initialize and connect to instruments using TSL USB device 5 and SPA as Dev1
spa.Initialize("Dev1", "USB", 0, 5, "", 0)

# load DSPA file
spa.LoadDSPAFile("SPAData.dspa")

# load SPA Settings from file
spa.LoadOperationSettingsFromFile("Settings.ini")

# Change individual settings
spa.SetOperationSettingsValue("StartWave", 1500)
spa.SetOperationSettingsValue("StopWave", 1600)
spa.SetOperationSettingsValue("GaussianFilter", True)
spa.SetOperationSettingsValue("GaussianRadius", 0.2)
spa.SetOperationSettingsValue("ILWidth", 0.1)

# Save changes to settings file
settings = spa.Settings
settings.SaveOperationSettingsIni("settings.ini")


"""
--------------------------------------------------------------------
Reference Reflectance (Reflection Mode) 
--------------------------------------------------------------------
"""

# Creating an object for the SPAModule class
spa = SantecSPA.SPAModule()

# Initialize and connect using connection file
spa.Initialize("Connection.ini")

# ...

# Perform a reflection reference scan using the base functions

# Set to Reflection Mode Port 1
spa.SetOperationSettingsValue("MeasurementMode", 1)

# Set wavelength range
spa.SetOperationSettingsValue("StartWave", 1500)
spa.SetOperationSettingsValue("StopWave", 1600)

# Perform the scan as reference
spa.Scan(True)  # reference = true

# Process and get the reference
status, reference = spa.GetReflectanceReferenceOffset()
print(status, reference)

# ...

# Perform a reflection reference scan using the top level function
# Load settings from file instead of setting individually

# Load settings from file
spa.LoadOperationSettingsFromFile("settings.ini")
status, reference = spa.ExecuteReflectionReference()  # this will perform the scan and the processing
print(status, reference)


"""
--------------------------------------------------------------------
Measure Reflectance (Reflection Mode) 
--------------------------------------------------------------------
"""

# Perform a measurement after referencing using the base functions

# Perform the scan as measurement
spa.Scan()  # reference = false by default

# Process and get the spatial reflectance data x and y values
status, xValues, yValues = spa.GetReflectanceData()
print(status)

# To print x and y values
for x in xValues:
    print(float(x))

for y in yValues:
    print(float(y))

# ...

# Perform the measurement after referencing using the top level function
status, xValues, yValues = spa.ExecuteReflectionMeasurement()
print(status)


"""
--------------------------------------------------------------------
Finding Peaks
--------------------------------------------------------------------
"""

# Instruments initialized in Reflection Mode and reference scan was performed previously

# Set peak finding parameters
spa.SetOperationSettingsValue("PeakThreshold", -60)
spa.SetOperationSettingsValue("PeakWidth", 1.0)


# Find peaks from front-panel (0 mm) to 4000 mm
# Using base functions

spa.Scan()

status, xValues, yValues = spa.GetReflectanceData()
print(status)

status, peakList, peakValList, peakCount = spa.GetPeaks(0, 4000, [], [])

# ...

# Find the last 3 peaks between 0 mm and 3000 mm
# Using top level functions

# Perform the scan, process the data, then find the peaks
status, peakPositionList, peakValuesList = spa.ExecutePeakScan(0, 3000, 1, 3, [], [])

# ...

# Scan and set the last peak found between 0 mm and 3000 mm as the zero position
status, refPosition = spa.ExecutePositionReference(0, 3000, 1)

# Scan and find the first 5 peaks from the reference position to 4000 mm
status, peakPositionList, peakValuesList = spa.ExecutePeakScan(refPosition, 4000, 0, 5, [], [])

# Using the last scan (no re-scanning), get the last peak from reference position to 6000 mm
# then get the relative distance of that peak from the reference position
status, peakDistanceList, peakValuesList = spa.MeasurePeakDistance(refPosition, 0, 6000, 1, 1, [], [])

# Use an arbitrary position (1000 mm) as the zero position instead of finding a peak
# Get the distance to the first 5 peaks from the zero position
status, peakDistanceList, peakValuesList = spa.MeasurePeakDistance(0, 1000, 6000, 0, 5, [], [])  # this will give distances relative to 1000 mm


"""
--------------------------------------------------------------------
Advanced Peaks
--------------------------------------------------------------------
"""

# Find peaks across multiple regions with different peak thresholds
# Limit to 10 peaks per region

# Instruments initialized in Reflection Mode and reference scan was performed previously

# Set peak parameters for first region
spa.SetOperationSettingsValue("PeakThreshold", -60)
spa.SetOperationSettingsValue("PeakWidth", 1.0)

# Scan then find first 10 peaks in the region 0 - 1000 mm
status, peakPositionList, peakValuesList = spa.ExecutePeakScan(0, 1000, 0, 10, [], [])

# Set peak parameters for second region
spa.SetOperationSettingsValue("PeakThreshold", -40)
spa.SetOperationSettingsValue("PeakWidth", 1.0)

# Use the previous scan and find the first 10 peaks in the region 1000 - 1500 mm
status, peakDistanceList, peakValuesList = spa.MeasurePeakDistance(0, 1000, 1500, 0, 10, [], [])

# Set peak parameters for third region
spa.SetOperationSettingsValue("PeakThreshold", -70)
spa.SetOperationSettingsValue("PeakWidth", 1.0)

# Use the previous scan and find the first 10 peaks in the region 1500 - 2000 mm
status, peakDistanceList, peakValuesList = spa.MeasurePeakDistance(0, 1500, 2000, 0, 10, [], [])


"""
--------------------------------------------------------------------
Measure RL and IL
--------------------------------------------------------------------
"""

# Instruments initialized and reference scan was performed previously

# measurement scan
spa.Scan()

# process measurement
status, reflDataX, reflDataY = spa.GetReflectanceData([], [], False)

# measure RL between 1000 mm and 1100 mm position
status, rlValue = spa.MeasureRL(1000, 1100)

# measure IL between 1000 mm and 1100 mm positions using 0.1 mm averaging width
spa.SetOperationSettingsValue("ILWidth", 0.1)
status, ilValue = spa.MeasureIL(1000, 1100)


"""
--------------------------------------------------------------------
Measure RL and IL for Peaks Found
--------------------------------------------------------------------
"""

# Instrument initialized and reference scan was performed previously

# Set peak finding parameters
spa.SetOperationSettingsValue("PeakThreshold", -60)
spa.SetOperationSettingsValue("PeakWidth", 1.0)

# Set IL averaging width
spa.SetOperationSettingsValue("ILWidth", 0.1)

# Reference to the end of a fiber(length=1000m)
status, refPosition = spa.ExecutePositionReference(0, 1000, 1)

# Setup DUT then find first 6 peaks from refPosition to 4000 mm
status, peakPositionList, peakValuesList = spa.ExecutePeakScan(refPosition, 4000, 0, 6, [], [])

# Iterate through the peakList and calculate RL and IL for each peak
# Measure IL and RL across a 0.2 mm region centered at the peak
# Save in a table with distance from refPosition to peak
# Note: this uses the IL measurement parameters in the settings

rlTable = []
ilTable = []

for value in peakValuesList:
    spa.MeasureRL(value - 0.1, value + 0.1, rlValue)
    spa.MeasureIL(value - 0.1, value + 0.1, ilValue)

    rlTable.append((value - refPosition, rlValue))
    ilTable.append((value - refPosition, ilValue))
