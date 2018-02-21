from math import pi
print(pi)

i=4.0

# Floating point data type
print(i)
j = 1
print (j)
text = "Hi"
print(text)
text[4]
type(text)

j=4.2
j.is_integer()


float_one=7.8
float_two=3.6
result = float_one - float_two
print(result)

number=7.8
number_dec=3.0
result = number + number_dec
print(result)

result = float_one - float_two
print(result)


dedication = "Your planet, love."
dedication[0:4]
dedication_supp = "Your reality, honey."
paean = dedication + " " + dedication_supp
print(paean)
paean.find("love")
paean[paean.find("love")]
paean[13]
paean_length=2


msg = "I wrote you a paean. It goes like {} Then it goes like {} It has {} lines.".format(dedication, dedication_supp, paean_length)
print(msg)


# F string
msg = f"I wrote you a paean. It goes like {dedication} Then it goes like {dedication_supp} It has {paean_length} lines."
print(msg)


# Boolean
reality = True
non_reality = False
print(reality and non_reality)
print(reality and not non_reality)


eric_height = 6.0
liana_height = 5.75
print(eric_height != liana_height)
print(eric_height == liana_height)
# double equal for truth, single for variable

x=1
y=1.0
print(x==y)
print(x is y)


# List
# Object Literal
l_one=[]

x=5
l_two=[1, 2.0, 'a', "abcd", True, x]
l_two[0]
l_two[3]

l_two.append(1)
print(l_two)

l_three=['a', 'b', 'c']

l_two.append(l_three)
l_two.extend(l_three)
print(l_two)

squares = []
for i in range(5):
    squares.append(i*i)
print(squares)

squares= [i*i for i in range(5)]
print(squares)


#Dictionaries
# key value pairs
d_one = {'key1':1, 'key2': 'moose', 'key3':4}
print(d_one)

d_one['key1']

d_one[6]='six'
d_one[6]
