#!/bin/bash
pversion=$(cat /root/mcscript/AutoUpdate/server.com)
wget -q https://api.mcsrvstat.us/2/server.com -O /root/mcscript/AutoUpdate/server.com
sversion=$( jq .version /root/mcscript/AutoUpdate/server.com )
if [ $sversion = null ]; then
 echo ${pversion} > /root/mcscript/AutoUpdate/server.com
 echo "Server is down"
else
 echo ${sversion} > /root/mcscript/AutoUpdate/server.com
fi
