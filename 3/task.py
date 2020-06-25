

content = open('input.txt','r')
both_wires = content.read().split('\n')
wire_one = both_wires[0].split(',')
wire_two = both_wires[1].split(',')

def manhattan_distance(x1,x2,y1,y2):
    return abs(x1-x2) + abs(y1-y2)
    
def move(x,y,direction,steps):
    if(direction == 'U'):
        return (x, y + steps)
    if(direction == 'L'):
        return (x - steps, y)
    if(direction == 'R'):
        return (x + steps, y)
    if(direction == 'D'):
        return (x, y - steps)

def unfold(arr):
    coordset = list()
    loc = (0,0)
    coordset.append(loc)
    for i in arr:
        x = loc[0]
        y = loc[1]
        direction = i[0]
        steps = int(i[1:])
        for step in range(1,steps + 1):
            loc = move(x,y,direction,step)
            coordset.append(loc)            

    return coordset

def first(wire_one, wire_two):
    set1 = set(unfold(wire_one))
    set2 = set(unfold(wire_two)) 

    set3 = set()

    for i in set1.intersection(set2):
        set3.add(manhattan_distance(0,i[0],0,i[1]))

    set3.remove(0)
    return set3

print("Answer 1: " + str(min(first(wire_one,wire_two))))

def second(wire_one, wire_two):
    set1 = set(unfold(wire_one))
    set2 = set(unfold(wire_two))

    set3 = set1.intersection(set2)
    set4 = set()

    list1 = unfold(wire_one)
    list2 = unfold(wire_two)

    for coord in set3:
        step = 0
        for i in list1:
            if i == coord:
                step += list1.index(i)
                break
        for i in list2:
            if i == coord:
                step += list2.index(i)
                break
        set4.add(step)
    set4.remove(0)
    return set4

print("Answer 2: " + str(min(second(wire_one,wire_two))))
