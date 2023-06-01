import queue as Q

dict_hn = {'Delhi': 0, 'Mumbai': 205, 'Chennai': 345, 'Kolkata': 550, 'Bangalore': 790}

dict_gn = {
    'Delhi': {'Mumbai': 1420, 'Chennai': 2180, 'Kolkata': 1640, 'Bangalore': 2140},
    'Mumbai': {'Delhi': 1420, 'Chennai': 1340, 'Kolkata': 2010, 'Bangalore': 980},
    'Chennai': {'Delhi': 2180, 'Mumbai': 1340, 'Kolkata': 1660, 'Bangalore': 350},
    'Kolkata': {'Delhi': 1640, 'Mumbai': 2010, 'Chennai': 1660, 'Bangalore': 1870},
    'Bangalore': {'Delhi': 2140, 'Mumbai': 980, 'Chennai': 350, 'Kolkata': 1870}
}

start = 'Delhi'
goal = 'Bangalore'
result = ''


def get_fn(citystr):
    cities = citystr.split(" , ")
    hn = gn = 0
    for ctr in range(0, len(cities) - 1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]
    hn = dict_hn[cities[len(cities) - 1]]
    return hn + gn


def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()
    if thiscity == goal:
        result = citystr + " : : " + str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr + " , " + cty), citystr + " , " + cty, cty))
    expand(cityq)


def main():
    cityq = Q.PriorityQueue()
    thiscity = start
    cityq.put((get_fn(start), start, thiscity))
    expand(cityq)
    print("The A* path with total cost is:")
    print(result)

# Execute the main function
main()