#!/usr/bin/env bash
# Modified by Barborica-Alexandru

POST_SCRIPT=$1

sleep 10

while [ true ]; do
        status="$(pidof moonlight | wc -w)"
        if [ ${status} -ne 1 ]; then
            if [ -z "${POST_SCRIPT}" ]; then
                echo ${POST_SCRIPT}
                ${POST_SCRIPT}
            fi

        /usr/local/bin/moonlight quit
        exit
        else
            sleep 2
        fi
done
