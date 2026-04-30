# Functions
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

result1 = add(10,5.3)
result2 = sub(3,5.3)

print("the reult is",result1)
print("the reult is",result2)

def areYouBrave():
    theTruth = input("If you say yes you are brave and if you say no, you might be brave too so are you brave, say the opposite")
    if theTruth == 'yes':
        print('you are BRAVEE!!!')
    else:
        print('You are a not brave')
        
# areYouBrave()

# Lists
nums=[1,2,3,44,5,6]

print(nums[0+3])
nums.append(232)
print(nums[6])

# Dictionaries
person = {
    "name":'Deepak',
    "age":17
}

print(person['name'],"Nalloru manushyanaan")


users =[{'name':"Manu",'age':13},{'name':"Anu",'age':33},{'name':"Sanu",'age':3},{'name':"Vinu",'age':5}]

for user in users:
    if user['age']>=18:
        print(user['name'],"is an adult")
    else:
        print(user['name'],"is a minor")

result3 = ()

# Comprehensions 
# List Comprehension
numbers = [1,2,3,4,5]
squares = [number*number for number in numbers]
print(squares)

# Dict Comprehension
numbers = [1,2,3,4,5]
numberDictionary = {number:(number*number) for number in numbers}
print(numberDictionary)

# Set Comprehension
numbers = [1,2,3,4,5,3,4,5,6,12,1,2]
uniqueValues = {number for number in numbers}
print(list(uniqueValues))