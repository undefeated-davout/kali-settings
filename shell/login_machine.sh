#!/usr/bin/env bash

# ターミナルログイン設定
echo 'SETTING TERMINAL LOGIN...'
~/data/repo/github.com/undefeated-davout/kali-settings/shell/login.sh

echo 'WAITING FOR LOGIN SETTINGS...'
sleep 5
# ディスプレイ設定（3ディスプレイ時）
~/data/repo/github.com/undefeated-davout/kali-settings/shell/setup_display.sh
