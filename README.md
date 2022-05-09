# Fetch data from the Raspberry Pi Weather Station database and plot that data on a graphical map

# Project Description

One thousand weather stations were sent out to school all over the world at the beginning of 2016, ready to be assembled and begin collecting global weather data.

The weather stations continually monitor the environment and send their data to an Oracle database, where it is stored and from which it can be accessed.

In this project we are going to fetch a list of online weather stations with their data, and then plot them onto a map of the world.

We can then look at gathering data from all the available weather stations and plotting that weather data to the map.

# Schematics

Insert the SD card with the previous installed OS

Connect the mouse and the keyboard through dedicated USB ports

Connect the Monitor, with the help of the HDMI cable, to the Board

Plug in the Power supply

Note: no other cables or special equipment is required for this project

# Pre-requisites

Hardware:

    - Raspberry Pi 3B+ Board - https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/
    - SD card
    - Power supply
    - Mouse
    - Keyboard
    - Monitor
    - HDMI cable

Software:

    - Raspberry Pi OS (Raspbian) - https://www.raspberrypi.com/software/
    - Python 3 - https://www.python.org/downloads/

# Setup and Build

1. SD card setup

Install Raspberry Pi Imager - link: https://www.raspberrypi.com/software/ (More details at https://www.youtube.com/watch?v=ntaXWS8Lk34)

With the help of Raspberry Pi Imager, install Raspberry Pi OS to a microSD card

2. Put all the hardware together

Insert the SD card with the previous installed OS

Connect the mouse and the keyboard through dedicated USB ports

Connect the Monitor, with the help of the HDMI cable, to the Board

Plug in the Power supply

3. Finally, install Python 3 to your Raspberry Pi

# Running

1. Copy the project (main.py) to Raspberry Pi and run it
2. A .html file will be created (worldMap.html) and opened
3. World map with all the weather stations will be shown
4. User can:

    - Zoom in/out and pan the map to different zones
    - Select different stations in order to see more details (name of the station, temperature)
