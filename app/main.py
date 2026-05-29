import sys


def main():
    exit = False
    while not exit:
        sys.stdout.write("$ ")
        command = input()
        if command == 'exit':
            exit = True
        else:
            print(f'{command}: command not found')


if __name__ == "__main__":
    main()
