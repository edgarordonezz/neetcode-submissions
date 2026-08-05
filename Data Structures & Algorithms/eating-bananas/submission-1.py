class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # start with the most minimum k we can
        best = 0
        low = 1
        high = max(piles)
        while low <= high:
            middle = low + (high - low) // 2 # calculate the middle of the low and high boundaries
            k = middle
            total_hours = 0
            for pile in piles:
                total_hours += -(-pile // k) # calculate total hours for current k
            if total_hours <= h: # if total hours is valid, set as k and check smaller k values
                best = k
                high = middle - 1
            elif total_hours > h: # if total hours is greater, increment low to check bigger k values
                low = middle + 1

        return best