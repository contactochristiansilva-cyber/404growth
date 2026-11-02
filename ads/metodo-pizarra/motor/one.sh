#!/bin/bash
# one.sh N → out/metodo-0N-pizarra.mp4
D=$(dirname "$0"); cd "$D"; v=$1
python3 v$v.py $PWD/v$v.html >/dev/null
dur=$(grep -o '"dur": [0-9.]*' v$v.html | grep -o '[0-9.]*$')
n=$(python3 -c "import math;print(math.ceil($dur*25))")
node rend.mjs $PWD/v$v.html $PWD/out/metodo-0$v-pizarra.mp4 0 $n 18
