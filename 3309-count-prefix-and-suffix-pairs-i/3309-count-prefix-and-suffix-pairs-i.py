class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        def isPrefix(s1,s2):
            m = len(s1)
            n = len(s2)
            if s1 == s2[:m] and s1 == s2[-m:]:
                return True

        n = len(words)
        l,r = 0,1
        while(l<n-1 and r<n):
                if isPrefix(words[l],words[r])==True:
                    count += 1
                r +=1
                if r == n:
                    l += 1
                    r = l+1
        return count

        