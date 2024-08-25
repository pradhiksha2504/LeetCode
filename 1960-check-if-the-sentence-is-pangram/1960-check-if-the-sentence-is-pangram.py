class Solution(object):
    def checkIfPangram(self, sentence):
        s = set(sentence)
        if len(s)==26:
            return True
        return False
        