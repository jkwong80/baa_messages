#!/bin/bash

for f in baa_messages/*.thrift; do
  thrift --out baa_messages/thrift_lib --gen py $f;
done
git add baa_messages/thrift_lib/
