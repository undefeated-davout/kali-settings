#!/usr/bin/env bash

# ディレクトリをクリーン
sudo rm -rf /tmp/install_mozc/
mkdir -p /tmp/install_mozc/
cd /tmp/install_mozc/

# ソースをダウンロード
apt source ibus-mozc
cd /tmp/install_mozc/mozc-*

# const bool kActivatedOnLaunch = false; → const bool kActivatedOnLaunch = true; に書き換え
sed -i -e "s/const\sbool\skActivatedOnLaunch\s=\sfalse;/const bool kActivatedOnLaunch = true;/" ./src/unix/ibus/property_handler.cc

# ビルド
dpkg-buildpackage -us -uc -b
# インストール
sudo dpkg -i ../mozc*.deb ../ibus-mozc*.deb

# 使用したソースを削除
rm -rf /tmp/install_mozc/
