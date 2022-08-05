class Solution(object):
    # Create dictionary with value as key and list of indices as value.
    # For each value, check if the remainder required to reach the sum exists and return the indices.
    # Gets a bit complicated because half the sum existing twice is a possible solution.
    # O(n) time and faster than 65% of solutions.
    def twoSumMultiPass(self, nums, target):
        hashmap = dict()
        for i in range(0, len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]

        for i in range(0, len(nums)):
            
            if nums[i] == target/2:
                if len(hashmap[nums[i]]) == 2:
                     return hashmap[nums[i]]
            else:
                rem = target - nums[i]
                if rem in hashmap:
                    return [i,hashmap[rem][0]]

    # Simpler single pass solution. For each number, check if a number summing up to the target exists. If not, add the index to the dictionary.
    # Dictionary values can just be a single index becaue we don't need to remember multiple indices.
    # O(n) time and faster than 99.3% of solutions.
    def twoSumSinglePass(self, nums, target):
        hashmap = dict()
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if rem in hashmap:
                return[hashmap[rem],i]

            hashmap[nums[i]] = i


def testSolution(nums, target):
    sol = Solution
    result = sol.twoSumMultiPass(sol, nums, target)
    print("Multi pass: " + str(result))
    result = sol.twoSumSinglePass(sol, nums, target)
    print("Single pass: " + str(result))

testSolution([2,7,11,15], 9)
testSolution([3,2,4], 6)
testSolution([3,3], 6)