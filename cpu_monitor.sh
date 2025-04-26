#!/bin/bash
while true; do
  top -bn1 | grep "Cpu(s)" | awk '{print "⚙️ CPU Load: " $2 "%"}'
  sleep 1
done
