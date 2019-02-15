# Comment section
# bomber written by Korbelz
# current scope: Airfield size required for bombers


print ('*** This app is a Airfield size calc for level bombers ***')
print ('*** Written by Korbelz ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')

print ('Examples: Sally 2205, Nell 1764, Betty 1764')
print ('Examples: B-17 6800, A-20 2400, B-25 4000')

i_loop = 0 

while i_loop < 10:
    print ('')
    max_load = input("What is the max load of the level bomber? ")
    max_load = int(max_load)

    airfield_size = 4 + (max_load / 6500)
    airfield_size = int(airfield_size)

    print (f'This bomber required an airfield size of: {airfield_size}')
    print ('Light bombers only require a size 2 airfield')
    i_loop += 1 

input('Press ENTER to exit')