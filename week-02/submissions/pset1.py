# Part A: Creating Lists

#Create list containing any 4 strings
aList= ['my', 'name', 'is', 'liana']

#Print 3rd item in List
print(aList[2])

#Print the 1st and 2nd item in the list
print(aList[0:2])

#Add a new string with text “last” to the end of the list and print the list
aList.append('last')
print(aList)

#Get the list length and print it.
len(aList)
print(len(aList))

#Replace the last item in the list with the string “new” and print
aList.remove('last')
aList.append('new')
print(aList)





#Part B: Strings

sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']

#Convert the list into a normal sentence
' '.join(sentence_words)
print(' '.join(sentence_words))

#Reverse the order of this list
' '.join(reversed(sentence_words))
print(' '.join(reversed(sentence_words)))

#Sort the list using the sort method
sentence_words.sort()
print(sentence_words.sort())

#Sort the list using the sorted method
sorted(sentence_words)
print(sorted(sentence_words))
    #Sort is more efficient than the sorted function, but only accepts lists, unlike sorted, which accepts any iterable.

#Extra credit: case-insensitive alphabet sort
 sw=sorted(sentence_words, key=lambda x:x.lower())
print(sw)





#Part C: Random function
from random import randint


# this returns random integer: 3 <= number <= 9

def lbnum(high_num, low_num=0):
    ret = randint(low_num, high_num)
    return ret

lbnum(9,3)

#test statements
assert(0 <= lbnum(900) <= 900)
assert(50 <= lbnum(900, low_num=50) <= 900)

#print random number less than 50 and greater than 10
print(lbnum(50,10))




#Part D: string formatting validation
#Define function
def besttit(num_place, tit1):
    ret = f'The number {num_place} bestseller today is: {tit1}.'.title()
    return ret

#Test out using number one best seller and big data title
besttit(1,'Big Data and Environmental Implications')





#Part E: Password validation function
#Code adapted from stackoverflow found here (https://stackoverflow.com/questions/45244854/identifying-special-characters-in-password-verification-in-python)
#Imported regular expressions, identified special characters, set conditions using function definitions for length, digits, capital letters, and special characters.

import re

specialcharacters = ['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 characters")
        elif len(password) > 14:
            print("Make sure your password is not longer than 14 characters")
        elif len([x for x in password if x.isdigit()]) < 2:
            print("Make sure your password has at least 2 digits.")
        elif re.search('[A-Z]',password) is None:
            print("Make sure your password has a capital letter in it")
        elif not any(c in specialcharacters for c in password):
            print("Make sure your password has a special character")
        else:
            print("Your password seems fine")
            break

validate()





#Part F: Exponention function
#Define function, set conditionals, and ran recursive

def nexp(n,m):
    if m == 0:
        return 1
    elif m==1:
        return n
    elif m > 1:
        return n * nexp(n, m - 1)

nexp(3,2)




#Extra Credit: Min and Max


#Define function for finding minimum, compare each number in list (candidate) to current min, return minimum
#Code found here: https://stackoverflow.com/questions/30623336/recursive-method-to-find-the-minimum-number-in-a-list-of-numbers

def find_min(l,current_minimum = None):
    if not l:
        return current_minimum
    candidate=l.pop()
    if current_minimum==None or candidate<current_minimum:
        return find_min(l,candidate)
    return find_min(l,current_minimum)

list2=[3, 6, 7, 1]

find_min(list2)



#Define function for finding maximum, compare each number in list (candidate) to current max, return max
#Code adapted from above source

def find_max(l, current_max = None):
    if not l:
        return current_max
    candidate = l.pop()
    if current_max==None or candidate>current_max:
        return find_max(l,candidate)
    return find_max(l, current_max)

list3=[3, 4, 5, 6, 7, 1]
find_max(list3)
