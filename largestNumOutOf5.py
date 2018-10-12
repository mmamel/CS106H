def main():


    numList = list();

    for x in range(5):
        userInput = int(input("What integer number would you like to add? \n"))


        numList.append(userInput);

    largest = numList[1];
    for x in range(4):

        if(numList[x]<numList[x+1]):
            largest = numList[x+1];
    print("The largest number is: ", largest);

main();
