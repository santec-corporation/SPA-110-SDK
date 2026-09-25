## SPA SDK v1.4.1
- Added support for SPA-110 with reduced switches
- New functions
	- `CloseTSLShutter()`
	- `OpenTSLShutter()`

## SPA SDK v1.3.0

- Added support for SPA-110
- New functions
	- `GetTslDeviceList`
	- `StopScan`
	- `GetDistanceRangeTable`
- New Settings
	- `DistanceRange`
- Fixed `GetReflectanceData` recalculating and re-applying offsets when using existing data.

## SPA SDK v1.2.1

- Prevent Gaussian Filter from being repeatedly applied to "old" data.

## SPA SDK v1.2.0

- Added SaveDSPA to save data to a DSPA file.

## SPA SDK v1.1.1
- Updated to work with `FFTSG` library.