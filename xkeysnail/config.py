# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# キー長押し判定時間
define_timeout(1)

# 単体キー自体を変更する
define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
})

# デバイス別：ThinkPadキーボード
define_conditional_modmap(lambda wm_class, device_name: device_name.startswith("AT Translated Set 2 keyboard"), {
    Key.CAPSLOCK: Key.LEFT_CTRL,
    # ATL、Superキーは位置を入れ替える
    Key.LEFT_META: Key.LEFT_ALT,
    Key.LEFT_ALT: Key.LEFT_META,
    Key.RIGHT_ALT: Key.RIGHT_META,
    # スクリーンショット誤操作防止のためALTに変更
    Key.SYSRQ: Key.RIGHT_ALT,
})

# 単押し／長押し
define_multipurpose_modmap({
    # 単押し時は、i3で入力モード変更のショートカットに割り当てている変換キーにリマップしている
    # 左Cmdキーは既存のModキー設定が反応するソフトがあるので右に置換
    Key.LEFT_META: [Key.MUHENKAN, Key.RIGHT_META],
    Key.RIGHT_META: [Key.HENKAN, Key.RIGHT_SHIFT],
})

# ブラウザ
define_keymap(re.compile("Google-chrome|Brave-browser|Firefox"), {
    K("Super-LEFT"): K("LM-LEFT"),
    K("Super-RIGHT"): K("LM-RIGHT"),
    K("Super-LEFT_BRACE"): K("LM-LEFT"),
    K("Super-RIGHT_BRACE"): K("LM-RIGHT"),
    K("Super-y"): K("C-h"),
    K("M-up"): K("page_up"),
    K("M-down"): K("page_down"),
    K("C-r"): K("Shift-LM-r"),
}, "browser")

# ターミナル
define_keymap(re.compile("qterminal|Gnome-terminal"), {
    K("Super-c"): K("Shift-C-c"),
    K("Super-f"): K("Shift-C-f"),
    K("Super-n"): K("Shift-C-n"),
    K("Super-t"): K("Shift-C-t"),
    K("Super-v"): K("C-v"),
    K("Super-q"): K("C-q"),
    K("C-p"): with_mark(K("up")),
    K("Super-Enter"): K("F11"),
}, "terminal")

# 共通設定（ターミナル以外）
define_keymap(lambda wm_class: wm_class not in ("qterminal|Gnome-terminal"), {
    # Emacs風
    # 方向キー
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    # 先頭、末尾移動
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    # 削除
    K("C-h"): with_mark(K("backspace")),
    K("C-d"): [K("delete"), set_mark(False)],
    # ヤンク
    K("C-y"): [K("C-v"), set_mark(False)],
    # カーソル以降カット
    K("C-k"): [K("Shift-end"), K("delete"), set_mark(False)],
    # カーソル以前カット
    K("C-u"): [K("Shift-home"), K("C-x"), set_mark(False)],
}, "common settings except terminal")

# 共通設定
define_keymap(lambda wm_class: wm_class not in (""), {
    # Mac風
    K("Super-down"): K("Enter"),
    K("Super-up"): K("backspace"),
    K("Super-backspace"): K("delete"),
    K("Super-Enter"): K("C-Enter"),
    K("Super-Slash"): K("C-Slash"),
    K("Super-a"): K("C-a"),
    K("Super-b"): K("C-b"),
    K("Super-c"): K("C-c"),
    K("Super-d"): K("C-d"),
    K("Super-e"): K("C-e"),
    K("Super-f"): K("C-f"),
    K("Super-g"): K("C-g"),
    K("Super-h"): K("C-h"),
    K("Super-i"): K("C-i"),
    K("Super-j"): K("C-j"),
    K("Super-k"): K("C-k"),
    K("Super-l"): K("C-l"),
    K("Super-m"): K("C-m"),
    K("Super-n"): K("C-n"),
    K("Super-o"): K("C-o"),
    K("Super-p"): K("C-p"),
    K("Super-q"): K("C-q"),
    K("Super-r"): K("C-r"),
    K("Super-s"): K("C-s"),
    K("Super-t"): K("C-t"),
    K("Super-u"): K("C-u"),
    K("Super-v"): K("C-v"),
    K("Super-v"): K("C-v"),
    K("Super-w"): K("C-w"),
    K("Super-x"): K("C-x"),
    K("Super-y"): K("C-y"),
    K("Super-z"): K("C-z"),
    K("Shift-Super-Enter"): K("Shift-C-Enter"),
    K("Shift-Super-a"): K("Shift-C-a"),
    K("Shift-Super-b"): K("Shift-C-b"),
    K("Shift-Super-c"): K("Shift-C-c"),
    K("Shift-Super-d"): K("Shift-C-d"),
    K("Shift-Super-e"): K("Shift-C-e"),
    K("Shift-Super-f"): K("Shift-C-f"),
    K("Shift-Super-g"): K("Shift-C-g"),
    K("Shift-Super-h"): K("Shift-C-h"),
    K("Shift-Super-i"): K("Shift-C-i"),
    K("Shift-Super-j"): K("Shift-C-j"),
    K("Shift-Super-k"): K("Shift-C-k"),
    K("Shift-Super-l"): K("Shift-C-l"),
    K("Shift-Super-m"): K("Shift-C-m"),
    K("Shift-Super-n"): K("Shift-C-n"),
    K("Shift-Super-o"): K("Shift-C-o"),
    K("Shift-Super-p"): K("Shift-C-p"),
    K("Shift-Super-q"): K("Shift-C-q"),
    K("Shift-Super-r"): K("Shift-C-r"),
    K("Shift-Super-s"): K("Shift-C-s"),
    K("Shift-Super-t"): K("Shift-C-t"),
    K("Shift-Super-u"): K("Shift-C-u"),
    K("Shift-Super-v"): K("Shift-LM-v"), # Clipman用にaltに割り当てる
    K("Shift-Super-w"): K("Shift-C-w"),
    K("Shift-Super-x"): K("Shift-C-x"),
    K("Shift-Super-y"): K("Shift-C-y"),
    K("Shift-Super-z"): K("Shift-C-z"),
}, "common settings for all")
