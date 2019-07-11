color = ['red', 'green', 'blue']
# i = int(input ('At position: '))
# print('The color is: ', color[i])
action = input('Insert Command: ')
if action.isnumeric():
    color.pop(int(action))
else:
    color.remove(action)
print(*color, sep=(','))
    