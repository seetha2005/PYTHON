def sq():
    side=int(input("Enter the side:"))
    print("Area of square:",side*side)
def rect(l,b):
    print("Area of rectangle:",l*b)
def tri():
    b=int(input("Enter the base:"))
    h=int(input("Enter the height:"))
    return 0.5*b*h
def cir(r):
     return 3.14*r*r
print("___MENU___")
print("1.SQUARE")
print("2.RECTANGLE")
print("3.TRIANGLE")
print("4.CIRCLE")
ch=int(input("Enter your choice:"))
if(ch==1):
    sq()
elif(ch==2):
      l=int(input("Enter the length:"))
      b=int(input("Enter the breadth:"))
      rect(l,b)
elif(ch==3):
    a=tri()
    print("Area of triangle;",a)
elif(ch==4):
    r=int(input("Enter the radius:"))
    b=cir(r)
      