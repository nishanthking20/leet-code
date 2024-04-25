class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=''
        l=len(strs)
        for i in  range(len(strs[0])):
            d=strs[0][:i+1]
            j=0
            while j<l:
                if d == strs[j][:i+1]:
                    j+=1
                else:
                    return s
            s=d 
        return s
        
