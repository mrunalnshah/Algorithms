"""
Problem: 739. Daily Temperatures
Link: https://leetcode.com/problems/daily-temperatures/

Author: Mrunal Nirajkumar Shah
Date: 3 June, 2026

Time Complexity: O(n * m)
Space Complexity: O(2 * n)

where n is the size of temperatures and m is the max size of t_stack.
"""

from typing import List

class Solution:
    """
    Input = [73, 74, 75, 71, 69, 72, 76, 73]
    Output = [1, 1, 4, 2, 1, 1, 0, 0]

    after 75, 4 indexes later we get 76.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Keep track of answers with 0 initialized. Use t_stack to note temperatures not 
        mesured due to not bigger amount encountered. If current temp > stack[-1] than pop from stack and
        answer
        """
        answer = [0] * len(temperatures)
        t_stack = []

        for i in range(len(temperatures)):
            while t_stack:
                if temperatures[i] > temperatures[t_stack[-1]]:
                    answer[t_stack[-1]] = i - t_stack[-1]
                    t_stack.pop()
                else:
                    break
            
            t_stack.append(i)

        return answer

def main():
    list_temperatures = [
        [73,74,75,71,69,72,76,73],
        [30,40,50,60],
        [30,60,90]
    ]

    list_output = [
        [1,1,4,2,1,1,0,0],
        [1,1,1,0],
        [1,1,0]
    ]

    solve = Solution()

    results = []
    for temperatures in list_temperatures:
        results.append(solve.dailyTemperatures(temperatures))

    # TEST
    for result, output in zip(results, list_output):
        if sorted(result) == sorted(output):
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()