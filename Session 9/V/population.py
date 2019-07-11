District = ['ST','BD','BTL','CG','DD','HBT']
Density = [150300,247100,333300,266800,420900,318000]
# print(max(Density),', ',min(Density))
imax = Density.index(max(Density))
print(District[imax])
imin = Density.index(min(Density))
print(District[imin])