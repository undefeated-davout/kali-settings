#!/usr/bin/env bash

echo 'SET DUMMY DISPLAY SETTINGS'
sleep 0.1
# ディスプレイ設定（3ディスプレイ時）
# 「設定変更した」とKali Linuxに認識させるためのダミー設定
xrandr --output eDP-1 --mode 3840x2400 --pos 2160x2228 --rotate normal \
       --output DP-1-0 --mode 3840x2160 --pos 2360x68 --rotate normal \
       --output DP-1-2 --mode 3840x2160 --pos 0x100 --rotate left
sleep 2
echo 'SET REAL DISPLAY SETTINGS'

sleep 0.1
# 実際に適用したい設定
xrandr --output eDP-1 --mode 3840x2400 --pos 2160x2228 --rotate normal \
       --output DP-1-0 --mode 3840x2160 --pos 2160x68 --rotate normal \
       --output DP-1-2 --mode 3840x2160 --pos 0x0 --rotate left
echo 'DISPLAY SETTINGS OVER'
