# Basic keyword argument

def simple_interest(p:float,t:float,r:float):
    si = (p*r*t)/100
    print("simple interest: ",si)
    
simple_interest(p=10000,t=2.5,r=3.5)

#student information

def student_info(name,age,city):
    print("name: ",name)
    print("age: ",age)
    print("city: ",city)
    
student_info(age=18,city="rajkot",name="vivek")

#mixing positional and keyword

def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    
display(1,c=3,b=2)

