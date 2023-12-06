
# puzzle input
times =" 56     97     77     93"
distance =  " 499   2210   1097   1440"


# to int array 
# to int array
times = [int(x) for x in times.split() if x.isdigit()]
distance = [int(x) for x in distance.split() if x.isdigit()]
 

print(times)
print(distance)
 
wins_list = []
for index, time in enumerate(times):
 
    wins = 0
    for push in range(0, time):
 
        speed = push
        travel_time = time-push
        distance_traveled = speed * travel_time
 
        if(distance_traveled > distance[index]):
            wins += 1
 

    wins_list.append(wins)
 

# multiply all wins together if wins are not 0
 
print(wins_list)
 
total_wins = 1
for win in wins_list:
    if(win != 0):
        total_wins *= win
 
print(total_wins)
 

#part 2
print("part 2")

times = "56     97  77  93"
distance = "   499 2210  1097   1440"
 
# remove whitespace & convert to int
times = times.replace(" ", "")
time = int(times)

distance = distance.replace(" ", "")
distance = int(distance)

print("start calculation")
wins = 0
for push in range(0, time):
 
    speed = push
    travel_time = time-push
    distance_traveled = speed * travel_time
 
    if(distance_traveled > distance):
        wins += 1
 
print(wins)

