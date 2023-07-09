#!/usr/bin/env bash

# ターミナルログイン設定
echo 'SETTING TERMINAL LOGIN...'
~/data/repo/github.com/undefeated-davout/kali-settings/shell/login.sh

echo 'WAITING FOR LOGIN SETTINGS...'
sleep 2
# # ディスプレイ設定（3ディスプレイ時）
# ~/data/repo/github.com/undefeated-davout/kali-settings/shell/setup_display.sh

# アプリケーション起動
~/data/repo/github.com/undefeated-davout/kali-settings/shell/delayed_launch.sh
