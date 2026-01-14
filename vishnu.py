class Solution:
    def two_sum(self,nums,target):
        nums.sort()
        left=0
        right=len(nums)-1

        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                return "yes"
            elif total<target:
                left+=1
            else:
                right-=1
        return "No"
    def index(self,nums,target):
        nums.sort()
        left=0
        right=len(nums)-1

        while left<right:
            total=nums[left]+nums[right]
            if total==target:
                return [left,right]
            elif total<target:
                left+=1
            else:
                right-=1
        return [-1,-1]


if __name__=="__main__":
    nums=[2,5,6,11,8]
    ob=Solution()
    result=ob.two_sum(nums,14)
    result2=ob.index(nums,14)
    print(result2)
    print(result)


