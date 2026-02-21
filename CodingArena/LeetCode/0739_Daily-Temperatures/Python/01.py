"""
Author: Mrunal Nirajkumar Shah
Date  : 17th February, 2026

LeetCode: 739. Daily Temperature

Time Limit Exceeded
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        answer = []
        for i in range(0, len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):             
                if temperatures[i] < temperatures[j]:
                    count += 1
                    break
                else:
                    count += 1


                if j == len(temperatures) - 1:
                    count = 0
                
            answer.append(count)

        return answer



def main():
    list_temperatures = [[73,74,75,71,69,72,76,73],
                         [30,40,50,60],
                         [30,60,90]
                         ]
    
    solve = Solution()

    result = []
    for temperatures in list_temperatures:
        result.append(solve.dailyTemperatures(temperatures))

    print(result)

if __name__ == "__main__":
    main()