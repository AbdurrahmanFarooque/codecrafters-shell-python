import sys


def main():
    # Assume input is correct
    def extractCommandAndText(userInput):
        wordList = userInput.split()
        command = wordList[0]
        text = ' '.join(wordList[1: ])
        return command, text
 
    exit = False
    while not exit:
        sys.stdout.write("$ ")
        userInput = input()

        command, text = extractCommandAndText(userInput)

        if command == 'exit':
            exit = True
        elif command == 'echo':  
            print(text)
        else:
            print(f'{command}: command not found')



if __name__ == "__main__":
    main()
