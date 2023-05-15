cases = int(input())

for _ in range(cases):
    datos = input().split(' ')
    people = int (datos[0])
    pairs = int (datos[1])
    #people, pairs = map(int, input().split())
    max_val = 1
    
    array = [0] * people
    numGroups = 1
    map = {}
    
    for _ in range(pairs):
        pers = input().split(' ')
        p1 = int (pers[0])
        p2 = int (pers[1])
        #p1, p2 = map(int, input().split())
        l1 = array[p1 - 1]
        l2 = array[p2 - 1]
        
        if l1 == 0 and l2 != 0:
            array[p1 - 1] = l2
            map[l2] = map.get(l2, 0) + 1
        elif l1 != 0 and l2 == 0:
            array[p2 - 1] = l1
            map[l1] = map.get(l1, 0) + 1
        elif l1 == 0 and l2 == 0:
            l1 = numGroups
            array[p2 - 1] = numGroups
            array[p1 - 1] = numGroups
            map[numGroups] = 2
            numGroups += 1
        elif l1 != l2:
            for i in range(people):
                if array[i] == l2:
                    array[i] = l1
            map[l1] = map.get(l1, 0) + map.get(l2, 0)
            del map[l2]
        
        if map.get(l1, 0) > max_val:
            max_val = map[l1]
        if map.get(l2, 0) > max_val:
            max_val = map[l2]
    
    print(max_val)
