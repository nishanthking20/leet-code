class Solution:
    def isValid(self, s: str) -> bool:
        st = [] 
        for c in s: 
            if c in '([{':
                st+=[c]
            else:
                if not st or \
                    (c == ')' and st[-1] != '(') or \
                    (c == '}' and st[-1] != '{') or \
                    (c == ']' and st[-1] != '['):
                    return False
                st.pop() 
        return not st