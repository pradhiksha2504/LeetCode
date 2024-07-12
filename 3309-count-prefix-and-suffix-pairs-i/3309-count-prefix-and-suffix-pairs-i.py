class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        def isPrefix(s1,s2):
            m = len(s1)
            n = len(s2)
            # print(s2[:m],s2[n-m])
            if s1 == s2[:m] and s1 == s2[-m:]:
                print("hi")
                return True

        n = len(words)
        for i in range(n-1):
            for j in range(i+1,n):
                if isPrefix(words[i],words[j])==True:
                    count += 1
        return count

        