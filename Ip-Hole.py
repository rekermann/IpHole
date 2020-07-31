#!/usr/bin/env python3
import funcs
import menu


def main():
    v = funcs.setup()
    try:
        while True:
            menu.mainMenu(v)
            pass
    except KeyboardInterrupt:
        funcs.interrupt(v)


if __name__ == '__main__':
    main()

