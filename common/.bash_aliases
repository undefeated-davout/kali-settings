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

# シャットダウン関連
alias powerup='sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y'                               
~/data/kali-settings/common/login.sh

# TryHackMe
alias thm='sudo openvpn ~/data/keys/try_hack_me/tryhackme.ovpn'
