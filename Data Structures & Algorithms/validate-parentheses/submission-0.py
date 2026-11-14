class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
                top+=1
            else:
                if top==-1:
                    return False
                if not((s[i]==")" and stack[top]=="(") or (s[i]=="}" and stack[top]=="{") or (s[i]=="]" and stack[top]=="[")):
                    return False
                else:
                    stack.pop()
                    top-=1
                    continue
        return top==-1 