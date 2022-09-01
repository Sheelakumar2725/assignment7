print("1.addition")
print("2.subtraction")
print("3.multipilication")
print("4.division")
x=int(input(print("enter your choice:"))) 
match x:
    case 1:
        print("enter two numbers:")
        a,b=int(input()),int(input())
        c=a+b
        print("sum is:",c)
    case 2:
        print("enter two numbers:")
        a,b=int(input()),int(input())
        c=a-b
        print("difference is:",c)
    case 3:
        print("enter two numbers:")
        a,b=int(input()),int(input())
        c=a*b
        print("product is:",c)
    case 4:
        print("enter two numbers:")
        a,b=int(input()),int(input())
        c=a/b
        print("divsion is:",c)
    case _:
        print("invalid choice")
print()      
      
      
      
   
      
      
      
   
      
      
      
   
      
      
      
 
