#!/bin/bash

mkdir -p tei

for f in papers/*.pdf; do
  echo "Processing $f"
  curl --max-time 3000 --fail -v \
       --form input=@"$f" \
       --form consolidateHeader=1 \
       --form consolidateCitations=1 \
       http://localhost:8070/api/processFulltextDocument \
       -o tei/"$(basename "$f" .pdf)".xml
done

