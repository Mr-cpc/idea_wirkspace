import random
def randomWord(n:int) ->str:
    nums = [chr(num) for num in (list(range(65,91)) + list(range(97,123)))]
    return "".join(random.sample(nums,n))

def random_words(num:int,length:int) ->list:
    return [randomWord(length) for i in range(num)]

class TrieNo:
    def __init__(self,ch:str):
        self.ch = ch
        self.chdts = {}

    def getCh(self,ch:str):
        return self.chdts.get(ch,None)
    def insert(self,word:str):
        root,chd = self,None
        flag = True
        for id,ch in enumerate(word):
            chd = root.getCh(ch)
            if chd is None :
                flag = False if id != len(word) - 1 else flag
                chd = TrieNo(ch)
                root.chdts[ch] = chd
            else:
                if not hasattr(chd,"isEnd"):
                    flag = False
            root = chd
        root.isEnd = True
        return flag
    def starts_with(self,word:str) ->bool:
        root ,chd = self,None
        for ch in word:
            chd = root.getCh(ch)
            if chd is None:
                return False
            root = chd
        return True

    def contains(self,word:str) ->bool:
        root ,chd = self,None
        for ch in word:
            chd = root.getCh(ch)
            if chd is None:
                return False
            root = chd
        return hasattr(root,"isEnd") and root.isEnd

    def is_end(self):
        return hasattr(self,'isEnd') and self.isEnd
if __name__ == '__main__':
    trie = TrieNo(" ")
    cal = lambda s:sum([(ord(s[i])-97) * (26 **(len(s)-i-1)) for i in range(len(s))])
    print(cal("otif"))
    print(cal("racy"))
    # words = ["a","apply","app","ap","appl","apple","appla"]
    words = ["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"]
    words.sort(key=lambda x:(len(x),-cal(x)))
    print(words)
    res,w = 0,""
    for id,word in enumerate(words):
        res,w = (id,word) if trie.insert(word) else (res,w)
    print(w)