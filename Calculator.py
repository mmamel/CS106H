def main():
    def addition(x, y):
        return x+y
    def subtraction(x, y):
        return x-y
    def multiplication(x,y):
        return x*y
    def division(x,y):
        return x/y
    def exponential(x,y):
        return x**y
    #Use while loop to catch bad inputs that are not 1 or 2
    first = True;

    while(first == True):
        second = True;
        third = True;
        fourth = True;

        mode = input("Enter 1 for programmer mode, 2 for scientific mode, and 3 to quit\n");
#programmer mode convertes decimal to binary
#second while loop to catch negative numbers
        while(second == True):

            if mode == "1":
      #break first error catching loop

                binary = input("Enter a postive decimal number to convert into binary\n");
                if binary[0] == "-":
                    print("Please enter a positive decimal number");
                else:
                    second = False;
            #convert string to int to run calculations
                    iBinary=int(binary);
            #store remainders
            #does array deallocate itself?
                    remainArray=[];
                    while(third == True):

                        remainder = iBinary%2

                        if remainder != 0:
                    #remember to reverse order of array
                            remainArray.append(1);
                        elif remainder == 0:
                            remainArray.append(0);
                            #temparary value to run remainder calculations
                        temp = int(iBinary / 2);
                            #keeps data within scope
                        iBinary = temp;

                #checks for last digit
                        if iBinary == 0:
                            third = False;
                    print("Decimal: ",binary)

                    upperbound = int(len(remainArray));
                    #if number is a power of 2
                    if upperbound == remainArray.count(0):
                        remainArray.append(1);
                        remainArray.pop(0);
                        for x in reversed(remainArray):
                            print(x, end='');
                    else:
                        for x in reversed(remainArray):
                            print(x, end='');
                    print('\n')


                    first = True;

            elif mode == "2":
                while(fourth == True):
                #errorcheck for correct input
                    operation = input("Enter an operation: +, -, *, / or  **\n");
                    if operation == "+" or operation =="-" or operation =="*" or operation =="/" or operation == "**":
                        calcArray = [];
                        calcArray.append(operation);
                        numOne = int(input("Enter the first number\n"));
                        numTwo = int(input("Enter second number\n"));
                    #could just reorder append but wanted to try insert function
                        calcArray.insert(0, numOne);
                        calcArray.append(numTwo);
                        for x in range(3):
                            print(calcArray[x], end='');
                        print("=", end='');
                        if operation == "+":
                            print(addition(calcArray[0], calcArray[2]));
                        elif operation == "-":
                            print(subtraction(calcArray[0], calcArray[2]));
                        elif operation == "*":
                            print(multiplication(calcArray[0], calcArray[2]));
                        elif operation == "/":
                            print(division(calcArray[0], calcArray[2]));
                        elif operation == "**":
                            print(exponential(calcArray[0], calcArray[2]));
                        rerun=input("Enter 1 to run another calculation and 2 to return to main menu")

                        if rerun == "2":
                            fourth = False;

                    else:
                        print("Enter a valid operation");
                second = False;



            elif mode == "3":
                return 0;
            else:
                print("Re-enter input")
                second = False;




main();
