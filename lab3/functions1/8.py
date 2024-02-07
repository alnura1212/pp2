def spy_game(nums):
    i=0
    a=0
    while i < len(nums)-1:
        if (nums[i]==0 and nums[i+1]==0 and nums[i+2]==7):
            a+=1
        i+=1
    if a>0:
        print ("Yes")
        return
    else:
        print ("No")
        return

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 