def area_circle(r):
    return (3.14*r**2)

def area_rectangle(l,b):
    area= lxb
    return area

def area_triangle(s1,s2,s3):
    s=(s1+s2+s3)/2
    area = (s*(s-s1)*(s-s2)*(s-s3))
    return area


if __name__== "__main__":
    print("enter your choice")
    print("1. Area of Triangle")
    print("2. Area of circle ")
    print("3. Area of rectangle")
    print("4.Quit")
    choice=int(input("enter your choice "))
    if choice== 1:
        s1=int(input("enter the side"))
        s2=int(input("enter the side"))
        s3=int(input("enter the side"))
        print(area_triangle(s1,s2,s3))
    elif choice==2:
        r=int(input("enter the radius"))
        print(area_circle(r))
    elif choice==3:
        l=int(input("enter the length"))
        b=int(input("enter the width"))
        print(area_rectangle(l,b))
    elif choice==4:
        print("good bye")
    else:
        print("Invalid chhoice")
    
    
