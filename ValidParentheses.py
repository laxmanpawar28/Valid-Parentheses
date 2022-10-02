class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        boo = True
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                try:
                    popped_element = stack.pop()
                except:
                    boo=False
                    break
                if popped_element=='(' and ch==')':
                    pass
                elif popped_element=='{' and ch=='}':
                    pass
                elif popped_element=='[' and ch==']':
                    pass
                else:
                    boo=False
                    break
        if len(stack)==0:
            return (boo)
        else:
            return (False)
