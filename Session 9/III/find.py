listings = ['5','6','7','8','9']
i = input('Find: ')
if i in listings:
    print('Found, position: ', listings.index(i) + 1)
else: 
    print('Not found!')