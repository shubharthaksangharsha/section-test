#!/bin/bash
find . -mtime -1 -path *$FILENAME* -type f >> list.txt 