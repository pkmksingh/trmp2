#!/bin/bash
# service.sh

nohup python stream_manager.py > stream.log 2>&1 &
echo "Relay started in background."
