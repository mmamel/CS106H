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
def bounds(a,b,):
    bool = True;
    while(bool == True):
        if a <= b:
            bool = False;
            return False;

def f(x):
    return x**2

def summation(a,b):
    sum = 0;
    for a in range(a,b+1,1):
        sum= sum+ f(x);


    return sum;
def TrapIntegration(a,b):
    sum=0
    N=int(input("number of trapezoids: "))
    width = (b-a)/N
    for i in range(a,b,1):
        sum=sum+width*.5*(f(i+(width*(i-1+a))))
    return sum
def RectIntegration(lower, upper):
    sum=0
    N=int(input("number of rectangles: "));
    width = (upper-lower)/N
    for i in range(lower, upper, 1):
        sum=sum+width*f(i+(width*(i-1+lower)));
    return sum;
def main():
    Sum_Int_Prompt = ["Summation", "Integration"]
    Sum_Int_Resp = prompt(2,Sum_Int_Prompt)
    if Sum_Int_Resp == 1:
        while valid_Bound_Sum == True:
            a = int(input("Enter lower: "))
            b = int(input("Enter upper: "))
            valid_Bound_Sum = bounds(a,b)
        sum = summation(a,b)
        print(sum);
    if Sum_Int_Resp == 2:
        Rect_Square_Prompt = ["Rectangle", "Trapezoid"]
        Rect_Square_Resp = promt(2, Rect_Square_Prompt)
        if Rect_Square_Resp == 1:
            while valid_Bound_Rect == True:
                a = int(input("Enter lower: "))
                b = int(input("Enter upper: "))
                valid_Bound_Rect = bounds(a,b)
            rect_Int=RectIntegration(a,b)
            print(rect_Int)
        if Rect_Square_Resp == 2:
            while valid_Bound_Trap == True:
                a = int(input("Enter lower: "))
                b = int(input("Enter upper: "))
                valid_Bound_Trap = bounds(a,b)
            trap_Int=TrapIntegration(a,b)
            print(trap_Int)

main();
