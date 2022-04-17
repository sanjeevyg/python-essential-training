
x = 99
y = 99

print('This is a test {}'.format(y))

if(x > y):
    z = 199
    print('x > y : x is {x} and y is {y}.')
elif(x == y):
    print('x is equal to y.')
else:
    print('x is less than y.')
    
# print({z})


numbers = ['one', 'two', 'three', 'four']

n = 0

# while n < 3:
#     print(numbers[n])
#     n += 1
    

for i in numbers:
    print(i)
    
# a, b = 0, 1

# while b < 1000:
#     print(b)
#     a, b = b, a + b
    
    
def isPrime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
             return False
    else:
        return True
             
        
n = 5
if isPrime(n):
    print ('Is a prime')
else:
    print ('Is not a prime')
    

def list_primes():
    for i in range(100):
        if isPrime(i):
            print(i)


list_primes()


class Duck:
    sound = "Whaaack!"
    walking = "Duck is walking!"

    def speak(self):
        print(self.sound)
        
    def walk(self):
        print(self.walking)
        
donald = Duck()
donald.speak()
donald.walk()


a = 9
b = 12 



x = f'These are two numbers {a:>09} {b:<07}'
y = 'This is a new string. {}'.format(x)

print(y)

print(type(a))

from decimal import *
x = Decimal('.1')  + Decimal('.1') + Decimal('.1') 

print(x)

print (7 % 2)


z = 7
a = f'This is amazing {z}'

print(a)

if (type(z) == float): 
    print("hello world")
else:
    print("hello universe") 
    
    
    
arr = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
arr2 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}


print(id(arr))
print(id(arr2))

arr1 = range(5, 100, 5)
for k in arr1:
    print(f'The key is {k}')
    
    
if isinstance(arr, dict):
    print('yap')
else:
    print('noop!')     
    
def sth():
    x = 10
    if x < 9:
        print(False)
    elif x > 10:
        print(False)
    else:
        print("x is greater than 9 but less than 11")

print(sth())
    
x = "This is great." if True else "this is ok."
print(x)