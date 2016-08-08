#!/bin/bash

for f in baa_messages/schema/*.thrift; do
  thrift --out baa_messages/ --gen py $f;
done
git add baa_messages/
