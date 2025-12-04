 - install `paho` pachage to system Python: `sudo apt install python3-paho-mqtt`
 - place `ep20.service` to `/etc/systemd/system`
 - start it by `sudo systemctl start ep20`
 - check possible errors in console
 - make it run on every start `sudo systemctl enable ep20`

