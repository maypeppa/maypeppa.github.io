#!/usr/bin/env bash
# Copyright (C) dirlt

# 文件夹下面所有的avi文件抽取mp3出来
# 并且将音量增加到10倍（但是很容易有杂音）
for x in *.avi
do
  y=${x/avi/mp3}
  ffmpeg -i $x -af “volume=10” $y
done
