"""
Author: Mrunal Nirajkumar Shah
Date  : 18th February, 2026

LeetCode: 853. Car Fleet

Solution Description:
Time Complexity: O(n log n)
Space Complexity: O(n)

Remember:
S = D / T
therefore, T = D / S

Method:
1. Sort the position with respect to its time (decreasing order)
2. for ith value, for first time add it to stack.
    3. check each ith value with the last stack memember such that if stack_time >= current_time then
        4. continue
    else
    5. add the index to slow_stack

6. return len(slow_stack)
"""

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position, sorted_speed = zip(*sorted(zip(position, speed), reverse=True))

        sorted_position = list(sorted_position)
        sorted_speed = list(sorted_speed)

        slow_stack = []

        for i in range(len(sorted_position)):
            if slow_stack:
                index = slow_stack[-1]
                stack_time = ((target - sorted_position[index]) / sorted_speed[index])
                current_time = ((target - sorted_position[i]) / sorted_speed[i])

                if stack_time >= current_time:
                    continue
                else:
                    slow_stack.append(i)

            else:
                slow_stack.append(i)

        return len(slow_stack)

def main():
    # position, speed, target
    list_testcases = [([10,8,0,5,3], [2,4,1,1,3], 12),
                     ([3], [3], 10),
                     ([0,2,4], [4,2,1], 100),
                     ([0, 4, 2], [2, 1, 3], 10)
                     ]
    solve = Solution()

    result = []
    for testcase in list_testcases:
        result.append(solve.carFleet(target=testcase[2], position=testcase[0], speed=testcase[1]))

    print(result)

if __name__ == "__main__":
    main()