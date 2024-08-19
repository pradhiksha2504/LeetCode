class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        b = s[0]
        ans = [b]
        mlen = len(ans[0])
        for i in range(1,len(s)):
            if s[i] in b:
                ind=b.index(s[i])
                b = b[ind+1:]
                b+=s[i]
            else:
                b+=s[i]
            if len(b)>mlen:
                ans=[b]
                mlen=len(b)
        # return len(ans[0])
        return mlen