#!/usr/bin/env bash



for (( i = 0; i < 30; i++ )); do
    TS=$(date +%s)
    BUILD_ID = "$(date +%s)";
    http POST localhost:5000/deploys Timestamp:=$TS Images:='["ipedrazas/botd"]' tag="ts_$BUILD_ID" Namespace="default" Target="https://54.246.156.77" Source="drone.ipedrazas.co.uk"

done


#http POST deep-api.ipedrazas.k8s.co.uk:5000/webhooks < webhooks.json

http POST localhost:5000/components < components.json


export APIHOST=deep-api.ipedrazas.k8s.co.uk:5000
http POST $APIHOST/components < components.json


TS=$(date +%s)
REPORT=$(cat reports.xml)
curl -i \
    -H "Content-Type: application/json" \
    -X POST -d '{build":"30", "branch":"Tip 3", "repo":"Target 3", "report":"$REPORT", "timestamp": "$TS"}' \
    http://deep-api.ipedrazas.k8s.co.uk:5000/reports
