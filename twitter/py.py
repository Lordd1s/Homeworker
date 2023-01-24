for a in range(1000+1):
    for b in range(200+1):
        list1 = []
        if a - (b * 8) == -150 and a - (b * 5) == 60:
            list1.append(a)
            list1.append(b)
            print(list1)
