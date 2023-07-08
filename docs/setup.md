# セットアップ手順

## インストール

- ロケーションはUS、Centralを選択しておく。後でAsia/Tokyoに変更する。

## デフォルトユーザ設定

- GNOME + gdm3 を選択しておけば、前回指定時のユーザが表示されるようになる

## ネットワーク設定（Cloudflare）

- 高度なネットワーク設定 > <対象のネットワーク（Wi-Fi、Ethernet 等）
  - IPv4 設定
    - 追加の DNS サーバー: 1.1.1.1,1.0.0.1
    - （Google DNS）: 8.8.8.8,8.8.4.4
  - IPv6 設定
    - 追加の DNS サーバー: 2606:4700:4700::1111,2606:4700:4700::1001
    - （Google DNS）: 2001:4860:4860::8888,2001:4860:4860::8844

## ディスプレイ設定

- （ThinkPad X1 Extreme時）NVIDIAドライバインストールし、外部ディスプレイを使えるようにする
- <https://www.kali.org/docs/general-use/install-nvidia-drivers-on-kali-linux/>
- ドライバは上記で順ではなく、以下のリンクを使う。再起動すると外部ディスプレイ2枚使えるようになった。
  - <https://www.nvidia.co.jp/Download/driverResults.aspx/199656/en-us>

## Chrome インストール

- <https://www.google.com/chrome/>から deb ファイルをダウンロードし、apt install
- ダークモード設定

  - `/opt/google/chrome/google-chrome` の最終行を書き換える

  ```bash
  # exec -a "$0" "$HERE/chrome" "$@"
  # ↓
  # exec -a "$0" "$HERE/chrome" "--enable-features=WebUIDarkMode" "--force-dark-mode" "$@"
  # に書き換えるスクリプト
  sudo sh ./scripts/chrome_dark_mode.sh
  ```

## bat コマンド

```bash
# bat, exaコマンド
# 日本語パッケージ
# xsel：コピーツール
# peco：リポジトリ選択ツール
# build-essential devscripts：Mozcに必要
# ibus-gtk：ibus-mozcの変換候補の位置が下端になってしまうのを修正
# piper：マウス設定
# redshift：ブルーライトカット
# timeshift：バックアップ
# seahorse：キーリング空文字許容
# ghostscript：PDF圧縮
sudo apt install -y \
  kali-linux-large \
  bat \
  exa \
  xsel \
  peco \
  build-essential \
  devscripts \
  ibus-gtk \
  ibus-gtk3 \
  ibus-mozc \
  ttf-mscorefonts-installer \
  fonts-roboto \
  fonts-noto \
  fonts-ricty-diminished \
  piper \
  redshift \
  redshift-gtk \
  timeshift \
  seahorse \
  bluetooth \
  blueman \
  htop \
  jq \
  ghostscript \
  python3-dev \
  build-essential \
  man2html \
  swish++ \
  xapp-sn-watcher \
  libxapp-gtk3-module \
  openvpn \
  wmctrl \
  xinput \
  libinput-tools \
  task-japanese \
  task-japanese-desktop \
  rlwrap
```

## Git 設定

```bash
mkdir ~/.zsh
cd ~/.zsh

git config --global core.editor vi
sudo git config --system core.editor vi

curl -o git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
curl -o git-completion.bash https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
curl -o _git https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.zsh
```

## ssh 設定

```bash
mkdir ~/.ssh
cd ~/.ssh
ssh-keygen -t rsa

# Githubに公開鍵を登録
cat ~/.ssh/id_rsa.pub | xsel --clipboard --input
```

### ~/.ssh/config例

```bash
Host private-github.com
  HostName github.com
  User git
  Port 22
  IdentityFile ~/.ssh/private/id_rsa_github_private
  IdentitiesOnly yes
```

## 初期配置

```bash
mkdir ~/apps
mkdir -p ~/data/repo
mkdir -p ~/work/install
```

## zshrc 読み込み設定

```bash
# ~/.zshrcに以下を追記
# --- custom ---
source ~/data/repo/github.com/undefeated-davout/kali-settings/shell/.zshrc_custom
```

## anyenv

```bash
git clone https://github.com/anyenv/anyenv ~/.anyenv

# anyenv初期処理
~/.anyenv/bin/anyenv init
exec $SHELL -l
anyenv install --init
# Do you want to checkout https://github.com/foo/anyenv-install.git? [y/N]: y

# anyenv updateで更新できるようにする
mkdir -p $(anyenv root)/plugins
git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update
# 更新したいとき
anyenv update
```

## Python

### pyenv

```bash
anyenv install pyenv
exec $SHELL -l

# for avoid install error
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# pyenvによるPythonインストール
# インストール可能バージョン一覧
pyenv install --list
# インストール
pyenv install 3.11.2
pyenv global 3.11.2
pyenv rehash
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
cd ~/.venvs/
pyenv install 3.9.12 # 環境作成直前にglobalバージョンを変更
pyenv global 3.9.12
python -m venv venv3.9 # 新規作成
# python -m venv venv3.9 --clear # すでに作成しているとき
pyenv global 3.11.2 # バージョンをもとに戻しておく
# 環境を有効化
source ~/.venvs/venv3.9/bin/activate


# Python2系で環境を作成するとき
cd ~/.venvs/
pyenv install 2.7.18
virtualenv -p python2 venv2
source ~/.venvs/venv2/bin/activate
# pipインストールするとき
python -m pip install {target library}
```

## ghq + peco（リポジトリ管理）

### ghq

```bash
# remove existing go
sudo rm /usr/bin/go
# まずはGoをインストールする
anyenv install goenv
exec $SHELL -l
# インストール可能なGoバージョンを確認
goenv install -l
goenv install 1.20.1
goenv global 1.20.1
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

### i3-gaps インストール

```bash
cd ~/work/install
git clone https://github.com/superbvgv/i3XFCE4.git
cd i3XFCE4
chmod +x install.sh
./install.sh
cd ..
rm -rf i3XFCE4
```

- Session and Startup の設定
  - xfwm4: Never
  - xfdesktop: Never

### i3 設定ファイル

```bash
cp ~/data/repo/github.com/undefeated-davout/kali-settings/i3/config ~/.config/i3/config
# 配下にロック画像に使用したい画像を入れる（~/.config/i3/images/lock.jpg）
mkdir ~/.config/i3/images/
```

## ターミナル設定

- 設定 > ショートカット
  - Close Tab: Ctrl + w
  - Paste Clipbord: Ctrl + V

### 壁紙設定

- nitrogen 起動
- Preference
- [Add]ボタンで[/usr/share/backgrounds/kali]を追加
- 壁紙を選び、ZoomFill、Screen1 を選択し[Apply]

## Super キー変更

- キーボード > アプリケーションショートカットキー
  - 以下の設定以外のショートカットを削除する。これにより左 Cmd キーでメニューが開かれる設定が削除される
    - スクリーンショット関連ショートカットキー

## ディスプレイ設定

- Kali HiDPI mode 起動
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
  - 複数モニターにまたがって表示する：ON 　にするとマルチディスプレイでもラップトップにパネル表示できる

## z コマンド

```bash
git clone https://github.com/rupa/z.git ~/apps/z
```

## fzf コマンド

```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/apps/.fzf
~/apps/.fzf/install
# 質問が3つ表示されるのですべて[y]
. ~/.zshrc
```

### mozc 設定

- 入力削除メソッド（白アイコン） > [明示的にユーザ設定を選択しますか？] > [はい] > [ibus]を選択
- 再起動
- 入力メソッド（青アイコン）
  - [Global settings]
    - Specify default IM: ON
    - Enable IM switching by hotkey: ON
    - Enable input method toggle by hot keys: OFF
  - [Mozc]
    - Default input mode: Hiragana
  - [Toolbar]
    - Use icon for dark background: ON
- Mozc アイコンから設定を開く
  - 一般、絵文字のショートカットをすべて削除する

### Mozc 時デフォルト入力をひらがなにする

```bash
sudo apt update
sudo apt upgrade -y
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" | sudo tee -a /etc/apt/sources.list
sudo apt update
sudo apt build-dep ibus-mozc

# # ソースをダウンロードしビルド→インストール
# sh ~/data/repo/github.com/undefeated-davout/kali-settings/scripts/hiragana_mozc.sh
vim ~/.config/mozc/ibus_config.textproto
# 以下の設定を追加する
# active_on_launch: True

# 再ログインする
```

### トグル解除

- 入力アイコン > 一般
  - スクリーンショット系以外のキーボードショートカット を削除

## キーバインド変更

```bash
cd ~/work/install
git clone --depth 1 https://github.com/mooz/xkeysnail.git
cd xkeysnail
sudo pip install --upgrade .

sudo xkeysnail ~/data/repo/github.com/undefeated-davout/kali-settings/xkeysnail/config.py
# [Xlib.error.DisplayConnectionError: Can't connect to display ":0.0": b'No protocol specified] エラー対応
xhost +SI:localuser:root

# すでにユーザが登録されているか確認
getent group uinput
sudo groupadd uinput
sudo usermod -aG input,uinput $USER
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
systemctl --user enable xkeysnail --now
# 登録確認
systemctl --user status xkeysnail
```

```bash
# sudo vim /etc/systemd/journald.conf ファイルを以下の通り書き換え
Storage=persistent # autoから
SystemMaxUse=1G # ''から
```

## VS Code

```bash
cp ~/data/repo/github.com/undefeated-davout/kali-settings/vscode_settings/* ~/.config/Code/User/
```

## マウス設定

- Piper を起動して、各ボタンを設定する

## redshift（ブルーライト軽減）

```bash
cp ./redshift/redshift.conf ~/.config/redshift.conf
```

- Redshift 起動
- システムトレイに電球アイコンが表示されるので、「自動起動」ON にしておく

## Default Keyring のパスワード入力回避

- [パスワードと鍵] > Default keyring > 右クリック > パスワードを変更
  - 新しいパスワードを空文字で登録

## Docker インストール

```bash
# Docker
sudo apt -y install curl gnupg2 apt-transport-https software-properties-common ca-certificates
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

sudo usermod -aG docker $USER
cat /etc/group | grep docker
docker -v

# Docker Desktop
# https://docs.docker.com/desktop/linux/install/ よりdebファイルダウンロード（Debian）
sudo apt install ./docker-desktop-4.16.2-amd64.deb

modprobe kvm
modprobe kvm_intel
lsmod | grep kvm
ls -al /dev/kvm
sudo usermod -aG kvm $USER

# docker-composeはDocker Desktopに付いてインストールされる
# Docker Desktopを起動し General > Enable Docker Compse V1/V2 compatibility mode をONにする
```

### Docker desktop 設定

- General
  - Enable Docker Compose V1/V2 compatibility mode: ON
- Resources
  - CPU: 4
  - Memory: 8GB

## Bluetooth 設定

```bash
sudo systemctl enable bluetooth --now

# connect
bluetoothctl
power on
agent on
default-agent
scan on
pair {対象のMACアドレス}
connect {対象のMACアドレス}
trust {対象のMACアドレス}

# finish
scan off
exit
```

## VirtualBox インストール

```bash
# GPGキーインポート
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -

echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian buster contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list

sudo apt update
sudo apt install virtualbox

# 拡張パックをダウンロードする（https://www.virtualbox.org/wiki/Downloads or https://download.virtualbox.org/virtualbox/）
sudo VBoxManage extpack install ./Oracle_VM_VirtualBox_Extension_Pack-6.1.38-153438.vbox-extpack
# Do you agree to these license terms and conditions (y/n)? → y と回答する
# USB機器にアクセスできるようグループに追加
sudo usermod -aG vboxusers $USER
cat /etc/group | grep vboxusers
```

## Vagrant

- <https://developer.hashicorp.com/vagrant/downloads> > Binary download for Linux > I686 の deb ファイルをダウンロード
- apt install する

## Windows 環境

- <https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/>にアクセスし、以下の zip(ova 同梱)をダウンロード
  - IE8 on Win7 (x86)
  - IE11 on Win81 (x86)

## Metasploitable2

- <https://sourceforge.net/projects/metasploitable/files/Metasploitable2/>

## Metasploitable3

- <https://github.com/rapid7/metasploitable3>の Quick-Start の手順通りに構築

```bash
mkdir metasploitable3-workspace
cd metasploitable3-workspace
# curl -O https://raw.githubusercontent.com/rapid7/metasploitable3/master/Vagrantfile && vagrant up
# ↑の手順だとエラーになるので、以下の手順に変更
wget https://raw.githubusercontent.com/rapid7/metasploitable3/master/Vagrantfile
# Vagrantfileの
# ub1404.vm.network "private_network", ip: '172.28.128.3'
# ↓ 固定IPをDHCPタイプに書き換える
# ub1404.vm.network "private_network", type: "dhcp"
vagrant up
```

## gotop

```bash
cd ~/work/install
git clone --depth 1 https://github.com/cjbassi/gotop /tmp/gotop
/tmp/gotop/scripts/download.sh
sudo mv ./gotop /usr/local/bin/
```

## Kindle

- [アーカイブ](https://kindle-for-pc.jp.uptodown.com/windows/versions)からバージョン[1.39.65383]をダウンロード

```bash
sudo dpkg --add-architecture i386
sudo apt update && sudo apt -y full-upgrade
sudo apt install wine

wine --version
# wine-8.0

# 解像度を変更する Windows 10, 192dpi
winecfg

# インストール
wine ./kindle-1-39-65383.exe
```

## スリープ設定

- 電源管理 > セキュリティ
  - スリープ状態へ遷移中は画面をロックする：OFF

## 時計表示

```bash
%m/%d (%a) %I:%M %p
```

## ログイン画面のユーザアイコン設定

- gdm3 ログイン画面のアイコンの設定は、GNOME で行う
- /usr/share/pixmaps/faces/ 配下の画像しか選択できないのでこのディレクトリへ画像をコピーしておく

## BurpSuite

### Burp インストール

- [https://portswigger.net/burp/communitydownload](https://portswigger.net/burp/communitydownload) [Go straight to downloads]よりダウンロード

```bash
# 既存のBurp Suiteはアンインストール
sudo apt remove burpsuite
# sudo shで実行
sudo sh ./burpsuite_community_linux_v2022_12_7.sh
```

### Burp 設定

- Chrome 拡張[SwitchySharp Options]をインストール
- SwitchySharp Options 設定
  - HTTP Proxy: localhost
  - Port: 8080
  - Use the same proxy server for all protocols: ON
  - No Proxy for: <-loopback>
- 証明書
  - localhost:8080 にアクセスし証明書ダウンロード
  - Chrome > 設定 > プライバシーとセキュリティ > セキュリティ > 証明書の管理 > 認証局 > インポート
    - 前項でダウンロードした cacert.der を指定
    - Trust this certificate foridentifying websites：ON

## スクリーンロック設定

```bash
xfconf-query -c xfce4-session -p /general/LockCommand -s "i3lock -t -e -i ~/.config/i3/images/lock.jpg" --create -t string
```

## Clipman

- Clipman > プロパティ > 即時貼り付け
  - なし → [Ctrl + V] に変更

## ブラウザ版 man

```bash
sudo a2enmod cgid
sudo systemctl enable apache2 --now

# sudo vim /etc/apache2/ports.conf
# Listen 80 を以下に変更
Listen 8050

# 起動
sudo a2enmod cgid
sudo systemctl enable apache2 --now
```

- [http://localhost:8050/cgi-bin/man/man2html](http://localhost:8050/cgi-bin/man/man2html) にアクセスすると man をブラウザで表示できる
- [/var/www/html]に favicon.ico を配置するとファビコンが表示される

### デフォルトブラウザの設定

```bash
# デフォルトブラウザ設定でChromeを選択する
sudo update-alternatives --config x-www-browser
sudo update-alternatives --config gnome-www-browser
```

## PDF 圧縮

```bash
# 対象のディレクトリに移動して実行
pdfmin *.pdf
```

## pwntools

```bash
pip install --upgrade pip
pip install --upgrade pwntools
```

## 自動翻訳

```bash
# https://chromedriver.chromium.org/downloads からChromeのバージョンに該当するドライバをダウンロード
unzip ./chromedriver_linux64.zip
mkdir ~/apps/chromedriver/
mv ./chromedriver ~/apps/chromedriver/
pip install pyautogui
```

## TryHackMe

```bash
# ダウンロードした.ovpnファイルを指定して接続（US-West-Regular-1）
sudo openvpn {.ovpnファイルのパス}
# もしくは
# Wi-Fiアイコン > VPN接続 > VPNを設定 > 追加 > 保存したVPN設定をインポートする
```

## Nerd Fonts

```bash
# 例）Hackフォント用の設定方法

# 各ttfファイルをダウンロード
https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/Hack/Regular/complete

# /usr/share/fonts/truetype/hack/ ディレクトリにダウンロードしたttfファイルをコピーする
sudo cp ./*.ttf /usr/share/fonts/truetype/hack/

# フォントを適用
fc-cache -fv
```

## ワークスペース設定

```bash
# ワークスペース名一覧を表示
xfconf-query -c xfwm4 -p /general/workspace_names
# ワークスペース名を設定
xfconf-query -c xfwm4 -p /general/workspace_names -t string -t string -t string -t string -t string -t string -t string -t string -t string -t string -s "1" -s "2" -s "3" -s "4" -s "5" -s "6" -s "7" -s "8" -s "9" -s "0"
```

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

## Wi-Fi 省力モード OFF

```bash
sudo iwconfig wlan0 power off
# GNOMEには電源管理から[パフォーマンス]を選択できるが[Power Management:off]にはならない
iwconfig

# 設定ファイル作成
sudo vim /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
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
# sudo vim /etc/pam.d/gdm-password 先頭行に以下を追記
auth sufficient pam_succeed_if.so user ingroup nopasswdlogin

# nopasswdloginグループをシステムに追加
sudo groupadd -r nopasswdlogin
sudo gpasswd -a $USER nopasswdlogin

# ユーザ名をクリックするだけでログインできるようになる
```

## 通知ポップアップのテーマが変更されてしまうので戻す

```bash
# すべてコメントアウト
sudo vim /usr/lib/systemd/user/dunst.service
```

## Translate Shell（ターミナル上で翻訳）

```bash
wget git.io/trans
sudo mv ./trans /usr/local/bin/
chmod +x /usr/local/bin/trans
```

## glow（ターミナル上で Markdown プレビュー）

```bash
echo 'deb [trusted=yes] https://repo.charm.sh/apt/ /' | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install glow
```

## Pomatez（ポモドーロタイマー）

- <https://roldanjr.github.io/pomatez/>で deb ファイルをダウンロードして apt インストール

## Timeshift

- USB メモリ初期化
  - ディスク設定起動
  - 対象 USB 選択
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
    - タイプ：Linux 用の内蔵ディスクとして使用する
      - ボリュームをパスワードで保護する：ON
  - 再生マーク ▶ でマウント
- Timeshift 起動
  - タイプ：RSYNC
  - スナップショットの場所
    - 先ほど作成した USB ボリューム：Timeshift を選択
  - スケジュール
    - 週次：4
    - 日次：7
  - ユーザーホームディレクトリ：各ディレクトリ「すべて含める」を選択
  - パターンを含める／除外する：変更なし
  - 日付形式：変更なし
- Timeshift「新規作成」から初回のバックアップ取得
- USB：次回起動時、パスワードを入力して保存設定を適宜選択

## SmartGit

- <https://www.syntevo.com/smartgit/download/>でdebファイルをダウンロード
- apt installでインストールする

## GitHub Desktop

```bash
sudo rpm --import https://rpm.packages.shiftkey.dev/gpg.key
sudo sh -c 'echo -e "[shiftkey-packages]\nname=GitHub Desktop\nbaseurl=https://rpm.packages.shiftkey.dev/rpm/\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=https://rpm.packages.shiftkey.dev/gpg.key" > /etc/yum.repos.d/shiftkey-packages.repo'

sudo apt update && sudo apt install github-desktop
```

## Firewall

```bash
sudo apt install ufw
sudo ufw enable
sudo ufw status
```

## アンチウイルスソフト

```bash
sudo apt install clamtk
```

- Settings: 全部ON
- Scheduler:
  - Scan: 13:10
  - Antivirus signatures: 13:00

## VMware Workstation 17 Player

- <https://www.vmware.com/go/getplayer-linux>の「Workstation 17 Player for Linux の試用」項目からダウンロード
