"""
Problem: 853. Car Fleet
Link: https://leetcode.com/problems/car-fleet/

Author: Mrunal Nirajkumar Shah
Date: 6 June, 2026

Time Complexity: O(n log n + n + n)
Space Complexity: O(3 * n)

where n is the size of input of car position, speed and time.
"""

from typing import List

class Solution:
    """
    Inputs: Position = [10, 8, 0, 5, 3] ; Speed = [2, 4, 1, 1, 3]
    Output: 3

    if you calculate t = s / d for each and see how each car is behind other and can't overtake,
    you will find pair of 3 car fleet. 10, 8 & 0 & 5, 3.
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Step 1: Sort position, speed such that keep order while descending sort.
        Step 2: Calculate time with time = speed / distance
        Step 3: Calculate Fleet such that if time[i] <= time[j] than its part of fleet where
        i = inital and j = i + 1
        """
        # SORT
        pairs = sorted(zip(position, speed), reverse=True)

        position, speed = zip(*pairs)

        position = list(position)
        speed = list(speed)

        # Calculate Time
        time = []

        for p, s in zip(position, speed):
            d = target - p

            t = s / d   

            time.append(t)
        
        # Calculate Fleet
        fleet = 0

        i = 0
        while i < len(position):
            fleet += 1

            j = i + 1
            while j < len(position):
                if time[i] <= time[j]:
                    j += 1
                else:
                    break
            i = j
        
        return fleet
        

def main():
    list_inputs = [
        (12, [10,8,0,5,3], [2,4,1,1,3]),
        (10, [3], [3]),
        (100, [0,2,4], [4,2,1])
    ]

    list_output = [
        3,
        1,
        1
    ]

    solve = Solution()

    results = []
    for inputs in list_inputs:
        results.append(solve.carFleet(inputs[0], inputs[1], inputs[2]))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()