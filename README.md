# セットアップ手順

## デフォルトユーザ設定

- GNOME + gdm3を選択しておけば、前回指定時のユーザが表示されるようになる

## ネットワーク設定（Cloudflare）

- 高度なネットワーク設定 > <対象のネットワーク（Wi-Fi、Ethernet等）
  - IPv4設定
    - 追加のDNSサーバー: 1.1.1.1,1.0.0.1
    - （Google DNS）: 8.8.8.8,8.8.4.4
  - IPv6設定
    - 追加のDNSサーバー: 2606:4700:4700::1111,2606:4700:4700::1001
    - （Google DNS）: 2001:4860:4860::8888,2001:4860:4860::8844

## Git設定

```bash
git config core.editor vi
git config --global core.editor vi
sudo git config --system core.editor vi
```

## ssh設定

```bash
mkdir ~/.ssh
cd ~/.ssh
ssh-keygen -t rsa

# Githubに公開鍵を登録
sudo apt install xsel
cat ~/.ssh/id_rsa.pub | xsel --clipboard --input
```

## 初期配置

```bash
mkdir ~/apps
mkdir -p ~/data/repo
mkdir -p ~/work/install
```

## anyenv

```bash
git clone https://github.com/anyenv/anyenv ~/.anyenv

# anyenv初期処理
~/.anyenv/bin/anyenv init
anyenv install --init
# Do you want to checkout https://github.com/foo/anyenv-install.git? [y/N]: y

# anyenv updateで更新できるようにする
mkdir -p $(anyenv root)/plugins
git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update
# 更新したいとき
anyenv update
```

## ghq + peco（リポジトリ管理）

### peco

```bash
sudo apt install peco
```

### ghq

```bash
# まずはGoをインストールする
anyenv install goenv
# インストール可能なGoバージョンを確認
goenv install -l
goenv install 1.18.4
goenv global 1.18.4
goenv rehash
　
# ghqインストール
go install github.com/x-motemen/ghq@latest

# ghqディレクトリを設定
git config --global ghq.root '~/data/repo'
```

```bash
# 使い方
ghq get ssh://git@github.com/undefeated-davout/kali-settings.git

# "Ctrl + [" で、取得したghqリポジトリリストを表示、Enterでcd
```

## xfce4 + i3-gaps

### i3-gapsインストール

```bash
cd ~/work/install
git clone https://github.com/superbvgv/i3XFCE4.git
cd i3XFCE4
chmod +x install.sh
./install.sh
cd ..
rm -rf i3XFCE4
```

### i3設定ファイル

```bash
cp ~/data/repo/github.com/undefeated-davout/kali-settings/i3/config ~/.config/i3/config
# 配下にロック画像に使用したい画像を入れる（~/.config/i3/images/lock.jpg）
mkdir ~/.config/i3/images/
```

## ターミナル設定

- 設定 > ショートカット
  - タブを閉じる：Ctrl + w

### 壁紙設定

- nitrogen起動
- Preference
- [Add]ボタンで[/usr/share/backgrounds/kali]を追加
- 壁紙を選び、ZoomFill、Screen1を選択し[Apply]

## Superキー変更

- キーボード > アプリケーションショートカットキー
  - 以下の設定以外のショートカットを削除する。これにより左Cmdキーでメニューが開かれる設定が削除される
    - スクリーンショット関連ショートカットキー

## ディスプレイ設定

- Kali HiDPI mode起動
- ディスプレイ設定
  - 全般
    - ラップトップ：3840x2400（最大）、スケール：0.8
    - 外部ディスプレイ：3840x2160（最大）、スケール：1.2
  - 詳細
    - プロファイルを作成する
    - 接続中のディスプレイ
      - 新しくディスプレイが接続されたとき設定する：ON
      - 新しくディスプレイが接続されたときプロファイルを自動的に有効にする：ON
- パネル設定
  - 複数モニターにまたがって表示する：ON　にするとマルチディスプレイでもラップトップにパネル表示できる

## zshrc読み込み設定

```bash
# ~/.zshrcに以下を追記
[ -f ~/data/repo/github.com/undefeated-davout/kali-settings/shell/.zshrc_custom ] && source ~/data/repo/github.com/undefeated-davout/kali-settings/shell/.zshrc_custom
```

## Chromeインストール

## z コマンド

```bash
git clone https://github.com/rupa/z.git ~/apps/z
```

## fzfコマンド

```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/apps/.fzf
~/apps/.fzf/install
# 質問が3つ表示されるのですべて[y]
. ~/.zshrc
```

## batコマンド

```bash
sudo apt install bat
```

## exaコマンド

```bash
sudo apt install exa
```

## 日本語化

### ディレクトリ名日本語化

```bash
LANG=C xdg-user-dirs-gtk-update
```

### 日本語パッケージインストール

```bash
sudo apt install task-japanese task-japanese-desktop -y
```

### Mozc時デフォルト入力をひらがなにする

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install build-essential devscripts -y
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee -a /etc/apt/sources.list
sudo apt update
sudo apt build-dep ibus-mozc
apt source ibus-mozc

cd mozc-2.23.2815.102+dfsg

# 対象の設定箇所を修正する（false→true）
# vi $(find . -name property_handler.cc)
const bool kActivatedOnLaunch = true;

# 修正したmozcをビルドする
dpkg-buildpackage -us -uc -b
# mozcをインストールする
sudo dpkg -i ../mozc*.deb ../ibus-mozc*.deb
# 再ログインする
```

### mozc設定

- 入力メソッド（白アイコン） > [明示的にユーザ設定を選択しますか？] > [はい] > [ibus]を選択
- 再起動
- 入力メソッド（青アイコン）
  - [全体設定]ペイン
    - 入力方式の利用準備 > 標準の入力方式 : チェックON
    - 入力方式の一時切り替え > ホットキーによる入力方式の一時切り替えを有効にする : チェックON
  - [ツールバー]
    - アイコン > 濃色背景向けアイコンを使用する : チェックON
  - [Mozc]ペイン
    - 標準の入力モード : ひらがな
- Mozcアイコンから設定を開く
  - 一般、絵文字のショートカットをすべて削除する

### トグル解除

- 入力アイコン > 一般
  - スクリーンショット系以外のキーボードショートカット を削除

### 変換候補設定

#### ibus-mozcの変換候補の位置が下端になってしまうのを修正

```bash
sudo apt install ibus-gtk ibus-gtk3
sudo apt install ttf-mscorefonts-installer fonts-roboto fonts-noto fonts-ricty-diminished
```

## キーバインド変更

```bash
cd ~/work/install
git clone --depth 1 https://github.com/mooz/xkeysnail.git
cd xkeysnail
sudo pip3 install --upgrade .

sudo xkeysnail ~/data/repo/github.com/undefeated-davout/kali-settings/xkeysnail/config.py
# [Xlib.error.DisplayConnectionError: Can't connect to display ":0.0": b'No protocol specified] エラー対応
xhost +SI:localuser:root

# すでにユーザが登録されているか確認
getent group uinput
sudo groupadd uinput
sudo usermod -aG input,uinput {ユーザ名}
getent group input
getent group uinput

echo 'KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="input"' | sudo tee /etc/udev/rules.d/70-input.rules
echo 'KERNEL=="uinput", GROUP="uinput"' | sudo tee /etc/udev/rules.d/70-uinput.rules
# PC再起動後
mkdir -p ~/.config/systemd/user/
cp ./systemd/xkeysnail.service ~/.config/systemd/user/xkeysnail.service
# sudoなし起動設定
echo 'uinput' | sudo tee /etc/modules-load.d/uinput.conf
# ログアウト後、uinputモジュールがロードされているか確認する
lsmod | grep uinput
# サービス登録
systemctl --user enable xkeysnail
systemctl --user start xkeysnail
# 登録確認
systemctl --user status xkeysnail
```

```bash
# /etc/systemd/journald.conf ファイルを以下の通り書き換え
Storage=persistent # autoから
SystemMaxUse=1G # ''から
```

- VSCodeでCtrl+Kが効かない問題
  - 設定：Terminal > Integrated: Allow Chords ： OFFにする

## VS Code

```bash
cp ~/data/repo/github.com/undefeated-davout/kali-settings/vscode_settings/settings.json ~/.config/Code/User/
cp ~/data/repo/github.com/undefeated-davout/kali-settings/vscode_settings/keybindings.json ~/.config/Code/User/
```

## マウス設定

```bash
sudo apt install piper
```

- Piperを起動して、各ボタンを設定する

## redshift（ブルーライト軽減）

```bash
sudo apt install redshift redshift-gtk

cp ./redshift/redshift.conf ~/.config/redshift.conf
```

- Redshift起動
- システムトレイに電球アイコンが表示されるので、「自動起動」ONにしておく

## Timeshift

```bash
# Timeshiftインストール
sudo apt install -y timeshift
```

- USBメモリ初期化
  - ディスク設定起動
  - 対象USB選択
  - 右上三点リーダ > ディスクを初期化
    - 消去：既存のデータを上書きしない
    - パーティション：パーティションなし
  - ボリュームの歯車マーク > 暗号化オプションを編集
    - ユーザセッションのデフォルト：OFF
    - システム起動時にロック解除する：ON
    - パスフレーズ：暗号化解除用パスワードを入力する
  - ボリュームの歯車マーク > パーティションを初期化
    - ボリューム名：Timeshift（任意）
    - 消去：OFF
    - タイプ：Linux用の内蔵ディスクとして使用する
      - ボリュームをパスワードで保護する：ON
  - 再生マーク▶でマウント
- Timeshift起動
  - タイプ：RSYNC
  - スナップショットの場所
    - 先ほど作成したUSBボリューム：Timeshiftを選択
  - スケジュール
    - 週次：4
    - 日次：7
  - ユーザーホームディレクトリ：各ディレクトリ「すべて含める」を選択
  - パターンを含める／除外する：変更なし
  - 日付形式：変更なし
- Timeshift「新規作成」から初回のバックアップ取得
- USB：次回起動時、パスワードを入力して保存設定を適宜選択

## Default Keyringのパスワード入力回避

```bash
sudo apt install seahorse
```

- [パスワードと鍵] > Default keyring > 右クリック > パスワードを変更
  - 新しいパスワードを空文字で登録

## Dockerインストール

```bash
# Docker
# sudo apt -y install curl gnupg2 apt-transport-https software-properties-common ca-certificates
# curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
# echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" | sudo tee /etc/apt/sources.list.d/docker.list
# sudo apt update
# sudo apt install docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker $USER
cat /etc/group | grep docker
docker -v
# 自動起動設定
# sudo systemctl enable docker --now
# systemctl disable docker # 自動起動無効

# Docker Desktop
# https://docs.docker.com/desktop/linux/install/ よりdebファイルダウンロード
sudo apt install ./docker-desktop-4.8.2-amd64.deb
systemctl --user start docker-desktop
# docker-composeはDocker Desktopに付いてインストールされる
# Docker Desktopを起動し General > Enable Docker Compse V1/V2 compatibility mode をONにする
```

### Docker desktop設定

- General
  - Enable Docker Compose V1/V2 compatibility mode: ON
- Resources
  - CPU: 4
  - Memory: 8GB

## Bluetooth設定

```bash
sudo apt install bluetooth blueman
sudo systemctl enable bluetooth --now
```

## VirtualBoxインストール

```bash
# GPGキーインポート
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -

echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian buster contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list

sudo apt update
sudo apt install virtualbox

# 拡張パックをダウンロードする（https://www.virtualbox.org/wiki/Downloads）
sudo VBoxManage extpack install ./Oracle_VM_VirtualBox_Extension_Pack-6.1.34.vbox-extpack
# Do you agree to these license terms and conditions (y/n)? → y と回答する
# USB機器にアクセスできるようグループに追加
sudo usermod -aG vboxusers $USER
cat /etc/group | grep vboxusers
```

## gotop

```bash
cd ~/work/install
git clone --depth 1 https://github.com/cjbassi/gotop /tmp/gotop
/tmp/gotop/scripts/download.sh
sudo mv ./gotop /usr/local/bin/
```

## htop

```bash
sudo apt install htop
```

## jq

```bash
sudo apt install jq
```

## Kindle

### Wine

```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install wine32 wine64
wine --version
# wine-6.0.3 (Debian 6.0.3~repack-1)
winecfg
```

- winecfg設定
  - アプリケーション
    - Windowsバージョン：Windows 8.1
  - 画面
    - 画面の解像度：192dpi

### Kindle for Windows

```bash
mkdir -p ${WINEPREFIX:-$HOME/.wine}/drive_c/users/$USER/AppData/Local/Amazon/Kindle
wine ./Kindle_for_PC_Windows_ダウンロード.exe

# GeckoをインストールしWebページを表示できるように
wget https://dl.winehq.org/wine/wine-gecko/2.47.2/wine-gecko-2.47.2-x86_64.msi
wget https://dl.winehq.org/wine/wine-gecko/2.47.2/wine-gecko-2.47.2-x86.msi
wine msiexec /i wine-gecko-2.47.2-x86_64.msi
wine msiexec /i wine-gecko-2.47.2-x86.msi

# Wine再起動
wineboot
```

- 電源管理 > セキュリティ
  - スリープ状態へ遷移中は画面をロックする：OFF

## 時計表示

```bash
%m/%d(%a) %p %I:%M
```

## ログイン画面のユーザアイコン設定

- gdm3ログイン画面のアイコンの設定は、GNOMEで行う
- /usr/share/pixmaps/faces/ 配下の画像しか選択できないのでこのディレクトリへ画像をコピーしておく

## BurpSuite

### Burpインストール

- <https://portswigger.net/burp/communitydownload> [Go straight to downloads]よりダウンロード

```bash
# 既存のBurp Suiteはアンインストール
sudo apt remove burpsuite
# sudo shで実行
sudo sh ./burpsuite_community_linux_v2022_3_9.sh
```

### Burp設定

- Chrome拡張[SwitchySharp Options]をインストール
- SwitchySharp Options設定
  - Use the same proxy server for all protocols: ON
  - No Proxy for: <-loopback>
- 証明書
  - localhost:8080にアクセスし証明書ダウンロード
  - Chrome > 設定 > プライバシーとセキュリティ > セキュリティ > 証明書の管理 > 認証局 > インポート
    - 前項でダウンロードしたcacert.derを指定
    - Trust this certificate foridentifying websites：ON

## カーソル非表示

```bash
sudo apt install unclutter

# /etc/default/unclutter を書き換えて再起動
EXTRA_OPTS="-idle 15 -root"
```

## スクリーンロック設定

```bash
xfconf-query -c xfce4-session -p /general/LockCommand -s "i3lock -t -e -i ~/.config/i3/images/lock.jpg" --create -t string
```

## Clipman

- Clipman > プロパティ > 即時貼り付け
  - なし→ [Ctrl + V] に変更

## ブラウザ版 man

```bash
sudo apt install man2html swish++ xapp
sudo a2enmod cgid
sudo systemctl enable apache2 --now

# sudo vi /etc/apache2/ports.conf
# Listen 80 を以下に変更
Listen 8050
```

- <http://localhost:8050/cgi-bin/man/man2html> にアクセスするとmanをブラウザで表示できる

## Python

### pyenv

```bash
anyenv install pyenv

# pyenvによるPythonインストール
# インストール可能バージョン一覧
pyenv install --list
# インストール
pyenv install 3.10.5
pyenv global 3.10.5

# Pythonインストールでエラーになる場合
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### venv

```bash
sudo apt install python3-venv
mkdir ~/.venvs/
cd ~/.venvs/
python -m venv venv3

# 環境を無効化
deactivate

# Pythonバージョン指定して環境を作成するとき
pyenv install 3.8.13 # 環境作成直前にglobalバージョンを変更
python -m venv venv3.8 # 新規作成
python -m venv venv3.8 --clear # すでに作成しているとき
# バージョンをもとに戻しておく
pyenv global 3.10.5

# Python2系で環境を作成するとき
pyenv install 2.7.18
cd ~/.venvs/
virtualenv venv2
source ~/.venvs/venv2/bin/activate
```

## PDF圧縮

```bash
sudo apt install ghostscript

# 対象のディレクトリに移動して実行
pdfmin *.pdf
```

## pwntools

```bash
sudo apt update
sudo apt install python3-dev build-essential
pip install --upgrade pip
pip install --upgrade pwntools
```

## 自動翻訳

```bash
# https://chromedriver.chromium.org/downloads からChromeのバージョンに該当するドライバをダウンロード
unzip ./chromedriver_linux64.zip
mkdir ~/apps/chromedriver/
mv ./chromedriver ~/apps/chromedriver/
```

## TryHackMe

```bash
# OpenVPN
sudo apt install openvpn
# ダウンロードした.ovpnファイルを指定して接続（US-West-Regular-1）
sudo openvpn {.ovpnファイルのパス}
# もしくは
# Wi-Fiアイコン > VPN接続 > VPNを設定 > 追加 > 保存したVPN設定をインポートする
```

## Git

```bash
mkdir ~/.zsh
cd ~/.zsh

curl -o git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
curl -o git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
curl -o _git https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.zsh
```

## Nerd Fonts

```bash
# 例）Hackフォント用の設定方法

# 各ttfファイルをダウンロード
https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/Hack/Regular/complete

# /usr/share/fonts/truetype/hack/ ディレクトリにダウンロードしたttfファイルをコピーする

# フォントを適用
fc-cache -fv
```

## ワークスペース設定

```bash
sudo apt install wmctrl
# ワークスペース名一覧を表示
xfconf-query -c xfwm4 -p /general/workspace_names
# ワークスペース名を設定
xfconf-query -c xfwm4 -p /general/workspace_names -t string -t string -t string -t string -t string -t string -t string -t string -t string -t string -s "1" -s "2" -s "3" -s "4" -s "5" -s "6" -s "7" -s "8" -s "9" -s "0"
```

## ポモドーロタイマー

```bash
# https://github.com/Splode/pomotroid/releases からdebファイルをダウンロードする
sudo apt install ./pomotroid-0.13.0-linux.deb
```

- /opt/Pomotroid/pomotroid を自動起動設定する

## リモートデスクトップ

```bash
echo 'deb http://ftp.debian.org/debian stretch-backports main' | sudo tee --append /etc/apt/sources.list.d/stretch-backports.list >> /dev/null
sudo apt update
sudo apt install -t stretch-backports remmina-plugin-rdp remmina-plugin-secret remmina-plugin-spice


sudo apt install software-properties-common
sudo apt-add-repository ppa:remmina-ppa-team/remmina-next
sudo apt update
sudo apt install remmina remmina-plugin-rdp
```

## Wi-Fi省力モードOFF

```bash
sudo iwconfig wlan0 power off
# GNOMEには電源管理から[パフォーマンス]を選択できるが[Power Management:off]にはならない
iwconfig

# 設定ファイル作成
sudo vi /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
# (0): use the default value
# (1): don't touch existing setting
# (2): disable powersave
# (3): enable powersave
# ↓以下を記載
[connection]
wifi.powersave = 2

# 再起動して反映
NetworkManager restart
```

## 自動ログイン

```bash
# sudo vi /etc/pam.d/gdm-password 先頭行に以下を追記
auth sufficient pam_succeed_if.so user ingroup nopasswdlogin

# nopasswdloginグループをシステムに追加
groupadd -r nopasswdlogin
gpasswd -a $USER nopasswdlogin

# ユーザ名をクリックするだけでログインできるようになる
```

## Translate Shell（ターミナル上で翻訳）

```bash
wget git.io/trans
sudo mv ./trans /usr/local/bin/
chmod +x /usr/local/bin/trans
```

## glow（ターミナル上でMarkdownプレビュー）

```bash
echo 'deb [trusted=yes] https://repo.charm.sh/apt/ /' | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install glow
```
