


def unique():
    num_list=list(map(int, (input().split())))
    new_list=[]
    for x in num_list:
        if x in new_list:
            continue
        else:
            new_list.append(x)
    for x in new_list:
        print(x)

unique()
