#!/bin/bash

noext=`basename "$1" .py`
dir=`dirname "$1"`
full_out=`readlink -f "$2"`
outf=${dir}/${noext}_mem_profiled.py
sed -e 's/\(^.*\)\(def .*\)$/\1@profile\n\1\2/g' "$1" > "$outf"
pushd "$dir"
python "$outf" > "$full_out"
popd
python parse_logs.py "$full_out"