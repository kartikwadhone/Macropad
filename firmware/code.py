import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()


keyboard.col_pins = (
    board.D0,
    board.D1,
    board.D2,
)

keyboard.row_pins = (
    board.D3,
    board.D4,
    board.D5,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)


encoder_handler.pins = (
    (board.D6, board.D7, None),
)

encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),
    ),
]


keyboard.keymap = [
    [
        KC.COPY,   KC.PASTE, KC.CUT,
        KC.UNDO,   KC.REDO,  KC.PSCR,
        KC.MPRV,   KC.MPLY,  KC.MNXT,
    ]
]

if __name__ == "__main__":
    keyboard.go()
