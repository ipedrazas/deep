#!/usr/bin/env bash


export HOST="deep-reports.ipedrazas.k8s.co.uk";

# export HOST="localhost";
export BUILD_ID="$(date +%s)";
http POST $HOST:5000/reports timestamp="$(date +%s)" branch="master" build="ts_$BUILD_ID" repo="ipedrazas/deep-reports" report="$(cat reports.xml)"



