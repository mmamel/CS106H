def main():

    userInput = int(input("What integer number would you like to add? \n"))
    largest = userInput
    for x in range(1,5):
        userInput = int(input("What integer number would you like to add? \n"))
        if(largest<userInput):
            largest=userInput;
    print("The largest number is: ", largest);
   

main();
