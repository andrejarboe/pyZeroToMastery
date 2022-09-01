first_name = "Saurabh"
last_name = "Agarwal"
full_name = first_name + " " + last_name
print(full_name)

long_string = """
WOW
0 0
---
"""

long2 = '''
BIG
NOW
HOW
POW
'''
print(long_string)
print(long2)

#Escape sequence
weather = "\t It's \"kind of\" sunny \n hope you have a god day!"

print(weather)

#formatted strings 
name = 'Johnny'
age = 29

# python 3
print(f'hi {name}. You are {age} years old')
# python 2
print('hi {}. You are {age} years old'.format(name, age = 34))

# string indexes 
me = 'me me me me'
index = 4

print(f'\'me me me me\' index {index} is: {me[index]}')

string = '0123456789'
# [start:stop]
print(string[0:7])
# [start:stop:step over]
print(string[0:8:2])
# reverse the string
print(string[::-1])
# index to the end
print(string[1:])

"""
# string immutability 

"""

'''
string methods
'''
print((58-36)  * 6 / 60)

quote = 'to be or not to be'
print(quote.title())

print(quote.replace('be', 'me'))
print(quote)