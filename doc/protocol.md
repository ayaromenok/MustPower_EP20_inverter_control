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

| # | Data      | Org Nam     | Type | Short name|
|--:|:----------|:------------|:----:|:--|
| | int8?     | MachineType | | mt|
| | int16     | SoftwareVersion | | swv|
|4| int16     | WorkState |4 - from grid, 3 - on battery | ws|
|5| int16     | BatClass | V | bcl |
|6| int16     | RatedPower|W | rp|
|7| int16*0.1 | GridVoltage | V | gv |
|8| int16*0.1 | GridFrequency | Hz | gf|
|9| int16*0.1 | OutputVoltage | V | ov |
|10| int16*0.1 | OutputFrequency | V |of|
|11| int16     | LoadCurrent | A |lc|
|12| int16     | LoadPower | W |lp|
|13| int16     | ? | | nnm0|
|14| int16     | LoadPercent| % | lpc|
|15| int16     | LoadState | | ls |
|16| int16*0.1 | BatteryVoltage | V | bv |
|17| int16*0.1 | BatteryCurrent  | A | bc |
|18| int16     | BatterySOC |% | bsoc |
|19| int16     | TransformerTemp | C | tt |
|20| int16     | AvrState | | as |
|21| int16     | BuzzerState | | bs|
|22| int16     | Fault | | flt |
|23| int16     | Alarm | | alrm|
|24| int16     | ChargeState | | cs |
|25| int16     | ChargeFlag | | cf|
|26| int16     | MainSw| | msw
|27| int16     | DelayType| | dt |

#### str1:
| Data      | Name        | Type |
|-----------|-------------|------|
| int16     | | |
