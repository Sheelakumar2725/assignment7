print("1.isosceles triangle")
print("2.right angled triangle")
print("3.equilateral triangle")
print("4.exit")
x=int(input(print("enter your choice:"))) 
match x:
    case 1:
       print("enter three lengths of a triangle")
       a,b,c=int(input()),int(input()),int(input())
       if a==b or b==c or c==a:
           print("isosceles triangle")
       else:
           print("false")
    case 2:
       print("enter three lengths of a triangle")
       a,b,c=int(input()),int(input()),int(input())
       if c**2==a**2+b**2:
           print("right angled triangle")
       else:
           print("false")
    case 3:
       print("enter three lengths of a triangle")
       a,b,c=int(input()),int(input()),int(input())
       if a==b and b==c:
           print("equilateral triangle")
       else:
           print("false")
    case 4:
       print("exit")
       
      
      
   
      
      
      
 
