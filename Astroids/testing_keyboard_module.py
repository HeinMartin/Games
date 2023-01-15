import keyboard

key_moves = {
        "a" : (0, -1),
        "d" : (0, 1),
        "s" : (1, 0),
        "w" : (-1, 0)
    }


for key, move in key_moves.items():
    def printy(key, move):
        print("key:", key, type(key))
        print("move:", move, type(move))
    
    # x = lambda: print(key, ",", key_moves[key])
    # x = lambda: printy(key, move)
    # x()

    keyboard.add_hotkey(str(key), lambda: print(str(key), ",", move))
    # printy(key, move)

# keyboard.add_hotkey("w", lambda: print("w", ",", key_moves["w"]))
# keyboard.add_hotkey("a", lambda: print("a", ",", key_moves["a"]))
# keyboard.add_hotkey("s", lambda: print("s", ",", key_moves["s"]))
# keyboard.add_hotkey("d", lambda: print("d", ",", key_moves["d"]))

while True:
    pass
