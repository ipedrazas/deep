#!/usr/bin/env bash

http POST localhost:5000/deploys created="$(date +%s)" image="ipedrazas/botd" tag="ts_$BUILD_ID" namespace="default" apiserver="https://54.246.156.77" soource="drone.ipedrazas.co.uk"
