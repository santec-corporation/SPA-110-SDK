# Valid Settings and Connection Parameters

## Settings INI

### Start Wavelength

```text
LimitMinWave <= StartWave <= LimitMaxWave
```

- Floor `StartWave` to `LimitMinWave`.

### Stop Wavelength

```text
LimitMinWave <= StopWave <= LimitMaxWave
```

- Ceiling `StopWave` to `LimitMaxWave`.

### Start/Stop Wavelength Relationship

```text
StartWave >= StopWave
```

- If not valid, set `StartWave` and `StopWave` to `LimitMinWave` and `LimitMaxWave`, respectively.

### Water Absorption Wavelengths

```text
1350 <= StartWave <= 1420
1350 <= StopWave <= 1420
```

- Water Absorption Wavelengths.
- If not valid, set to `LimitMinWave` and `LimitMaxWave`.

### Measurement Mode

`MeasurementMode` supports the following values:

| Value | Description |
|---:|---|
| `0` | Port 1 |
| `1` | Port 2 |
| `3` | Port 1+2 (if supported) |
| `4` | IL (Transmission) |

### Default Refractive Index

```text
DefaultRefractiveIndexValue >= 1
```

- If not valid, set to `1`.

### Average Count

```text
AverageCount >= 1
```

- If not valid, set to `1`.

### Power

```text
-3 <= Power <= 10
```

- If not valid, set to `-3`.

### Gain

`Gain` supports the following values:

| Value | Description |
|---:|---|
| `0` | Auto |
| `1` | 0 dB |
| `2` | 4 dB |
| `3` | 9 dB |
| `4` | 13 dB |

### Distance Range

```text
DistanceRange: 5.0, 14.0, 30.0
```

This is based on the Distance Range Table from `GetDistanceRangeFunction`.

---

## Connection INI

### TSL Communication

Supported communication methods:

- `USB`
- `GPIB`
- `LAN`

If `TSL Communication = GPIB`:

```text
GPIBAddress = 0 - 30
```

If `TSL Communication = USB`:

```text
USBDeviceID > 0
```

If `TSL Communication = LAN`:

```text
IP and Port must be valid
```

### SPA Device ID

SPA Device ID must be of the form:

```text
Dev#
```

where `# > 1`.

### WDL Resolution

`WDLResolution` supports values from `0` to `10`:

| Value | Resolution |
|---:|---|
| `0` | `w2500fm` |
| `1` | `w5pm` |
| `2` | `w10pm` |
| `3` | `w20pm` |
| `4` | `w40pm` |
| `5` | `w80pm` |
| `6` | `w160pm` |
| `7` | `w320pm` |
| `8` | `w640pm` |
| `9` | `w1281pm` |
| `10` | `w2564pm` |
