#!/usr/bin/env bash

# 最終行をダークモード設定に書き換え
sudo sed -r -i 's/exec -a \"\$0\" \"\$HERE\/chrome\" \"\$@\"/exec -a \"\$0\" \"\$HERE\/chrome\" \"--enable-features=WebUIDarkMode\" \"--force-dark-mode\" \"\$@\"/' /opt/google/chrome/google-chrome
