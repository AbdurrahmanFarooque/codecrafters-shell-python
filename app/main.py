import sys


def main():
    # Assume input is correct
    def extractCommandAndText(userInput):
        wordList = userInput.split(maxsplit = 1)

        if len(wordList) == 1:
            command = wordList[0]
            text = ''
            return command, text
        
        command = wordList[0]
        text = wordList[1]
        return command, text
 
    builtins = [
        'exit',
        'echo',
        'type',
    ]

    exit = False
    while not exit:
        sys.stdout.write("$ ")
        userInput = input()

        command, text = extractCommandAndText(userInput)

        if command == 'exit':
            exit = True
        elif command == 'echo':  
            print(text)
        elif command == 'type':
            if text in builtins:
                print(f'{text} is a shell builtin')
            else:
                print(f'{text}: not found')
        else:
            print(f'{command}: command not found')



if __name__ == "__main__":
    main()
