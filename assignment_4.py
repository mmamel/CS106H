# takes in string to check if all characters are numbers using ascci
# returns bool to break out of loop of user input
def numCheck(user_in):
    bool = True;
    while bool == True:
        list(user_in);
        len_user_in = len(user_in);
        count = 0;
        #use of ascii to check if input contains only numbers
        for a in range(0, len_user_in, 1):
            char=user_in[a];
            ascii=ord(char);
            if ascii <48 or ascii >57:
                count = count +1
        if count == 0:
            bool = False

            return False
        else:
            print("Re-enter valid input");
            bool = False
            return True
#different from numCheck because this checks for negative values
#handles error within function
def sub_interval():
    bool = True;
    while bool == True:
        user_in = input("Enter number of sub-intervals: ")
        list(user_in);
        len_user_in = len(user_in);
        count = 0;
        #use of ascii to check if input contains only numbers
        for a in range(0, len_user_in, 1):
            char=user_in[a];
            ascii=ord(char);
            if ascii <48 or ascii >57:
                count = count +1
        if count == 0:
            bool = False

            return user_in
        else:
            print("Re-enter valid input");


        if user_in[0] == "-":
            print("Please enter a positive decimal number");
#generates prompts for user input and handles bad input
def prompt(x, array):
    bool = True;


    count = 0;
    while(bool == True):
        for y in range(0, x, 1):
            print(y+1,"=",array[y])
        response = str(input());
        for z in range(1, x+1, 1):
            stringConvertor = str(z);
            if stringConvertor == response:
                bool = False;
                return response;
        print("Re-enter input");
def bounds(a,b):
    if a <= b:

        return False;
    else:
        return True

def f(x):
    return x**2

def summation(a,b):
    int(a)
    int(b)
    sum = 0;
    for a in range(a,b+1,1):
        sum= sum+ f(a);


    return sum;
def TrapIntegration(a,b,n):
    sum=0
    width = (b-a)/n
    for i in range(a,b,1):
        sum=sum+width*.5*(f(a+(width*(i-a))))
    return sum
def RectIntegration(lower, upper, n):
    sum=0
    width = (upper-lower)/n
    for i in range(lower, upper, 1):
        sum=sum+width*f(lower+(width*(i-lower)));
    return sum;
def main():
    Sum_Int_Prompt = ["Summation", "Integration"]
    Sum_Int_Resp = prompt(2,Sum_Int_Prompt)
    valid_Bound_Sum = True;
    valid_Bound_Rect = True;
    valid_Bound_Trap = True;
    Rect_Square_Resp = True;

    if Sum_Int_Resp == "1":
        while valid_Bound_Sum == True:
            #reusable while loop to ensure bounds for calculations are integers
            lower_bound = True;
            upper_bound = True;
            while lower_bound == True:
                a = input("Enter lower: ")
                lower_bound = numCheck(a);
            while upper_bound == True:
                b = input("Enter upper: ")
                upper_bound = numCheck(b);
            #need to reconvert to int to run comparisons
            #first inputed as string to run error checking
            new_a=int(a)
            new_b=int(b)
            valid_Bound_Sum = bounds(new_a,new_b)
        sum = summation(new_a,new_b)
        print(sum);
    if Sum_Int_Resp == "2":
        Rect_Square_Prompt = ["Rectangle", "Trapezoid"]
        Rect_Square_Resp = prompt(2, Rect_Square_Prompt)
        if Rect_Square_Resp == "1":
            #allows user to reinput each prompt if there is bad input
            while valid_Bound_Rect == True:
                lower_bound = True;
                upper_bound = True;
                while lower_bound == True:
                    a = input("Enter lower: ")
                    lower_bound = numCheck(a)
                while upper_bound == True:
                    b = input("Enter upper: ")
                    upper_bound=numCheck(b);
                valid_Bound_Rect = bounds(a,b)
            n = sub_interval()
            new_n = int(n)
            new_a=int(a)
            new_b=int(b)
            rect_Int=RectIntegration(new_a,new_b,new_n)
            print(rect_Int)
        if Rect_Square_Resp == "2":
            while valid_Bound_Trap == True:
                lower_bound = True;
                upper_bound = True;
                while lower_bound == True:
                    a = input("Enter lower: ")
                    lower_bound = numCheck(a)
                while upper_bound == True:
                    b = input("Enter upper: ")
                    upper_bound=numCheck(b);
                valid_Bound_Trap = bounds(a,b)
            n = sub_interval();
            new_n = int(n)
            new_a=int(a)
            new_b=int(b)
            trap_Int=TrapIntegration(new_a,new_b,new_n)
            print(trap_Int)

main();
