family = dict(dad=60, mom=50, aunt=12)
print(family['dad'])
family['uncle'] = 55
print(family)
for key, value in family.items():
    print ("\nKey: " + key + " Value:" + str(value))