def has_33(nums):
    i=0
    a=0
    while i < len(nums)-1:
        if (nums[i]==3 and nums[i+1]==3):
            a+=1
        i+=1
    if a>0:
        print ("true")
        return
    else:
        print ("false")
        return

has_33([1, 3, 3])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3])