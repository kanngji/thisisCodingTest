class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum = sum(apple)

        capacity_sort = sorted(capacity,reverse=True)
        i = 0
        while apple_sum > 0:
            apple_sum-=capacity_sort[i]
            i+=1
        
        return i