#!/bin/bash
# Copyright (C) VPNCloud 2015
export PATH="/bin:/sbin:/usr/sbin:/usr/bin"

function welcome() {
  echo "VPN Speed Up From VPNCloud."
  echo "[Warning] Please disconnect VPN before install!"
  echo ""
  read -n1 -r -p "Then press any key to continue..." nothing
}

function success_message() {
  echo ""
  echo "Install successfully."
  echo "Connect VPN to try the speed up!"
}

function failed_message() {
  echo ""
  echo "Install failed"
  echo "Try to reinstall or report a ticket!"
}

function fedora_install() {
  cp $SCRIPTDIR/data/ip-pre-up /etc/NetworkManager/dispatcher.d/pre-up.d/ip-pre-up
  chmod +x /etc/NetworkManager/dispatcher.d/pre-up.d/ip-pre-up

  cp $SCRIPTDIR/data/ip-up /etc/ppp/ip-up.local
  chmod +x /etc/ppp/ip-up.local

  cp $SCRIPTDIR/data/ip-down /etc/ppp/ip-down.local
  chmod +x /etc/ppp/ip-down.local
}

function ubuntu_install() {
  cp $SCRIPTDIR/data/ip-pre-up /etc/ppp/ip-pre-up
  chmod +x /etc/ppp/ip-pre-up

  cp $SCRIPTDIR/data/ip-up /etc/ppp/ip-up.d/ip-up
  chmod +x /etc/ppp/ip-up.d/ip-up

  cp $SCRIPTDIR/data/ip-down /etc/ppp/ip-down.d/ip-down
  chmod +x /etc/ppp/ip-down.d/ip-down
}

welcome

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
if [ -f '/etc/redhat-release' ]; then
  SYSTEM=`cat /etc/redhat-release`
else
  SYSTEM="UBUNTU"
fi

SYSTEM=`echo $SYSTEM | tr '[A-Z]' '[a-z]'`

if [[ "$SYSTEM" =~ "fedora" ]]; then
  fedora_install
  success_message
elif [[ "$SYSTEM" =~ "ubuntu" ]]; then
  ubuntu_install
  success_message
else
  failed_message
  exit 0;
fi
