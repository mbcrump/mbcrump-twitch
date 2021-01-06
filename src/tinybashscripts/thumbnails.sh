#!/bin/bash

for i in *.jpg; do
    convert "$i" -resize 400 "$i-tn.jpg";
done;