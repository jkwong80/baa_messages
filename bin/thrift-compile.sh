#!/bin/bash

thrift --out baa_messages/thrift_lib --gen py baa_messages/*.thrift
git add --all
