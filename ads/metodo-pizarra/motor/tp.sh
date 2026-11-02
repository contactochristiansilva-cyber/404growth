#!/bin/bash
# tp.sh N BOARD.mp4 → out3/metodo-0N-teleprompter.mp4
D=$(dirname "$0"); cd "$D"; v=$1; board=$2; mkdir -p out3
python3 mktp.py $v
[ -f out3/tp$v-text.mp4 ] || node rendtp.mjs $PWD/tp$v.html $PWD/out3/tp$v-text.mp4 || exit 1
TB=$(python3 -c "import json;print(json.load(open('tp$v.json'))['TB'])")
TOT=$(python3 -c "import json;print(json.load(open('tp$v.json'))['total'])")
ffmpeg -y -loglevel error -i out3/tp$v-text.mp4 -itsoffset $TB -i $board -f lavfi -i "sine=frequency=1000:duration=0.2:sample_rate=48000" \
 -filter_complex "[1:v]scale=300:300:flags=lanczos,format=yuv420p[b];[0:v][b]overlay=916:330:eof_action=pass:enable='gte(t,$TB)'[v];[2:a]volume=2.5,adelay=3000|3000,apad[a]" \
 -map "[v]" -map "[a]" -t $TOT -c:v libx264 -preset veryfast -crf 24 -pix_fmt yuv420p -c:a aac -b:a 96k -ac 1 -movflags +faststart out3/metodo-0$v-teleprompter.tmp.mp4 && mv out3/metodo-0$v-teleprompter.tmp.mp4 out3/metodo-0$v-teleprompter.mp4 && echo done $v
