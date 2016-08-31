#Suppose you have a list of words and 
#you want to sort them from longest to shortest:

txt = 'but soft what light in yonder window breaks'

words = txt.split()

t = list()


for word in words:
    t.append((len(word), word)) #this builds a list of tuples. Each tuple is a word preceded by its length e.g. (3, 'but')
    
print t                         #this is what our list of tuples looks like prior to sorting.    

t.sort(reverse=True)            #the sort() method on a list sorts that list into ascending order, but since we uesd the
                                #arguement reverse=True, it's sorted in decreasing order. Sort compared the first element 
                                #of the tuple (which is the 3 in the tuple (3, 'but')) -- it only considers the second
                                #element to break ties that may occur when comparing the first elements. 
print t

res = list()                    #this creates another list. 
for length, word in t:          #this loop traverses the list of tuples. 
    res.append(word)            #we append each word to our list.
    
print res                       #the result is a list, sorted in descending word length order. 

#the above is an example of the (DSU) Decorate, Sory and Undecorate pattern. 
#Decorate a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence
#Sort the list of tuples using the sort built in method
#Undecorate by extracting the sorted elements of the sequence. 

#Tuple assignment

#You can have a tuple on the left side of an assignment statement, allowing you to assign more than one variable
#at a time when the left side is a sequence. 

#Here is a two element list. 

m = ['have', 'fun']

#We assign the first and second elements to the variables x and y.

x, y = m

print x
print y

#Essentially x = m[0] and y = m[1]
#We can swap values in a single statement 

x, y = y, x 

print x
print y

#both sides of this statement are tuples, but the left side is a tuple of variables
#the right side is a tuple of expressions. Each value on the right side is assigned 
#to its respective variable on the left side.The expressions on the right are evaluated first. 
#Note, the number of variables on the right side must be the same on the left. 

#the right side can be any kind of sequesnce.

addr = 'monty@python.org'
uname, domain = addr.split('@') #the right side is a list with two elements, monty and python.org

print uname
print domain

#Dictionaries and Tuples

#Dictionaries have a method called items that returns a list of tuples, 
#where each tuple is a key value pair.