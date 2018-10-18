def main():
  capNum = int(input("Enter a number \n"));
  print("The prime numbers are: ");
  for x in range (1, capNum, 1):

    if(x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0):
      print(x);
  if(capNum%2 != 0 and capNum%3 != 0 and capNum%5 != 0 and capNum%7 != 0):
      print(capNum);



main();
