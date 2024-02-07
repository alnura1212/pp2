num_list=list(map(int, (input().split())))
def histogram(nums):
    for x in nums:
        print ('*'*x)

histogram(num_list)