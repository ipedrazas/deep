#!/usr/bin/env bash


# export HOST="deep-reports.ipedrazas.k8s.co.uk";

export HOST="localhost";
export BUILD_ID="21";
export COMMIT="e077cc31995f9c609dd3de59e1c35651cf384d7d"
export REPO="deep"

http POST $HOST:5000/reports  branch="master" build="$BUILD_ID" repo="$REPO" commit="$COMMIT" report="$(echo $(cat reports.xml))"
