
# 3.1
type(True)
# 3.3 Conditional execution
if x < 0 :
    pass
# you can use the pass statement, which does nothing.usually as a place holder for code you haven’t written yet
# 3.4 Alternative execution
if x%2 == 0 :
    print('x is even')
else :
    print('x is odd')
# 3.5 Chained conditionals
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

# 3.6 Nested conditionals
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

# 3.7 Catching exceptions using try and except
inp=input('Enter Fahrenheit Temperature:\n')
try:
    fahr=float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('please enter a number')

# 3.11 exercises
hours=input('enter hours\n')
try:
    hours=float(hours)
    rate=input('enter rate\n')
    rate=float(rate)
    if hours > 40:
        pay=(hours-40)*10*1.5+40*rate
        print(pay)
    else:
        pay=hours*rate
        print(pay)

except:
    print('Error, please enter numeric input')

score=input('enter a score')
try:
    score=float(score)
    if score >= 1.0:
        print('bad socre')
    elif score >=0.9:
        print('A')
    elif score >= 0.6:
        print('D')
    elif score > 0:
        print('F')
    else:
        print('bad score')
except:
    print('please enter a number')

# 4.3
smallest_so_far=None
#None is a reserved word
for the_num in [9,41,95,885,75,26]:
    if smallest_so_far is None:
        smallest_so_far=the_num
    if the_num<smallest_so_far:
        smallest_so_far=the_num
    print(smallest_so_far,the_num)

print('after',smallest_so_far)

# 4.4 Math functions
import math
print(math)
radians = 0.7
height = math.sin(radians)
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print(math.pi)
math.sin(radians)
math.sqrt(2)

# 4.5 Random numbers
import random
for i in range(10):
    x = random.random()
    print(x)
random.randint(5, 10)
random.choice(range(10))

# 4.6 Adding new functions
def myfunction_name():
    print('test')

# 4.7 Definitions and uses

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
repeat_lyrics()

# 4.8 Flow of execution

# 4.9 Parameters and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('Spam')
print_twice('Spam '*4)

# 4.10 Fruitful functions and void functions
result = print_twice('Bing')
print(result)

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
the
# addtwo function was called with 3 and 5 as arguments. Within the function, the
# parameters a and b were 3 and 5 respectively.
#
# 4.14
# 4.d
# 5.d
# 6.
def computepay(hours,rate):
    pay=hours*rate
    return pay

print(computepay(45,10))
# 7.
def computegrade(score):
    print('1',type(0.6))
    print('2',type(score))
    if score > 1:
        return print('bad socre,please enter a value between 0-1')
    elif score >= 0.9:
        return print('A')
    elif score >= 0.8:
        return print('B')
    elif score >= 0.6:
        return print('D')
    elif score >= 0:
        return print('F')
    else:
        return print('bad socre,please enter a value between 0-1')

score1 = input('Enter score:')

score1=float(score1)
#print(type(score1))
computegrade(score1)

# 5.2 The while statement
n=5
while n > 0:
    print(n)
    n=n-1
print('blastoff')

# 5.3 Infinite loops
while True:
    print(n)
    n=n-1
print('done')

while True:
    line = input('enter ')
    if line == 'done':
        break
    print(line)

print('done!')

# 5.4 Finishing iterations with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# 5.5 Definite loops using for
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# 5.6.1 Counting and summing loops
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
# 5.6.2 Maximum and minimum loops
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

smallest=None
print('before',smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest=itervar
    print('loop',itervar,smallest)
print('smallest',smallest)

def min(values):
    smallest=None
    for value in values:
        if value is None or value < smallest:
            smallest=value
    return smallest

# 5.9 exercises
total=0
count=0
while True:
    num=input('Enter a number: ')
    if num =='done':
        break
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue
    total=total+num
    count=count+1

print('tatol',total,'count',count,'average',total/count)

maximum=None
minimum=None
while True:
    num=input('Enter a number: ')
    if num =='done':
        break
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue
    if maximum  is None or maximum < num:
        maximum=num
    if minimum is None or minimum > num:
        minimum = num

print(maximum,minimum)



# 6.1 A string is a sequence

fruit='banana'
letter = fruit[1]

# 6.2 Getting the length of a string using len
len(fruit)
print(fruit[-1])
print(fruit[-2])



# 6.3 Traversal through a string with a loop
index=0
while index < len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1

index=len(fruit)-1
while index > 0:
    letter=fruit[index]
    print(letter,index)
    index=index-1

for letter in fruit:
    print(letter)
# 6.4 slicing strings
s='wuiqdhsADCdhsua'
print(s[0:4])
# the end is up to but not including
print(s[8:])
print(s[:3])
print(s[:])

# 6.5 Strings are immutable
greeting='hello lynn'
new_greeting='j'+greeting[1:]
print(new_greeting)

# 6.6 Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

def counter(string1,letter1):
    count=0
    for letter in string1:
        if letter==letter1:
            count=count+1
    return(count)

# 6.7 The in operator
'a' in 'banana'
'seed' in 'banana'

# 6.8 String comparison
if word == 'banana':
    print('identical')

word=input('enter:\n')
if word < 'banana':
    print('your word,',word, ', comes before banana')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# 6.9 String methods
stuff = 'ajdyagewag'
print(type(stuff))
print(dir(stuff))
help(stuff.capitalize)
print(stuff.capitalize())
print(stuff.upper())
print(stuff)
index=stuff.find('a')
print(index)
stuff.find('ag')
stuff.find('ag',5)

line = ' Here we go '
line.strip()
line = 'Have a nice day'
line.startwith('Have')
line.startwith('h')
line.lower().startwith('h')

word = 'banana'
word.count('a')

# 6.10 Parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
index1=data.find('@')
print(index1)
index2=data.find(' ',index1)
print(index2)
print(data[index1+1:index2])


# 6.11 Format operator
a1=54357468
s1='%d' % a1
s1.find('57')

camels = 42
'I have spotted %d camels.' % camels
'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

while True:
    line = input('> ')
    if line.startwith('#'):
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Exercise 5
str1='X-DSPAM-Confidence:0.8475'
index1=str1.find(':')
want=str1[index1+1:]
float1=float(want)
print(float1)

# Exercise 6:
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print(data.find('s'))
print(data.find(' '))
print(data.find(' ',5,21))

print(data.replace('a','AAA',2))
