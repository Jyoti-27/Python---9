#!/usr/bin/env python
# coding: utf-8

# - Parameters and Arguments

# In[10]:


def power(base, exponent):  # Add your parameters here!
    result = base ** exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!


# In[4]:


- % d is used as a placeholder for numeric and decimal values
- The %d is for numbers


# In[21]:


FirstName="Jyoti"
LastName="Sabarad"
#Age = 35
print("%s is my First Name and %s is my Last Name." % (FirstName,LastName))


# In[11]:


firstName ="Jyoti"
lastName="Sabarad"
age=35
print("%s is my first name and %s is my last name"%(firstName,lastName))
print("My name is %s %s and my age is %d"%(firstName,lastName,age))


# - Arguments

# In[25]:


complex(real=3,imag=5)


# In[26]:


complex(5,3)


# In[28]:


complex(**{'imag': 5,'real': 3})


# In[55]:


def fullname(Firstname,Lastname):
    result = Firstname + Lastname 
    print(result)
Firstname = "JyotiSabarad"
Lastname = "Sabarad"
fullname(Firstname,Lastname)


# In[44]:


def Positional_Arguments(Place, Pincode):
    print("Place = {} and Pincode = {}".format(Place, Pincode))
Positional_Arguments("Sangli", 416416)
Positional_Arguments(416406, "Madhavnagar")
Positional_Arguments(Place = "Kolhapur", Pincode = 409410)   #Keyword Arguments


# In[43]:


def fullname(Firstname,Lastname):
    print("Firstname = {}, Lastname = {}".format(Firstname,Lastname))
    
fullname(Lastname = "Reddy", Firstname = "Aravind")


# In[56]:


def fullname(Firstname,Lastname):
    print("Firstname = {}, Lastname = {}".format(Firstname, Lastname))
    fullname(***{Lastname = "Sabarad",Firtname = "Jyoti"})


# In[46]:


def Positional_Arguments(Place, Pincode):
    print("Place = {} and Pincode = {}".format(Place, Pincode))
Positional_Arguments("Sangli", 416416)
Positional_Arguments(416406, "Madhavnagar")
Positional_Arguments(Place = "Kolhapur", Pincode = 409410)   #Keyword Arguments
Positional_Arguments(Place = "Kolhapur", Pincode = "409410")


# - Parameters with Default Argument

# In[50]:


def area_circle(r,pi=3.14):
    Area = pi*r**2
    print("Area of Circle is multiplying the square of the radius r = {} with pi = {} and the result = {}".format(r,pi,Area))
area_circle(5)


# In[51]:


def area_rectangle(l,w):
    Area = l*w
    print("Area of rectangle is multiplying the length l = {} with w = {} and the result = {}".format(l,w,Area))
area_rectangle(2,3)


# In[1]:



# Create a complex number 3-5i using keyword arguments and also positional arguments
a = 3
b = -5
complex(a,b)


# In[5]:


z1 = complex(3,-5)  # Positional
print(z1)
z2 = complex(imag = 4, real = 3) # Keywords Arguments
print(z2)


# In[6]:


z1.imag


# In[7]:


z1.imag()


# In[9]:


# Here every complex number has certain properties which are called as attributes,characteristicsor features.
# Few such attributes are more real and imag which talks about the real and imaginarypart of complex numbers.
print(z1.real)
print(z1.imag)


# In[10]:


# Using some in built function on this object.
# For every complex number,there exists it's conjugate,Conjugate of x+iy is x-iy
z1.conjugate()


# In[11]:


add(z1,z2)


# In[12]:


# Create a user defined functions to find a sum of complex number.
df additio(z1,z2):
return z1 + z2
addition(z1,z2)


# In[1]:


def addcomplex(n1,n2):
    z = n1 + n2
    print(z)
    addcomplex(n1,n2)


# In[27]:


z1 = 3 + 5j
z2 = 2 - 3j
def addi(a,b):
    return a + b
print("The addition result is")
addi(z1,z2)


# In[9]:


def sum_comp(num1,num2):
    return num1 + num2
z1 = complex(2,3)
z2 = complex(3,4) 
print(sum_comp(z1,z2))


# In[3]:


MovieName = "Bahubali"
Ntimes = 4
place = "Theatre"
print("I have watched {} movie{} times in {}" .format(MovieName,Ntimes,place))


# ### Placeholders in Python
# 
# What is a Placeholder?
# 
# - Intuitively, a placeholder is a pre-formatted container into which content can be placed.
# - If you have a variable in Python or any other type of data type, you can create a placeholder, usually in a print function to reserve a spot for this variable before explicitly saying what the variable is.
# 
# 

# In[5]:


name = "Jyoti"
age = 36
print("My name is {} and my age is {}".format(name,age))


# In[8]:


name = "Jyoti"
age = 36
print("My name is %s and my age is %d" %(name,age))


# In[ ]:




