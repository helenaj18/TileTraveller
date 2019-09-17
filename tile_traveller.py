# Starting location is (1,1)
# Print travel options for the location
# Write possible travel direction
# Ask the user for direction
# If the user inputs a invalid direction, print "Not a valid direction!" and try again
# Ask user for direction until they are at (3,1), then print "Victory!"


initial_location = 1.1

location = initial_location


def travel_options(location):
    N='(N)orth'
    S='(S)outh'
    E='(E)ast'
    W='(W)est'

    if location==1.1 or location==2.1 or location==3.1:
        print('You can travel: ', N)
    elif location==1.2:
        print('You can travel: ', N,'or',S,'or',E)
    elif location==1.3:
        print('You can travel: ', S, 'or', E)
    elif location==2.2 or location==3.3:
        print('You can travel: ', S, 'or', W)
    elif location==2.3:
        print('You can travel: ', E,'or',W)
    elif location==3.2:
        print('You can travel: ', N,'or', S)


def input_direction(location):
    direction = input('Direction: ')
    direction=direction.lower()

    while location != 3.1:

        if location == 1.1 and direction == 'n':
            location = 1.2
        elif location == 1.2 and direction == 'n':
            location = 1.3
        elif location == 1.2 and direction == 's':
            location = 1.1
        elif location == 1.2 and direction == 'e':
            location = 2.2
        elif location == 1.3 and direction == 'e':
            location = 2.3
        elif location == 1.3 and direction == 's':
            location = 1.2
        elif location == 2.3 and diretion == 'e':
            location = 3.3
        elif location == 2.3 and direction == 'w':
            location = 1.3
        elif location == 3.3 and direction == 's':
            location = 3.2
        elif location == 3.3 and direction == 'w':
            location = 2.3
        elif location == 3.2 and direction == 'n':
            location = 3.3
        elif location == 3.2 and direction == 's':
            location = 3.1
        elif location == 2.2 and direction == 's':
            location = 2.1
        elif location == 2.2 and direction == 'w':
            location = 1.2
        elif location == 2.1 and direction == 'n':
            location = 2.2
        else:
            print('Not a valid direction!')

        direction = input('Direction: ')
        direction = direction.lower()



while location!=3.1:
    travel_options(location)

    input_direction(location)

    change_location(location)
else:
    print('Victory!')
