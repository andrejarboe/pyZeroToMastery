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