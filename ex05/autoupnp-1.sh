#!/bin/bash
# 2022/05/13 by CreaterName

uip=$(hostname -I | cut -d " " -f1) && echo "IP:" $uip
uip3d="000" && echo "prefix:" $uip3d

# for SSH
uport="22"$uip3d && echo $uport
upnpc -d $uport TCP  || true
upnpc -a  $uip  22  $uport TCP || true
# for WEB
uport="28"$uip3d && echo $uport
upnpc -d $uport TCP  || true
upnpc -a  $uip  80  $uport TCP || true
# for VNC
uport="29"$uip3d && echo $uport
upnpc -d $uport TCP  || true
upnpc -a  $uip  5900  $uport TCP || true

