#!/bin/bash
#Parse all pcaps recursively only if they are a valid tcpdump capture
find /data/pcap -exec file {} \; | grep "capture" | awk -F: '{print $1}' | xargs -I % /data/moloch/bin/moloch-capture -r %
