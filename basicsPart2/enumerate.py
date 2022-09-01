# we can pass any iterable to enumerate, and it will store them as separate tuple with index starting from 0.
for i, char in enumerate('Hello World'):
    print(i, char)

# only print the value for the index of 50
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')
