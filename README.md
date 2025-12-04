# MustPower EP20 inverter monitor

Must Power EP 20 series monitor utility. It may also work with newest EP 21 series, as well as EP30 and any other MustPower UPS/inverters which _not_ use RS485.

### License

[MIT License](./LICENSE)
Copyright (c) 2025 Andrey E. Yaromenok



### Status

So far so good - it's working perfect with Home Assistant. Exist some issues with responce from UPS - like 1/5 query finihsed without responce - but it's ok for me (just use previous values). In the time of this update PY code working about 5 days correctly. Nore testing will come

### Other names

 - Official name looks like `MUST EP20 - 1012 PRO` (for 1000W version. 600W looks like `MUST EP20 - 0612 PRO` ).
 - Other name can be `MUST EP20 - 1000 PRO` (for 1000W version. 600W looks like `MUST EP20 - 600 PRO` ).
 - Windows Application `Solar/Power Monitor` can display different names like `Ep 2000 Pro`, `PV 2000 PK` depenfing on the version off application. 
 - It also can apper under other brand names, like `SYNAPSE` in South Africa.

### Idntification

Inverter use serial converter CH340, so appear in `lsusb` output as follow:

```Bus 001 Device 006: ID 1a86:7523 QinHeng Electronics CH340 serial converter```

### RaspberryPi issues

- Error: device reports readiness to read but returned no data (device disconnected or multiple access on port?)
 
`sudo systemctl mask serial-getty@ttyUSB0.service` and/or `sudo nano /boot/firmware/cmdline.txt`. remove `console=serial0,115200`

### Run as sevice

 - [Service file provided](./src/py/ep220.service)
 - [Ho to documentation](./doc/run_as_service.md)

## Protocol description

 - [detaild descrition](./doc/protocol.md)

