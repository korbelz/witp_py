# Comment section
# bomber written by Korbelz
# current scope: Airfield damage required to stop mission types


print ('*** This app calcs Airfield damage required to stop certain mission types ***')
print ('*** Written by Korbelz ***')
print ('*** Feedback/Bugs: Discord: Korbelz#3504 ***')
input('Press ENTER to continue')

i_loop = 0 

while i_loop < 10:
    airfield_size = input("What is the size of the airfield? ")
    airfield_size = int(airfield_size)

    stop_strike = 20 + (airfield_size * 5)

    stop_cap = 50 + (airfield_size * 5)

    print (f'an airfield size of {airfield_size} requires {stop_strike} damage to stop strike missions')
    print ()
    print (f'an airfield size of {airfield_size} requires {stop_cap} damage to stop Patrol and CAP missions')
    print ()
    i_loop += 1 

input('Press ENTER to exit')