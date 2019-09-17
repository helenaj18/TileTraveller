# Starting location is (1,1)
# Print travel options for the location
# Write possible travel direction
# Ask the user for direction
# If the user inputs a invalid direction, print "Not a valid direction!" and try again
# Ask user for direction until they are at (3,1), then print "Victory!"


initial_location = 1.1

location = initial_location

while location!=3.1:
    travel_options(location)

    input_direction(location)

    change_location(location)
else:
    print('Victory!')
