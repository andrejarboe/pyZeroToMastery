# For loop 
# iterable, can be looped over:
# list, dictionary, tuple, set, string

for i in 'Hello World':
    print(i)

print(i)

print("\n")
for i in [1,2,3,4,5]:
    print(i)

print("\n")
for i in {6,7,8,9,10}:
    print(i)

print("\n")
for i in (11,12,13,14,15):
    print(i)
 
print("\n")
for i in list(range(10)):
    print(i)

print("\n")
print(i)

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)

user = {
    'name': 'Golem',
    'age': 5006,
    'canSwim': False
}

for item in user.items(): #it stores each pair as tuple, in a list (in a dict_items class).
    print(item)

for item in user.values():
    print(item)
for item in user.keys():
    print(item)

for k, v in user.items():
    print(k,v)

for i in user.items():
    k,v=i
    print(k,v)