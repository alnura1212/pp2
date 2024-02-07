num_list=list(map(int, (input().split())))

def filter_prime(x):
    for x in num_list:
        if x==2:
            print(2)
        else:
            k=0
            for i in range(2, int(x*0.5)+1):
                if x%i==0:
                    k+=1
            if k==0 and x>2:
                print(x)
filter_prime(num_list)