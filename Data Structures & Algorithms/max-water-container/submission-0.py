class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l = 0
        r = len(heights)-1
        max_area = 0

        while l < r:
            width = abs(r-l)
            curr_area = min(heights[l], heights[r])*width
            if max_area < curr_area:
                max_area = curr_area

            #we need to make a move that maximizes the area.
            #Since the area is limited by the shortest wall, moving the higher wall makes 0 sense.  
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            #move one of them to ensure we continue exploring 
            #and hope for a case where the area is more,
            #say- 1,2,3,7,100,2,100,7,4 This case, 7 and 7 l and r, 
            #so we still continue exploring and eventually reach at 100,100
        return max_area

                


            
