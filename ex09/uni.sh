#!/bin/bash

PNAME=$(basename $1) && echo $PNAME
if pidof -o %PPID -x "$PNAME">/dev/null; then
    echo "Process[$(basename $1)] already running"
        exit 1
else
    $* &
fi

