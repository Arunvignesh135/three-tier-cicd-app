#!/bin/bash

pkill -f "python3 app.py" || true
export JENKINS_NODE_COOKIE=dontKillMe
nohup python3 app.py > app.log 2>&1 &
