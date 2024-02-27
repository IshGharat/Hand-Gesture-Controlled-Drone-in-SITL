#!/bin/bash

gnome-terminal -- bash -c "./RunSITL.sh'"

# sleep 1

gnome-terminal -- bash -c "echo 'hello'; exec bash"

gnome-terminal -- bash -c "./RunMavProxy.sh"

# gnome-terminal -- bash -c "QGC.AppImage"

