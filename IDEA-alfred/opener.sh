#!/bin/sh
 
# check for where the latest version of IDEA is installed
IDEA=`ls -1d /Applications/IntelliJ\ * | tail -n1`
open -a "$IDEA" {query}
