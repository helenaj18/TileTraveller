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



while location!=3.1:
    travel_options(location)

    input_direction(location)

    change_location(location)
else:
    print('Victory!')
