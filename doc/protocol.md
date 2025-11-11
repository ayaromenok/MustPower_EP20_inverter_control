### Device

| Device | speed |
|--------|-------|
|/dev/ttyUSB0 | 9600 |


### Query
| Name      | Data        | Response Size |
|:----------|:------------|:----:|
|(HandShake?)    | "0A 03 79 18 00 07 9C 28" | - |
|str0            | "0A 03 75 30 00 1B 1E B9" | 59 |
|str1            | "0A 03 79 18 00 0A 5D ED" | 25 |
|(factory) reset | "0A 10 7D 00 00 01 02 00 01 B9 A7" | |
|(remote) reset  | "0A 10 7D 01 00 01 02 00 01 B8 76"| |
|remote shotdown | "0A 10 7D 02 00 01 02 00 01 B8 45" | |
| (DoWork?)      | "0A 03 79 18 00 07 9C 28" | |
| SaveSettings   | "01 10 79 18 00 0A 14" | |


### Response:

#### str0:

| Data      | Name        | Type |
|:----------|:------------|:----:|
| int8?     | MachineType | | 
| int16     | SoftwareVersion | |
| int16     | WorkState | |
| int16     | BatClass | V |
| int16     | RatedPower| |
| int16*0.1 | GridVoltage | V |
| int16*0.1 | GridFrequency | Hz |
| int16*0.1 | OutputVoltage | V |
| int16*0.1 | OutputFrequency | V |
| int16*0.1 | LoadCurrent | A |
| int16     | LoadPower | W |
| int16     | LoadPercent| % |
| int16     | LoadState | |
| int16*0.1 | BatteryVoltage | V |
| int16*0.1 | BatteryCurrent  | A |
| int16     | BatterySoc | |
| int16     | TransformerTem | C |
| int16     | AvrState | |
| int16     | BuzzerState | |
| int16     | Fault | |
| int16     | Alarm | |
| int16     | ChargeState | |
| int16     | ChargeFlag | |
| int16     | MainSw| |
| int16     | DelayType| |

#### str1:
| Data      | Name        | Type |
|-----------|-------------|------|
| int16     | | |
