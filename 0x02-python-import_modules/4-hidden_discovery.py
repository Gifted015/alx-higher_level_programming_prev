#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hid = dir(hidden_4)
    for a in hid:
        if a[:2] != "__":
            print(a)
