import csv
import numpy as np

array_powerOffDragCurve = []

with open('data/calisto/powerOffDragCurve.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        array_powerOffDragCurve.append(row)

print(array_powerOffDragCurve)

#####

aerofreno100cd = []

with open('data/calisto/aerofreno100cd.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        aerofreno100cd.append(row)

#print(aerofreno100cd)

##### interpolazione

# new_x = np.linspace(0,1,num=200)
# new_y = np.interp(new_x, x, y)


#####

array_powerOffDragCurve_completo = []

aerofreno100cd = np.linspace(0,1,num=201)
print(len(aerofreno100cd))
print(aerofreno100cd)

for i in range(0, len(array_powerOffDragCurve)):
    array_powerOffDragCurve_completo.append(array_powerOffDragCurve[i] + aerofreno100cd[i])