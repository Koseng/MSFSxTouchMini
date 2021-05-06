# MSFSxTouchMini
Installation and Configuration of Behringer X-Touch Mini for Microsoft Flight Simulator. Including configuration for the FlyByWire A320 and 3D printable labels.

## Overview
![Picture Overview](Pics/overview.png)

Needed Software:
* [X-Touch-Mini-FS2020](https://github.com/maartentamboer/X-Touch-Mini-FS2020): 
  * Needs to run while the flighsim is running. This software is the communication bridge between the X-Touch Mini and the flighsim. It converts the midi signals to the flightsim simconnect interface.
* [Mobiflight Addon](https://www.mobiflight.com):
  * Mobiflight installs an addon to the community folder. This exposes special variables to the simconnect interface and makes them accessible for other external software like the X-Touch-Mini-FS2020.
* [Behringer X-Touch Editor](https://www.behringer.com/product.html?modelCode=P0B3M):
  * That is needed to make a configuration change to the dial knobs.

## [Installation and setup](installation/README.md)


## Configuration of buttons and knobs

Configuration is done via the files in X-Touch-Mini-FS2020\Configurations

## Usage

After the start of MSFS2020 start X-Touch_mini-FS2020.exe. The button and knobs layout changes automatically for different planes according to the configuration.

### Default configuration of X-Touch-Mini-FS2020:

**Knobs**
* Knob1 - Heading bug | Press - Set heading bug to current heading.
* Knob2 - Baro | Press - Set to standard baro.
* Knob3 - Alt bug 
* Knob4 - VS bug
* Knob5 - COM | Press - Alternate to decimal places | Long press - swap frequencies
* Knob6 - NAV1 | Press - Alternate to decimal places | Long press - swap frequencies

**ROW 1**
* Button1 - Flight Director
* Button2 - HDG
* Button3 - ALT
* Button4 - VS
* Button5 - APR
* Button6 
* Button7
* Button8 - Decrease Flaps

**ROW 2**
* Button9 - AP
* Button10 - NAV
* Button11
* Button12 - AP flight level change
* Button13 - YD
* Button14 - Master Battery
* Button15 - Gear
* Button16 - Increase Flaps
