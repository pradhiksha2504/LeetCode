class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        b = s[0]
        mlen = len(b)
        for i in range(1,len(s)):
            if s[i] in b:
                ind=b.index(s[i])
                b = b[ind+1:]
                b+=s[i]
            else:
                b+=s[i]
            mlen = max(mlen, len(b))
        return mlen