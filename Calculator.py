a = int(input("Enter First Number: "))
c = input("Enter Opearator: ")
if c in ('+', '-', '*', '/'):
  if c == '+':
    b = int(input("Enter Second Number: "))
    print(" ")
    print("Output:")
    print(a + b)
  elif (c == '-'):
    b = int(input("Enter Second Number: ")) 
    print(" ")
    print("Output:")
    print(a - b)
  elif (c == '*'):
    b = int(input("Enter Second Number: "))
    print(" ")
    print("Output:")
    print(a * b)
  elif c == '/':
    b = int(input("Enter Second Number: ")) 
    print(" ")
    print("Output:")
    print(a / b)
else:
  i=0
  d=0
  while(i==d):
    print(" ")
    print("Invalid Operator ! ")
    c = input("Enter Correct Opearator: ")
    if c in ('+', '-', '*', '/'):
      if c == '+':
        print(" ")
        b = int(input("Enter Second Number: "))
        print(" ")
        print("Output:")
        print(a + b)
        break
      elif (c == '-'):
        print(" ")
        b = int(input("Enter Second Number: "))
        print(" ")
        print("Output:")
        print(a - b)
        break
      elif (c == '*'):
        print(" ")
        b = int(input("Enter Second Number: ")) 
        print(" ")
        print("Output:")
        print(a * b)
        break
      elif c == '/':
        print(" ")
        b = int(input("Enter Second Number: "))
        print(" ")
        print("Output:")
        print(a / b)
        break