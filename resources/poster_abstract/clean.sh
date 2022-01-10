#!/usr/bin/env bash
# source for avoiding extra messages on failed shell command
# https://stackoverflow.com/questions/31318068/shell-script-to-remove-a-file-if-it-already-exist/31318262
rm *.aux > /dev/null 2>&1
rm *.fdb_latexmk > /dev/null 2>&1
rm *.log > /dev/null 2>&1
rm *.lyx~ > /dev/null 2>&1
rm *.synctex.gz > /dev/null 2>&1
rm *.fls > /dev/null 2>&1
