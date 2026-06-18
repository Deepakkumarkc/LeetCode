class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # Step 1: Calculate the minute hand angle
        # The minute hand moves 6 degrees per minute
        minute_angle = minutes * 6

        # Step 2: Calculate the hour hand angle
        # The hour hand moves 30 degrees per full hour
        # PLUS 0.5 degrees for every minute that has passed
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        # Step 3: Find the absolute difference between the two angles
        diff = abs(hour_angle - minute_angle)

        # Step 4: Return the smaller angle
        # There are always TWO angles between two hands (they add up to 360)
        # We want the smaller one
        return min(diff, 360 - diff)


solve = Solution()
h = 12
m = 30
print(f"Output: {solve.angleClock(h, m)}")