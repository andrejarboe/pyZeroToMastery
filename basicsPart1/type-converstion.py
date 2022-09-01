print(type(int(str(100))))
print(int("0b100",2))
print(bin(5))

birth_year = input('What year were you born? ')

age = 2022 - int(birth_year)

print(f'Your age is: {age}')