def area_of_triangle():
    a=int(input("enter the length of side a"))
    b=int(input("enter the length of side b"))
    c=int(input("enter the length of side c"))v
    print ("the area of triangle is : ",area)

def area_of_circle():
    r=int(input("enter the radius of circle:"))
    area=3.14*r**2
    print ("the area of circle is : ",area)

def area_of_rectangle():
    l=int(input("enter the length of rectangle"))
    w=int(input("enter the with of rectangle")) 
    area =l*w
    print ("the area of rectangle is : ",area)


#main program starts here
def menu():
    print("1. Area of Triangle")
    print("2. Area of circle ")
    print("3. Area of rectangle")
    print("4.Quit")
    choice=int(input("enter your choice "))
    if choice== 1:
        area_of_triangle()
    elif choice==2:
        area_of_circle()
    elif choice==3:
        area_of_rectangle()
    elif choice==4:
        print("good bye")
    else:
        print("Invalid chhoice")
        menu()


if __name__=="__main__":       #as if is a keyword requires space after 
     menu()                    #the file name is always saved by default name main

