#!/usr/bin/env bash

http POST deep-api.ipedrazas.k8s.co.uk:5000/deploys created="$(date +%s)" image="ipedrazas/botd" tag="ts_$BUILD_ID" namespace="default" target="https://54.246.156.77" source="drone.ipedrazas.co.uk"


http POST deep-api.ipedrazas.k8s.co.uk:5000/webhooks < webhooks.json


