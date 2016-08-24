#!/bin/bash

# Directory where this script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Moving to the head of the repo to perform operations
pushd "$DIR/../"
cwd=$(pwd)
if [ -d "$cwd/baa_messages/messages/" ]; then
    echo -e "Removing old thrift messages library  ..."
    echo -e "$cwd/baa_messages/messages"
    rm -r "$cwd/baa_messages/messages"

    echo -e "Removing old thrift docs..."
    echo -e "$cwd/docs/thrift/*"
    rm -r "$cwd"/docs/thrift/*
    mkdir "$cwd"/docs/thrift/sensor
    mkdir "$cwd"/docs/thrift/algorithm
fi



echo -e "Compiling Sensor Components..."

for f in "$cwd"/baa_messages/schema/sensor/*.thrift; do
    echo -e "Compiling: $f..."
    thrift --out "$cwd" --gen py $f;
    thrift -r --gen gv --out "$cwd"/docs/thrift/sensor $f;
done

echo -e "Compiling Algorithm Components..."

for f in "$cwd"/baa_messages/schema/algorithm/*.thrift; do
    echo -e "Compiling: $f..."
    thrift --out "$cwd" --gen py $f;
    thrift -r --gen gv --out "$cwd"/docs/thrift/algorithm $f;
done

echo -e "Compiling Main thrift..."

for f in "$cwd"/baa_messages/schema/*.thrift; do
    echo -e "Compiling: $f..."
    thrift -I "$cwd"/baa_messages/schema/sensors --out "$cwd" --gen py $f;
    thrift -r --gen gv --out "$cwd"/docs/thrift/ $f;
done


rm "$cwd"/__init__.py
popd
# Creating PDF from gv
pushd "$cwd"/docs/thrift
for f in *.gv; do
  arrIN=(${f//./ })
  dot -Tpdf -o"$arrIN.pdf" $f
done
popd

git add "$cwd"/baa_messages/
git add "$cwd"/docs/


#
#
## Checking to make sure entered at proper location
#if [ ! -f $(readlink "./bin/thrift-compile.sh") ]; then
#    echo .
#    echo -e "ERROR!!: thrift-compile.sh must be executed from top level of the baa_messages repo"
#    exit 1
#fi

#
## removing old messages
#rm -r baa_messages/messages/*
#for f in baa_messages/schema/*.thrift; do
#  thrift --out ./ --gen py $f;
#  thrift -r --gen gv --out docs/thrift $f;
#done
#rm __init__.py
#pushd docs/thrift/
#for f in *.gv; do
#  arrIN=(${f//./ })
#  dot -Tpdf -o"$arrIN.pdf" $f
#done
#popd
#
#git add baa_messages/
#git add docs/
