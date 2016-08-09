#!/bin/bash

for f in baa_messages/schema/*.thrift; do
  thrift --out baa_messages/ --gen py $f;
  thrift -r --gen gv --out docs/ $f;
done
pushd docs/
for f in *.gv; do
  arrIN=(${f//./ })
  dot -Tpdf -o"$arrIN.pdf" $f
done
popd

git add baa_messages/
git add docs/
