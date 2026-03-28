# Basic positional arguments

def add(a,b):
    return a + b
result = add(2,5)
print("sum = ", result)

# check number positive negative or zero

def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
        
check_value(0)
check_value(90)
check_value(-15)

#student information
def student_info(name,roll,marks):
    print("name: ", name)
    print("roll: ", roll)
    print("marks: ", marks)
    
student_info("vivek","03","95")

#simple interest

def simple_interest(p,r,t):
    si=(p*r*t)/100
    print("simple interest",si)

simple_interest(10000,2,2)
simple_interest(50000,12,3)

#area of circle

def ar_circle(r):
    a_circle  = 3.14*r*r
    print("area of circle :",a_circle)
    
ar_circle(1.5)
ar_circle(4)

#odd or even

def odd_even(no):
    if(no % 2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
        
odd_even(50)
odd_even(15)

#arithmetic operation substraction
    #multiplication and division
    
def addition(a,b):
    add = a + b 
    print("addition of two values",add)
    
addition(50,10.5)
addition(100,200)