class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l=[]
        for i in words[0]:
            c=1
            for j in range(1,len(words)):
                if i in words[j]:
                    words[j]=words[j].replace(i,'',1)
                    c+=1
            if c==len(words):
                l+=[i]
        print(words)
        return l