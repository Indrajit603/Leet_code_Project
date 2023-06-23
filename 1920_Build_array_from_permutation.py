#nums = [0,2,1,5,3,4]
#output =[0,1,2,4,5,3]
def buildArray(nums):
    ans=[]
    for i in range(len(nums)):  # running a loop from i=0 to length of the list
        value=nums[nums[i]]  #storing in a temp variable
        ans.append(value)  # appending the value in the list
    
    print(ans)
    
if __name__ == "__main__":
    
    import sys
    
    nums=sys.argv[1]
    nums=list(eval(nums))

    buildArray(nums)
        
        