/dev/ttyUSB0, 9600

str0: "0A 03 75 30 00 1B 1E B9" // size 59
str1: "0A 03 79 18 00 0A 5D ED" // size 25

### response:

#### str0:

|| Data || Name || type||
|----|----|----|
| int8? | MachineType | | 
| int16 | SoftwareVersion | |
| int16 | WorkState | |
| int16 | BatClass | V |
| int16 | RatedPower| |
| int16*0.1 | GridVoltage | V |
| int16*0.1 | GridFrequency | Hz |
| int16*0.1 | OutputVoltage | V |
| int16*0.1 | OutputFrequency | V |
| int16*0.1 | LoadCurrent | A |
