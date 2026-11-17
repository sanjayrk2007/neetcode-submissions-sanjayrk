class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        i,j=0,len(heights)-1
        while(i<j):
            area=(j-i)*min(heights[i],heights[j])
            maxarea=max(maxarea,area)
            if(heights[i]<=heights[j]):
                i+=1
            else:
                j-=1
        return maxarea
