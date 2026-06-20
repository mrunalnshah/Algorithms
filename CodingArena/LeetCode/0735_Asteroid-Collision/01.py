"""
Problem: 735. Asteroid Collision
Link: https://leetcode.com/problems/asteroid-collision/

Author: Mrunal Nirajkumar Shah
Date: 3 June, 2026

Time Complexity: O(n * m)
Space Complexity: O(n)

where n is the number of asteroids, and m is the size of a_stack.
NOTE: m <= n
"""

from typing import List

class Solution:
    """
    Input = [5, 10, -5]
    Output = [5, 10]

    -5 and 10 collided and 10 destroyed -5, while 5, 10 are moving in same 
    direction and will never collide.
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Keep track of asteroids, if last asteriod is positive or negative and current asteroid is same sign,
        than they never collide. If last is negative and current is positive, then they never collide due to 
        moving in different directions. if last is positive and current is negative than they collide and either
        both are destroyed or one is destroyed moving towards next target.
        """
        a_stack = []

        for asteroid in asteroids:
            destroyed = False
            if asteroid < 0:
                while a_stack:
                    if a_stack[-1] < 0:
                        a_stack.append(asteroid)
                        break
                    else:
                        if a_stack[-1] == abs(asteroid):
                            a_stack.pop()
                            destroyed = True
                            break
                        elif a_stack[-1] < abs(asteroid):
                            a_stack.pop()
                        else:
                            break
                        
                if not a_stack and not destroyed:
                    a_stack.append(asteroid)

            else:
                a_stack.append(asteroid)

        return a_stack    

def main():
    list_asteroids = [
        [5,10,-5],
        [8,-8],
        [10,2,-5],
        [3,5,-6,2,-1,4],
        [-2,-1,1,2]
    ]

    list_outputs = [
        [5,10],
        [],
        [10],
        [-6,2,4],
        [-2,-1,1,2]
    ]

    solve = Solution()

    results = []
    for asteroids in list_asteroids:
        results.append(solve.asteroidCollision(asteroids))

    # TEST
    for result, output in zip(results, list_outputs):
        if sorted(result) == sorted(output):
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()