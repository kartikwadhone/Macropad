import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# Replace with actual row/column pins
keyboard.row_pins = ()
keyboard.col_pins = ()

keyboard.keymap = [
    [
        KC.COPY,
        KC.PASTE,
        KC.CUT,
        KC.UNDO,
        KC.REDO,
        KC.PSCR,
        KC.MPRV,
        KC.MPLY,
        KC.MNXT,
    ]
]

if __name__ == "__main__":
    keyboard.go()
