#!/usr/bin/env python3


COMMANDS = [
    'reserve',
    'release',
    'releaseall',
    'status',
]


PROMPT = 'tonbot> '

def reserve(params):
    pass

def release(params):
    pass

def releaseall(params):
    pass

def status(params):
    pass

def main():
    while True:
        print(PROMPT, end='')
        inp = input()

        tokens = inp.split(' ')

        if tokens[0] == 'exit' or tokens[0] == 'quit':
            return

        if tokens[0] not in COMMANDS:
            # TODO: stderr instead
            print(f'invalid command: {tokens[0]}')
        else:
            print(f'echo: {inp}')


if __name__ == '__main__':
    main()

