<<<<<<< HEAD

class Dog:
    kind = 'canine'
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):

# In[28]:
​
dog1 = Dog("fido")

# In[29]:

dog2 = Dog("sparky")

# In[30]:

dog1.kind

=======
​
# coding: utf-8
​
# In[27]:
​
class Dog:
    kind = 'canine'
    tricks = []             # mistaken use of a class variable
​
    def __init__(self, name):
        self.name = name
​
    def add_trick(self, trick):
        self.tricks.append(trick)
​
​
# In[28]:
​
dog1 = Dog("fido")
​
​
# In[29]:
​
dog2 = Dog("sparky")
​
​
# In[30]:
​
dog1.kind
​
​
>>>>>>> master
# In[31]:
​
dog2.kind
​
​
# In[32]:
​
dog1.add_trick('sit')
​
​
# In[33]:
​
dog2.tricks
​
​
# In[ ]:
​
​
​
​
# In[16]:
​
# Should be written as
class Dog:
    kind = 'canine'
​
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
​
    def add_trick(self, trick):
        self.tricks.append(trick)
​
​
# In[17]:
​
d = Dog('Cujo')
​
​
# In[18]:
​
d.add_trick("Roll Over")
​
​
# In[19]:
​
d2 = Dog('Spot')
​
​
# In[20]:
​
d2.tricks
​
​
# In[22]:
​
d.tricks
​
​
# In[23]:
​
d.kind = "Doggy"
​
​
# In[24]:
​
d2.kind
​
​
# In[25]:
​
d.kind
​
​
# In[26]:
​
d2.kind
​
​
# In[ ]:
​
​
​
Add Comment Collapse
dadsaster [7:16 PM]
added a Python snippet: -args and --kwargs.py
​
# coding: utf-8
​
# In[44]:
​
def test_var_args(args):
#     print ("first normal arg:", f_arg)
    for arg in args:
        print ("another arg through *args:", arg)
​
​
# In[45]:
​
test_var_args('yasoob', 'python','eggs','test')
​
​
# In[ ]:
​
​
​
​
# In[46]:
​
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("{} == {}".format(key, value))
​
​
​
# In[47]:
​
greet_me(name="yasoob")
​
​
# In[48]:
​
def test_args_kwargs(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)
​
​
# In[49]:
​
args = ("two", 3, 5)
​
​
# In[51]:
​
test_args_kwargs(*args)
​
​
# In[52]:
​
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
​
​
# In[53]:
​
test_args_kwargs(**kwargs)
​
​
# In[54]:
​
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
​
​
# In[55]:
​
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
​
​
# In[56]:
​
print("Hello, World", end="!")
print("Somthing")
​
​
# In[57]:
​
l = [1, 2, 3, 4]
​
​
# In[58]:
​
del l[2]
​
​
# In[59]:
​
l
​
​
# In[60]:
​
l.remove(1)
​
​
# In[61]:
​
l
​
​
# In[62]:
​
2 in l
​
​
# In[64]:
​
type((1))
​
​
# In[65]:
​
type((1,))
​
​
# In[66]:
​
type(())
​
​
# In[67]:
​
t = (1, 2, 3)
​
​
# In[68]:
​
a, b, c = t
​
​
# In[69]:
​
a
​
​
# In[70]:
​
b
​
​
# In[71]:
​
c
​
​
# In[72]:
​
t
​
​
# In[73]:
​
t[1:]
​
​
# In[74]:
​
t
​
​
# In[ ]:
​
​
​
