isOld = True
isLicensed = True

if isOld and isLicensed:
    print('You are old enough to drive!, and you have a license')
elif isLicensed:
    print('You can drive now!')
else:
    print('You are not of age...')

#Truthy and Falsy

#true, true, false
print(bool('hello'))
print(bool(5))
print(bool(0))
