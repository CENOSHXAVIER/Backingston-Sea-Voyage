# Arithmetics
a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Logical Operators
a = True
b = False

print(a and b)
print(a or b)
print(not b)

# condition
userName = 'deepak'
password = 'deepakIsAwesome'

if (userName == 'deepak' and password == 'deepakIsAwesome'):
    print('Authorized')
else:
    print('Wrong username or password. Please check and try again')

# condition with logical operator
if not(userName):
    print('Username is required')
else: 
    print('Authorized again')
    

# Loops - for & while
for i in range(10):
    print(i+1)
    
i=15
while(i>5):
    print('i love ronaldo')
    i-=1

age = int(input('What is your age?'))
parentConsent = False
if age>=18:
    print("Eligible to drink")
elif(age<18 and parentConsent): 
    print("Eligible for drink")
else:
    print("You are under-age poy vallathum eduth vach padikk mooneee")