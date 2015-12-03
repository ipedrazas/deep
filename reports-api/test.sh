#!/usr/bin/env bash


export HOST="deep-reports.ipedrazas.k8s.co.uk";

# export HOST="localhost";
export BUILD_ID="3";
http POST $HOST:5000/reports timestamp="$(date +%s)" branch="master" build="$BUILD_ID" repo="drone-kubernetes" report="$(cat reports.xml)"



