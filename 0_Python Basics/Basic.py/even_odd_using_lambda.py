#Find even odd using lambda function

even_odd=lambda n:  'even' if n%2==0 else 'odd'
print(even_odd(2))
#Handle negative numbers
even=lambda n: 'enter valid number' if n<=0 else('even' if n%2==0 else 'odd')
print(even(-32))


#Store even using list comprehension
even=[i for i in range(1,11) if i%2==0]
