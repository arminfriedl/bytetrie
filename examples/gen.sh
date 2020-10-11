#!/bin/sh

xwim cities500.tar.gz
mv cities500/cities500.txt .
rmdir cities500
python geonames.py
twopi -Tpng geo_dot.dot -o geo_dot_twopi.png -Groot=root -x
