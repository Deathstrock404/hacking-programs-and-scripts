#!/bin/bash

if [ "$1" == "" ]
then
echo "You forgot to give an ipv4 address! "
echo "Syntex for this script is ./ipsweep 192.168.1"

else
for ip in `seq 1 254`; do 
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"
done
fi
 
