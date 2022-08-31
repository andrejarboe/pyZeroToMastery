isMagician = True
isExpert = False

if isMagician and isExpert:
    print('You are a master magician')
elif isMagician and not isExpert:
    print("""At least you're getting there.""")

if not isMagician:
    print("""You need to find some magic!""")