# App
alias bat='batcat'
alias co='code'

# コマンド
alias ll='exa -lahF --time-style=long-iso --no-permissions --no-user --icons'
alias lr='ll -s=modified -r'
alias catl='bat --decorations=never'
alias catdl='bat'
alias cat='catl --paging=never'
alias catd='catdl --paging=never'
alias sudo='sudo '
alias watch='watch -n1 -c -d '
alias man='env LANG=C man' # manコマンドは英語版を使用する
alias jman='env LANG=ja_JP.UTF-8 man'
alias hman='hman -H localhost:8050'

# シャットダウン関連
alias powerup='sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y && anyenv update && pip install -U pip'
~/data/repo/github.com/undefeated-davout/kali-settings/shell/login.sh

# TryHackMe
alias thm='sudo openvpn ~/data/keys/try_hack_me/tryhackme.ovpn'
