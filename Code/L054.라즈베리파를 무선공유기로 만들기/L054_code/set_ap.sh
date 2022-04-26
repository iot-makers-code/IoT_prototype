#!/bin/bash
# AnHive, 2017.01

cd ~pi/ap

[ "$#" -lt "1" ] && echo "usage $0 enable\|disagle" \
                && exit 0

if [ "$1" == "enable" ]
then
    sudo sed -i 's/#denyinterfaces/denyinterfaces/g' \
                /etc/dhcpcd.conf
    [ -e disable_ap ] && mv disable_ap enable_ap
    sudo sed -i 's/wlan0/wlanX/g' \
                /etc/network/interfaces
elif [ "$1" == "disable" ]
then
    sudo sed -i 's/denyinterfaces/#denyinterfaces/g' \
                /etc/dhcpcd.conf
    [ -e enable_ap ] && mv enable_ap disable_ap
    sudo sed -i 's/wlanX/wlan0/g' \
                /etc/network/interfaces
else
  echo "not defined option $1."
fi