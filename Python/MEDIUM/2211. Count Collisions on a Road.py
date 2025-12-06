class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip("L")
        print('Directions: ', directions.count("R"))
        directions = directions.rstrip("R")
        print('Directions: ', directions)
        return directions.count("R") + directions.count("L")
    
directions = "RLRSLL"
solve = Solution()
print(f"output: {solve.countCollisions(directions)}")