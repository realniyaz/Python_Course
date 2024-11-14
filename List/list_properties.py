"""
Description: List and its Properties
"""

# How to Build any list?
#Using the built function

lst = list()
empty_lst = list()
print(len(empty_lst))

#using the Square brackets []
list = []
empty_list = []
print(len(empty_list))

# Example of Lists

lang_list = ["English", "Mandarin", "Spanish" , "French", "Arabic" ]
print("The list of languages: ", lang_list)
print("The number of langauges: ",len(lang_list))

# Accessing list items using index values

print("The first langauge: ",lang_list[0]) # access using +ve index
print("The last language : ", lang_list[-1])

#Unpacking list items

numbers_list = [1,2,3,4,5,6,7,8,9,10]
one, two, three, four,five, six,seven,eight,nine, ten = numbers_list
print("One: ", one)

ONE, TWO, THREE, *rest = numbers_list
print("Rest: ",rest) # Concept of rest

# Slicing lists

fruits = ['Apple', 'Banana', 'Mango', 'Orange']
print(fruits[1:4])
print(fruits[0:])
print(fruits[:-1])
print(fruits[::2])

# Checking items in a list
apple_exits = 'Apple' in fruits
print(apple_exits)

lime_exists = 'Lime' in fruits
print(lime_exists) # using membership operators (in & not in)

# Adding items in a list
"""
We will use append method which will add the item
at the end of the list
"""
fruits.append("Lime")
print(fruits)
print(len(fruits))

"""
We will use insert method which will help us to add the item
at any index of the list.
"""

fruits.insert(2, "Grapes")
print(fruits)
print(len(fruits))

lang_list.insert(3,"Urdu")
print(lang_list)

# Removing any item form list

"""
There are 3 ways in general :
1) using .remove()
2) using .pop()
3) using del keyword
"""

lang_list.remove("Spanish") #takes the specified item name
print(lang_list)

lang_list.pop() #this deletes the last index thing
lang_list.pop(2) # specify the index to delete any item
print(lang_list)

del lang_list[0] #using the index place
del lang_list[0:1] #giving the range too
print(lang_list)

lang_list.clear() #empties the list
print(lang_list)

# Joining the lists

pos_numbers = [1,2,3,4,5]
zero = [0] 
neg_numbers = [-5,-4,-3,-2,-1]

Numbers = neg_numbers + zero + pos_numbers #using + operator
print(Numbers)

zero.extend(pos_numbers)
print(zero) # extend()

# Counting the items
print(fruits.count('Apple')) #returns how mnay times any items is present in the list

# reverse any list
fruits.reverse()
print(fruits)

# Sorting items in any list
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)
