#!/usr/bin/env bash



for (( i = 0; i < 30; i++ )); do
    TS=$(date +%s)
    BUILD_ID = "$(date +%s)";
    http POST localhost:5000/deploys Timestamp:=$TS Images:='["ipedrazas/botd"]' tag="ts_$BUILD_ID" Namespace="default" Target="https://54.246.156.77" Source="drone.ipedrazas.co.uk"

done


#http POST deep-api.ipedrazas.k8s.co.uk:5000/webhooks < webhooks.json

