from typing import List


class Solution:
    # We need to know if the current midpoint is in the left portion or right portion (compared to wrapping point).
    # If midpoint is in left portion, everything to the left of midpoint is sorted.
    # If midpoint is in right portion, everything to the right of midpoint is sorted.
    # For the relevant case, check if the number should be in that sorted portion, otherwise choos the other half.
    # O(logn)
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2 
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: # Mid in left portion, wrap to the right (or no wrap at all)
                if target > nums[mid] or target < nums[l]: # Left portion is sorted, so if target is left it is greater than l and smaller than mid
                    l = mid + 1
                else:
                    r = mid - 1
            else: # Mid in right portion, wrap to the left
                if target < nums[mid] or target > nums[r]: # Right portion is sorted, so if target is right it is greater than mid and smaller than r
                    r = mid - 1
                else:
                    l = mid + 1
        return - 1

    # Similar principle but less elegant and efficient implementation.
    # Also O(logn).
    def searchFirstTry(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        def binSearch(l, r):
            mid = (r + l) // 2 
            if nums[l] == target: return l
            if nums[r] == target: return r
            if nums[mid] == target: return mid
            
            roomLeft = l < mid - 1
            roomRight = r > mid + 1
            
            if not roomLeft and not roomRight:
                return -1

            wrapLeft = nums[l] > nums[mid]
            wrapRight = nums[mid] > nums[r]

            leftIfUnwrapped = roomLeft and nums[l] < target < nums[mid]
            rightIfUnwrapped = roomRight and nums[mid] < target < nums[r]

            def searchLeft():
                return binSearch(l + 1, mid - 1)
            def searchRight():
                return binSearch(mid + 1, r - 1)

            if wrapLeft:
                if rightIfUnwrapped:
                    return searchRight()
                else:
                    return searchLeft()
            
            if wrapRight:
                if leftIfUnwrapped:
                    return searchLeft()
                else:
                    return searchRight()
            
            if leftIfUnwrapped:
                return searchLeft()
            elif roomRight:
                return searchRight()
            else:
                return - 1

        return binSearch(l, r)

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))
print(sol.search([4,5,6,7,0,1,2], 3))
print(sol.search([1], 0))
print(sol.search([1,2,3,4,5,6], 4))
print(sol.search([5,1,2,3,4], 1))

print("")
print(sol.searchFirstTry([4,5,6,7,0,1,2], 0))
print(sol.searchFirstTry([4,5,6,7,0,1,2], 3))
print(sol.searchFirstTry([1], 0))
print(sol.searchFirstTry([1,2,3,4,5,6], 4))
print(sol.searchFirstTry([5,1,2,3,4], 1))