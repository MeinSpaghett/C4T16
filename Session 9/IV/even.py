listings = [9,7,54,32,2346234,6234564367,5,6,7,4,5,67,78,23]
results = []
for i in range(1,len(listings)):
    if listings[i] % 2 == 0:
        results.append(listings[i])
# print(results)
print(*results, sep=(','))