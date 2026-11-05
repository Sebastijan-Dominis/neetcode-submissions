class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for p in path + "/":
            if p == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                    cur = ""
                elif cur == "." or cur == "":
                    cur = ""
                elif cur == "/":
                    continue
                else:
                    stack.append(cur)
                    cur = ""
            else:
                cur += p
        
        return "/" + "/".join(stack)