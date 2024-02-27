#!/bin/bash

cd "/home/ishgharat/drone/apm/ardupilot/build/sitl/bin"

./arducopter -S -I0 --home -35.363261,149.165230,584,353 --model "+" --speedup 1 --defaults /home/ishgharat/drone/apm/ardupilot/Tools/autotest/default_params/copter.parm
