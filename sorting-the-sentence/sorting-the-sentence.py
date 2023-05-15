class Solution:
 def sortSentence(self, s:str) -> str:
    dic = {}
    word = s.split(' ')
    
    for i in word:
        last = i[-1]
        dic[last] = i[:-1]
    dic = dict(sorted(dic.items()))
    return ' '.join(dic.values())

    