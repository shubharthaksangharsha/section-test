#!/bin/bash
dirname=$1 
filename=$2
find . -mtime -1 -path *$FILENAME* -type f >> $dirname/$filename