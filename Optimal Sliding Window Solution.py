'''
We first compute the sum of the first k elements as the initial max_sum. 
Then, using a sliding window approach, we iteratively adjust the sum by subtracting the element that moves out of the window and adding the one that comes into it, updating max_sum if a higher sum is found. 
After scanning through the list, we return the maximum average by dividing max_sum by k as a float.
'''
def findMaxAverage(self, nums, k):
        max_sum=0
        for i in range(k):
            max_sum+=nums[i]
        sum1=max_sum
        for i in range(k,len(nums)):
            sum1-=nums[i-k]
            sum1+=nums[i]
            max_sum=max(max_sum,sum1)
        
        return float(max_sum)/k   #If you are using python 3 , neglect the float() and use it if you are using python 2. 
'''
Time Complexity : O(n)
Space Complexity : O(1) 
'''
