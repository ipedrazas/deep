#!/usr/bin/env bash


export HOST="localhost"

http POST $HOST:5000/reports timestamp="$(date +%s)" branch="master" build="ts_$BUILD_ID" repo="ipedrazas/deep-reports" report="$(cat reports.xml)"



