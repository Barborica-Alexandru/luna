#!/bin/sh
# Originally written by miko
# Modified by dodslaser
# Modified again by wackerl91 (support for launch args)
# Modified again by Barborica-Alexandru

LAUNCHER_PATH=$1
HEARTBEAT_PATH=$2
HOST=$3
KEY_DIR=$4
GAME=$5
CONF_PATH=$6
DEBUG_ENABLED=$7
PRE_SCRIPT=$8
POST_SCRIPT=$9

if [ -z "{PRE_SCRIPT}" ]; then
    ${PRE_SCRIPT} \"${HOST}\" \"${GAME}\"
fi

sh $HEARTBEAT_PATH \"${POST_SCRIPT}\" &&

echo ${CONF_PATH}
bash $LAUNCHER_PATH ${HOST} "${GAME}" "${CONF_PATH}"

sleep 2

#sudo su -c "killall moonlight &" &

exit
