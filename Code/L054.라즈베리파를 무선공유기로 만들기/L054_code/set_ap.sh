#!/bin/bash
cd ~pi/ap
[ "$#" -lt "1" ] && \
    echo "usage $0 enable \|disable" && exit 0

DENY=denyinterfaces
CONF=/etc/dhcpcd.conf
[ "$(grep $DENY /etc/dhcpcd.conf | wc -l)" == 0 ] \
    && echo "#$DENY wlan0" | sudo tee -a $CONF
if [ "$1" == "enable" ]
then
    [ -e disable_ap ] && mv disable_ap enable_ap
    [ ! -e enable_ap ] && touch enable_ap
    sudo sed -i "s/#$DENY/$DENY/g" $CONF
elif [ "$1" == "disable" ]
then
    [ -e enable_ap ] && mv enable_ap disable_ap
    [ ! -e disable_ap ] && touch disable_ap
    sudo sed -i "s/$DENY/#$DENY/g" $CONF
else
  echo "not defined option $1."
fi
