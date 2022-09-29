from typing import List


class Solution:
    # Backtracking solution.
    # Recursively turn on lights passing through the current 
    # amount of hours, minutes, the light to decide, and the
    # number of lights turned on.
    # Check if the time is possible (hrs 0-11, mins 0-59),
    # and when the target number of lights are turned on,
    # print a time with the minutes zero padded.
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8: return []
        res = []
        leds = [1, 2, 4, 8, 16, 32, 1, 2, 4, 8] # Value of LED lights (mins / hrs)

        def setLeds(hrs, mins, light, nrOn):
            if hrs > 11: return
            if mins > 59: return
            if nrOn == turnedOn:
                res.append("".join([str(hrs), ":", str(mins).zfill(2)])) # Print zero padded string
                return
            if light == len(leds):
                return

            # Search with LED turned on:
            if light <= 5: # Switch between adding mins and hrs
                setLeds(hrs, mins + leds[light], light + 1, nrOn + 1)
            else:
                setLeds(hrs + leds[light], mins, light + 1, nrOn + 1)

            # Search with LED turned off:
            setLeds(hrs, mins, light + 1, nrOn)
        
        setLeds(0, 0, 0, 0)
        return res

sol = Solution()
print(sol.readBinaryWatch(turnedOn = 0))
print(sol.readBinaryWatch(turnedOn = 1))
print(sol.readBinaryWatch(turnedOn = 2))
print(sol.readBinaryWatch(turnedOn = 8))
print(sol.readBinaryWatch(turnedOn = 9))
