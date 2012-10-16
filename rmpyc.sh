#!/bin/bash - 
#===============================================================================
#
#          FILE:  rmpyc.sh
#
#         USAGE:  ./rmpyc.sh
#
#   DESCRIPTION: Remove all *.pyc and *pyo files
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR: GrandMaster
#       COMPANY: AbstolHeromBey
#       CREATED: 22.09.2011 11:25:20 UTC
#      REVISION: 0.1
#===============================================================================

cd `dirname $0`
for i in `find . -name "*.py[co]"`
do
    rm -rfv ${i}
done

