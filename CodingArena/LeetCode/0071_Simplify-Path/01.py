"""
Problem: 71. Simplify Path
Link: https://leetcode.com/problems/simplify-path/

Author: Mrunal Nirajkumar Shah
Date: 7 June, 2026

Time Complexity: O(n ^ 2)
Space Complexity: O(n)

where n is the length of path
"""

class Solution:
    """
    Input = "/home/"
    Output = "/home"

    Simplify path
    """
    def simplifyPath(self, path: str) -> str:
        """
        Use different cases to insert or pop from the stack. later join the stack into string.
        """
        p_stack = []

        i = 0
        while i < len(path):
            match (path[i]):
                case '/':
                    while i < len(path) and path[i] == '/':
                        i += 1

                    if p_stack and not p_stack[-1] == '/':
                        p_stack.append('/')
                case '.':
                    if p_stack and p_stack[-1] != '/':
                        p_stack.append(path[i])
                        i += 1
                        continue

                    if i + 1 < len(path):
                        match (path[i + 1]):
                            case '/':
                                i = i + 2
                            case '.':
                                count = 0
                                while i < len(path) and path[i] == '.':
                                    count += 1
                                    i += 1
                                
                                if i < len(path) and path[i] != '/':
                                    p_stack.extend(['.'] * count)
                                    continue

                                if count == 1:
                                    continue
                                elif count == 2:
                                                                           
                                    if p_stack:
                                       p_stack.pop()

                                    while p_stack and p_stack[-1] != '/':
                                        p_stack.pop()
                                else:
                                    p_stack.extend(['.'] * count)
                                    
                            case _:
                                p_stack.append(path[i])
                                i += 1
                    else:
                        break
                case _:
                    p_stack.append(path[i])
                    i += 1

        if len(p_stack) > 1 and p_stack[-1] == '/':
            p_stack.pop()
        
        if p_stack:
            if p_stack[0] != '/':
                p_stack.insert(0, '/')
        else:
            p_stack.append('/')

        return ''.join(p_stack)

def main():
    list_path = [
        "/home/",
        "/home//foo/",
        "/home/user/Documents/../Pictures",
        "/../",
        "/.../a/../b/c/../d/./",
        "/..hidden",
        "/hello../world"
    ]

    list_output = [
        "/home",
        "/home/foo",
        "/home/user/Pictures",
        "/",
        "/.../b/d",
        "/..hidden",
        "/hello../world"

    ]

    solve = Solution()

    results = []
    for path in list_path:
        results.append(solve.simplifyPath(path))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")
    

if __name__ == "__main__":
    main()