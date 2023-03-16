# App
alias bat='batcat'
alias co='code'

# コマンド
alias vi='vim '
alias globalip='echo "v4: "; curl ipecho.net/plain; echo "\n\nv6: "; curl ifconfig.io'
alias exa-base='exa --time-style=long-iso --icons'
alias ll='exa-base -lahF --no-permissions --no-user'
alias lt='ll -T --ignore-glob=".git"'
alias lr='ll -s=modified -r'
alias llh='ls -lahF'
alias lf='exa-base -lahFg'
alias lp='ls -aF | xargs stat -c "%a %n"'
alias catl='bat --decorations=never'
alias catdl='bat'
alias cat='catl --paging=never'
alias catd='catdl --paging=never'
alias sudo='sudo '
alias watch='watch -n1 -c -d '
alias man='env LANG=C man' # manコマンドは英語版を使用する
alias jman='env LANG=ja_JP.UTF-8 man'
alias hman='hman -H localhost:8050'
alias jtrans='trans -b en:ja'

alias auto-update='sudo apt update && sudo apt autoclean -y && anyenv update && pip install -U pip'
alias auto-upgrade='sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y && anyenv update && pip install -U pip && sh ~/data/repo/github.com/undefeated-davout/kali-settings/scripts/chrome_dark_mode.sh'

# TryHackMe
alias thm='sudo openvpn ~/data/keys/try_hack_me/tryhackme.ovpn'
alias htb='sudo openvpn ~/data/keys/hack_the_box/hack_the_box.ovpn'
