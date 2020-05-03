def To_decide_Turn(orientation, direction):
	if direction == "R":
		orientation += 1
	if direction == "L":
		orientation -= 1
	if orientation == -1:
		orientation = 3
	if orientation == 4:
		orientation = 0
	return orientation

def To_Visit_Horizontaly(old_value, new_value, Y, map):
	for X in range(old_value+1, new_value+1):
		if map[X][Y] == 1:
                        # below line print the cordinate of x and y if path repeated
			print("Found a repeat!  X:", X, " Y:", Y)
		else:
			map[X][Y] = 1

def To_Visit_Verticaly(X, old_Y, new_Y, map):
	for Y in range(old_Y+1, new_Y+1):
		if map[X][Y] == 1:
                        # below line print the cordinate of x and y if path repeated
			print("Found a repeat!  X:", X, " Y:", Y)
		else:
			map[X][Y] = 1

def To_Move_Ver_or_Hor(X, Y, orientation, distance, route_array):
	if orientation == 0:
		To_Visit_Horizontaly(X, X+distance, Y, route_array)
		X += distance
	if orientation == 1:
		To_Visit_Verticaly(X, Y, Y+distance, route_array)
		Y += distance
	if orientation == 2:
		To_Visit_Horizontaly(X, X-distance, Y, route_array)
		X -= distance
	if orientation == 3:
		To_Visit_Verticaly(X, Y, Y-distance, route_array)
		Y -= distance

	return X, Y

CurrentX = 0
CurrentY = 0
CurrentOrientation = 0

route_array = [[0 for x in range(300)] for y in range(300)] 
route_array[0][0] = 1

print("provide the input if form R2, L4, R5.......etc")

inputArray = input().split(", ")

for instruction in inputArray:
	CurrentOrientation = To_decide_Turn(CurrentOrientation, instruction[0][0])
	CurrentX, CurrentY = To_Move_Ver_or_Hor(CurrentX, CurrentY, CurrentOrientation, int(instruction[1:]), route_array)

print("Distance from start_point to end_point:", abs(CurrentX) + abs(CurrentY))
