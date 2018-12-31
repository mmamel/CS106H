#hangman program
def error_Handle_Word():
    bool = True;
    while bool == True:
        userInput = str(input("Enter a word: "))
        count = 0;
        special_count = 0;
        list(userInput)
        lenUserInput = len(userInput)
        #use of ascii to check if input contains only numbers
        for a in range(0, lenUserInput, 1):
            char=userInput[a];
            ascii=ord(char);
            if ascii <97 or ascii >122:
                count = count +1
            if ascii == 32:
                count = count -1
                special_count = special_count +1
        if count == 0 and special_count != lenUserInput:

            bool = False;
            return userInput

        else:
            print("Re-enter valid input");


def stringPrompt(string):
    arrayString = list(string);
    length= len(arrayString);
    dashArray = []
    for x in range(length):
        dashArray.append("_");
    return arrayString, dashArray
def charPrompt():
    bool = True;
    while bool == True:
        guess = str(input("enter a letter"))
        arrayGuess = list(guess)
        length = len(arrayGuess)
        if length == 1:
            ascii=ord(guess);
            if ascii>96 and ascii <123:
                bool = False

    return guess
def comparison(guess, arrayString, dashArray):
    length = len(arrayString)
    count = 0
    for x in range(length):
        if arrayString[x]==guess:
            dashArray[x] = guess;
            count=count+1
        #False -> did not find char
    if count == 0:
        return False
        #True -> found char
    if count >0:
        return True;
    return null
def usedGuess(charGuess):
    return null
def main():
    strike_counter = 0

    strike_display = []
    usedGuess = []
    string = error_Handle_Word();
    arrayString, dashArray = stringPrompt(string)
    win_length = len(arrayString)
    print(dashArray)
    #add a not winner thing
    print("___\n|\n|\n|")
    while strike_counter < 6 and arrayString != dashArray:
        if strike_counter == 1:
            print("___\n|  O\n|\n|");
        elif strike_counter == 2:
            print("___\n|  O\n|  |\n|")
        elif strike_counter == 3:
            print("___\n|  O\n| \|\n|")
        elif strike_counter == 4:
            print("___\n|  O\n| \|/\n|")
        elif strike_counter == 5:
            print("___\n|  O\n| \|/\n| /")

        guess = charPrompt()
        usedGuess.append(guess)
        strike = comparison(guess, arrayString, dashArray)
        if strike == False:
            strike_counter = strike_counter+1
            strike_display.append("X")
        print("Used letters: ", usedGuess)
        print("Strikes: ", strike_display)
        print(dashArray)
    if strike_counter == 6:
        print("___\n|  O\n| \|/\n| /\\")
        print("You lose")
    elif arrayString == dashArray:
        print("You win")
        #if strike == 6 you lose else you are a winner

main();
