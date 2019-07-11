items = input('Insert Numbers: ')
listings = items.split(',')
num = list(map(int, listings))
print (sum(num))
