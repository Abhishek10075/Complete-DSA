#List comprehension 
'''
"List comprehension is a short way to create
a new list from an existing list in a single line of code."
'''
#Q1. Even numbers
nums = [1, 2, 3, 4, 5]
even=[num for num in nums if num%2==0]
print(even)


#Q2. Squares
nums = [1, 2, 3, 4, 5]
sq=[num*num for num in nums ]
print(sq)

#Q3. Number greater than 10
nums = [5, 12, 7, 20, 3, 15, 8]
num=[num for num in nums if num>10]
print(num)


#Q4. UQ4. Convert strings to uppercase
words = ["python", "machine", "learning", "ai"]

result = [word.upper() for word in words]

print(result)

#Q5. Remove negative numbers
nums = [-5, 3, -2, 8, -1, 10]
result = [x for x in nums if x >= 0]
print(result)


#Lambda Functions
'''
Definition:
A lambda function is a small anonymous function that is defined using the lambda keyword.
It can take multiple arguments but contains only one expression.

An anonymous function is a function that does not have a name.
'''

#Q1. Find even odd using lambda function

even_odd=lambda n:  'even' if n%2==0 else 'odd'
print(even_odd(2))

#handle negative numbers
even_odd=lambda n: 'Enter valid number ' if n<=0 else ('even' if n%2==0 else 'odd' )
print(even_odd(9))


#Q2. Square using Lambda + map
nums = [1, 2, 3, 4, 5]
sq=list(map(lambda x:x*x,nums ))
print(sq)
'''
map() applies the lambda function to every element.
'''

#Q3. Filter even numbers
nums = [1, 2, 3, 4, 5]
even=list(filter(lambda x:x%2==0,nums))
print(even)
'''
filter() keeps only those elements for which the lambda returns True
'''