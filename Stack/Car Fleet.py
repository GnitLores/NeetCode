class Solution(object):
    # Solution making use of the fact that a car fleet cannot arrive before cars ahead of it.
    # This means that we can start the cars by position, and evalueate the time it takes to reach
    # in the order of position.
    # Every car that is not being held back by a car ahead of it results in a new car fleet.
    # O(nlogn) time becase of the sorting.
    def carFleet(self, target, position, speed):
        time = [(target-p) / s for p,s in zip(position, speed)] # Time to reach destination
        cars = list(zip(position, speed, time)) # Organize data for cars in a sorted list of tuples
        cars.sort(reverse = True)

        # In order of proximity to goal, check which cars are not being held back.
        carFleets = 0
        latestFleet = -1
        for i in range(len(cars)):
            if cars[i][2] > latestFleet:
                carFleets += 1
                latestFleet = cars[i][2]

        return carFleets

    # Could also have been solved with a stack, but the method is similar.
    # Same time complexity.
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

sol = Solution()
print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(sol.carFleet(10, [6,8], [3,2]))