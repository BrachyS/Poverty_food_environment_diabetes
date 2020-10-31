



IP= "1e1.4.5.6"
s4 = IP.split('.')
s6 = IP.split(':')
result = 'Neither'


if len(s4) == 4:
    i = 0
    result = 'IPv4'
    while i < len(s4) and result == 'IPv4':
        if s4[i][0] == '0' and len(s4[i]) != 1 or not s4[i].isdigit() or int(float(s4[i])) > 255:
            result = 'Neither'
        elif len(s4[i]) == 0 or len(s4[i]) > 3:
            result = 'Neither'
        else:
            result = 'IPv4'
        i += 1
        print(i, result)

print(result)



class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            total = 0
        else:
            total = max(nums)

            for j in range(len(nums) + 1):

                i = j
                m = 0
                while i + 2 < len(nums):

                    m = m + nums[i + 2]
                    i = i + 1

                    if m > total:
                        total = m

        return total




"""
Level 1 - Programming
----------------------
You are a data scientist working in the research labs for a large retail organization.
Currently you task involves mining for insights from Point-of-Sale systems which track item sales.
You have data stored as follows in JSON files (for simplicity think that you have one file 'pos_data.json')

Data Sample:

[{'item': 'Stella Extra Strong', 'price': '$23.45'},
{'item': 'Fosters Mild', 'price': '$12.99'},
{'item': 'Heineken', 'price': '$29.45'},
{'item': 'Stella Extra Strong', 'price': '$23.45'},
{'item': 'Stella Extra Strong', 'price': '$23.45'},
{'item': 'Fosters Mild', 'price': '$12.99'}]


Your tasks are as follows.
1. Write code to read in the JSON file to an appropriate python data structure (to solve Q2)
2. Use base python libraries (not pandas) to get the following insights
 -> Item name with top total sales
 -> Item name with least total sales
 -> Item name with the most units sold

Base Python libraries only (no 3rd party libraries e.g: numpy, pandas)

"""

# 1
import json

# with open('pos_data.json',r) as datafile:
#    sales = json.load(datafile)

sales = [{'item': 'Stella Extra Strong', 'price': '$23.45'},
         {'item': 'Fosters Mild', 'price': '$12.99'},
         {'item': 'Heineken', 'price': '$29.45'},
         {'item': 'Stella Extra Strong', 'price': '$23.45'},
         {'item': 'Stella Extra Strong', 'price': '$23.45'},
         {'item': 'Fosters Mild', 'price': '$12.99'}]

# print(sales)

# 2
# 1)

import collections
total_sales = collections.defaultdict(list)

for item in sales:
    total_sales[item['item']].append(float(item['price'].split('$')[1]))

print(total_sales)

keys = [i for i in total_sales.keys()]

values = [sum(i for i in count) for count in total_sales.values()]

units = [len(count) for count in total_sales.values()]

max_sale_item = keys[values.index(max(values))]
min_sale_item = keys[values.index(min(values))]
max_unit_item = keys[units.index(max(units))]


print('1):', max_sale_item)
print('2):', min_sale_item)
print('3):', max_unit_item)

# print(totals)

# len(counts)*(float(counts[0].split('$')[1]))
keys = total_sales.keys()

print(keys)

values = [i for i in total_sales.values()]
print(values)

item1 = len(values[0]) * (float(values[0][0].split('$')[1]))
item2 = len(values[1]) * (float(values[0][0].split('$')[1]))
item3 = len(values[2]) * (float(values[0][0].split('$')[1]))

max_sale = max(item1, item2, item3)
print(max_sale)


##
Student = collections.namedtuple('Student',['name','age','DOB'])

# Adding values
S = Student('Nandini','19','2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

##
my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

from collections import Counter
items = []
str_list = list(str)
c_str = collections.Counter(str_list)
for item in my_list:
    if collections.Counter(list(item)) == c_str:
        items.append(item)
print(items)


list(filter(lambda x: Counter(list(x)) == c_str, my_list))





##
my_list = [12, 65, 54, 39, 102,
                     339, 221, 50, 70]

data = list(filter(lambda x:x%13 == 0, my_list))



import json
hash = json.dumps(lst)
print(hash)
dict = {}
dict[hash] = 'converted'
print(dict)

##
import csv
with open('mydata.csv',r) as mydata:
    lines = csv.reader(mydata, delimiter=',')
    for line in lines:
        print(line)

# binary search
start, end = 1, n + 1
while start < end:
    mid = (start + end) // 2
    if isBadVersion(mid):
        end = mid
    else:
        start = mid + 1
return start

#
def sudoku2(grid):


    columns = [i for i in zip(*grid) ]
    boxes_dict = {}

    for i in range(9):
        for j in range(9):
            box_index = ((i//3)*3 + j//3)
            boxes_dict[box_index].append(grid[i][j])

    boxes = [v for v in boxes_dict.values()]

    all_data = grid + columns + boxes
    check_data = [i.append('.') for i in all_data]
    print(check_data)
    return False not in check_data


grid= [[".",".",".",".","2",".",".","9","."],
 [".",".",".",".","6",".",".",".","."],
 ["7","1",".",".","7","5",".",".","."],
 [".","7",".",".",".",".",".",".","."],
 [".",".",".",".","8","3",".",".","."],
 [".",".","8",".",".","7",".","6","."],
 [".",".",".",".",".","2",".",".","."],
 [".","1",".","2",".",".",".",".","."],
 [".","2",".",".","3",".",".",".","."]]



for i in range(9):
    for j in range(9):
        print((i//3)*3, j//3, (i//3)*3 + j//3)


# first duplicate
# better solution
def firstDuplicate(a):
    myset = set()  # Use set()
    for i in a:
        if i in myset:
            return i
        myset.add(i)  # Use add
    return -1

# mine:
def firstDuplicate(a):
    import collections
    count = collections.defaultdict(int)
    b = 0
    for i in a:
        count[i] +=1
        if count[i] > 1:
            return i
        else:
            b += 1
    if b == len(a):
        return -1


firstDuplicate(a)



# Rotate image
def rotateImage(a):
    n = len(a)

    newImage = []
    for i in range(n):
        newrow = []
        for j in list(range(n))[::-1]:


            newrow.append(a[j][i])
        print(newrow)
        newImage.append(newrow)
        #print(newImage)

    return newImage

a = [[1,2,3],
 [4,5,6],
 [7,8,9]]

rotateImage(a)



# Fractal tree
def tree(branchLen, t):
    if branchLen > 10:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)

from turtle import *
t= Turtle()
myWin = t.getscreen()
t.left(90)
t.color('green')


# Recursion Turtle
from turtle import *
myTurtle = Turtle()
myWin = myTurtle.getscreen()

def drawSpriral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpriral(myTurtle, lineLen-5)

drawSpriral(myTurtle, 100)
myWin.exitonclick()





# Recursion
# convert integer to string
def toStr(n,base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:

        rec = toStr(n//base, base) + convertString[n%base]

        return(rec)

toStr(769,10)




# Rotate Array

def rotate(nums,k):
    for i in range(k):
        num = nums.pop()

        nums.insert(0,num)

        print(nums)
    return nums


nums = [1,2]
k=3
rotate(nums,k)

def twoSum(nums, target):

twoSum(nums, target)



    def find_split(X, y):
        xy = collections.OrderedDict()
        for i in y:
            xy[i] = X[i]

    return X_split

X = np.array([3,1,4,5])
y = np.array([3,1,5,6])



def sumlist(nums):
    print(nums)
    while len(nums)> 1:
        newlist = []
        for i in range(len(nums)-1):
            newnum = nums[i] + nums[i+1]
            newlist.append(newnum)

        nums = newlist
        print(nums)

















import random
import math
mynums = list(range(1,16))
def guessnum(nums):
    nums.sort()
    rand = random.randint(1,nums[-1])
    guess = math.ceil((nums[-1]+nums[0])/2)
    print('rand:', rand, 'initial guess:', guess)
    while guess != rand:
        guess = math.ceil((nums[-1] + nums[0]) / 2)
        if guess < rand:
            nums = nums[nums.index(guess):]
            print('<rand guesses:',guess)
        elif guess > rand:
            nums = nums[:nums.index(guess)+1]
            print('>rand guesses:',guess)


    print('rand:',rand, 'final guess:',guess)
    return rand, guess

guessnum(mynums)


def multiples(N):
    numlist = []
    incr = 2

    while N != 1:
        if N%incr == 0:
            N = N//incr
            numlist.append(incr)
        else:
            incr+=1

    return numlist

# Binary search

# find a random number from [1,...15]


