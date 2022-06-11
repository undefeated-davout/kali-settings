#!/usr/bin/env bash

# ~/.zshrcに本スクリプトを実行するよう追記して使用

# 入力モードを「直接入力」にする
ibus engine 'xkb:us::eng'

# ワークスペース名設定
xfconf-query -c xfwm4 -p /general/workspace_names -t string -t string -t string -t string -t string -t string -t string -t string -t string -t string -s "1" -s "2" -s "3" -s "4" -s "5" -s "6" -s "7" -s "8" -s "9" -s "0"
