This will prevent an APC UPS battery backup system that has an Emergency
Power Off (EPO) port from discharging below a set threshold.
It leverages a Raspberry Pi to 1) monitor the Battery Charge of the UPS
and 2) trigger a relay to close via signal to GPIO pin.
Assumes apcupsd has already been setup and that you're ok with completely
powering down at set threshold.  This preserves life span of lead acid
batteries by limiting the DoD (Depth of Discharge)
