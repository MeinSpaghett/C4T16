District = ['ST','BD','BTL','CG','DD','HBT']
Population = [150300,247100,333300,266800,420900,318000]
Area = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
Density = []
for i in range (1,len(Area)):
    x = Population[i]/Area[i]
    Density.append(x)
total = sum(Density)
print(total/len(District))