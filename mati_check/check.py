import copy


def matihai(tehai):#list[]
    a1 = []
    a4 = []
    agarihai = []
    tehai.sort()
    #print(tehai)
    a1.append(tehai)

    if len(tehai) != 13:
        print("error")
        return [0]

    agarihai = [special(tehai)]#七対子、二盃口　判別方法を模索中
    """if agarihai[0] != 0:
        return agarihai"""

    for i in range(3):
        a2 = []
        for x in a1:
            i = (tehai_del(x))
            for y in i:
                a2.append(y)
        a1 = a2

    a3 = list(map(list, set(map(tuple, a2))))

    for pai4 in a3:
        a4.append(mati_4(pai4))
        
    for x in a4:
        for y in x:
            agarihai.append(y)

    agarihai = list(set(agarihai))

    try:
        while True:
            agarihai.remove(0)
    except:
        pass
    try:
        while True:
            agarihai.remove(10)
    except:
        pass

    agarihai.sort()

    #print(agarihai)
    if len(agarihai) == 0:
        agarihai.append(0)

    return agarihai


def special(tehai):#list[13] ちーとい
    j = 0
    for i in range(1,10):
        if tehai.count(i) == 2:
            j += 1
        if tehai.count(i) == 1:
            agarihai = i
    if j == 6:
        return agarihai
    else:
        return 0

#ごり押し    
def mati_4(tehai_4):
    agarihai = []
    tehai_4.sort()
    w = tehai_4[0]
    x = tehai_4[1]
    y = tehai_4[2]
    z = tehai_4[3]

    if z < 28:
        if w == x:
            if x == y:
                if y == z:
                    pass#槓子なので
                elif w+1 == z and ((w-1)%9+1) != 9:#3334
                    if ((w-1)%9+1) != 1:
                        agarihai.append(w-1)
                    agarihai.append(z)
                    if ((z-1)%9+1) != 9:
                        agarihai.append(z+1)
                elif w+2 == z and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#3335
                    agarihai.append(w+1)
                    agarihai.append(z)
                else:#3336
                    agarihai.append(z)
            elif y == z:#3344
                agarihai.append(w)
                agarihai.append(y)
            elif y+1 == z and ((y-1)%9+1) != 9:#3345
                if ((y-1)%9+1) != 1:
                    agarihai.append(y-1)
                if ((z-1)%9+1) != 9:
                    agarihai.append(z+1)
            elif y+2 == z and ((y-1)%9+1) != 8 and ((y-1)%9+1) != 9:#3346
                agarihai.append(y+1)
        elif w+1 == x and ((w-1)%9+1) != 9:#34
            if x == y:#344
                if x == z:#3444
                    if ((w-1)%9+1) != 1:
                        agarihai.append(w-1)
                    agarihai.append(w)
                    if ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:
                        agarihai.append(w+2)
                elif y+1 == z and ((y-1)%9+1) != 9:#3445
                    agarihai.append(x)
            elif x+1 == y and ((x-1)%9+1) != 9:#345
                if y == z:#3455
                    if ((w-1)%9+1) != 1:
                        agarihai.append(w-1)
                    if ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:
                        agarihai.append(w+2)
                elif y+1 == z and ((y-1)%9+1) != 9:#3456
                    agarihai.append(w)
                    agarihai.append(z)
                else:#3457
                    agarihai.append(z)
            elif y == z:#3466
                if ((w-1)%9+1) != 1:
                    agarihai.append(w-1)
                if ((x-1)%9+1) != 9:
                    agarihai.append(x+1)
        elif w+2 == x and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#35
            if x == y:#355
                if y == z:#3555
                    agarihai.append(w)
                    agarihai.append(w+1)
            elif y == z:#3566
                agarihai.append(w+1)
        else:
            if x == y and y == z:#3666
                agarihai.append(w)
            elif x+1 == y and y+1 == z and ((x-1)%9+1) != 8 and ((x-1)%9+1) != 9:#3678
                agarihai.append(w)
    elif y < 28:
        if w == x and w == y:#333東
            agarihai.append(z)
        elif w+1 == x and x+1 == y and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#234東
            agarihai.append(z)
    elif x < 28:
        if w == x and y == z:#22東東
            agarihai.append(w)
            agarihai.append(y)
        elif w+1 == x and y == z and ((w-1)%9+1) != 9:#23東東
            if ((w-1)%9+1) != 1:
                agarihai.append(w-1)
            agarihai.append(x+1)
        elif w+2 == x and y == z and ((w-1)%9+1) != 8 and ((w-1)%9+1) != 9:#24東東
            agarihai.append(w+1)
    elif w < 28:
        if x == y and x == z:#3東東東
            agarihai.append(w)
    else:
        if w == x:#白白
            if w == y:#白白白
                if w == z:##槓子
                    pass
                else:#白白白中
                    agarihai.append(z)
            elif y == z:#白白中中
                agarihai.append(w)
                agarihai.append(z)
        elif x == y and x == z:#中白白白
            agarihai.append(w)    

    return agarihai
        
        
def tehai_del(tehai_m):#list[]
    print_list = []
    
    for i in range(len(tehai_m)):
        exec("tehai_" + str(i) + "= copy.deepcopy(tehai_m)")
        exec("print_list.append(del_3(tehai_" + str(i) + ",i))")

    try:
        while True:
            print_list.remove(0)
    except:
        pass

    p = list(map(list, set(map(tuple, print_list))))

    return p#list[][]
    

def del_3(tehai, i):#list[],int
    j = 0
    x = len(tehai)
    for a in range(i, x):
        for b in range(a+1, x):
            for c in range(b+1, x):
                #print(a,b,c)
                if tehai[a] == tehai[b] and tehai[a] != 0 and tehai[b] != 0 and tehai[c] != 0:
                    if tehai[b] == tehai[c]:
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                elif tehai[a]+1 == tehai[b] and tehai[a] != 0 and tehai[b] != 0 and tehai[c] != 0:
                    if tehai[b]+1 == tehai[c]:
                        tehai[a] = 0
                        tehai[b] = 0
                        tehai[c] = 0
                        j += 1
                        break
                    else:
                        continue
                else:
                    continue
            if j == 1:
                break
        if j == 1:
            break
        
    try:
        for a in range(3):
            tehai.remove(0)
        return tehai#list[]
    except:
        return 0




