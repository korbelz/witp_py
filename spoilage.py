# Comment section
# spoil written by Korbelz
# current scope: spoil Calc


print ('*** This app is a fuel/supply spoilage calc ***')
print ('*** Written by Korbelz ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')

port = input("what size is the port? ")
port = int(port)

airfield = input("what size is the airfield? ")
airfield = int(airfield)

fuel_waste = 1000 + ((port + airfield) * (port + airfield) * 2000)

supply_waste = 5000 + ((port + airfield) * (port + airfield) * 3000)

print (f'fuel over {fuel_waste} will spoil at this base' )

print (f'supply over {supply_waste} will spoil at this base' )

input('Press ENTER to exit')

