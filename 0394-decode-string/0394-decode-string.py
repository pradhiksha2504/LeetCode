class Solution:
    def decodeString(self, s: str) -> str:
        stack, num = [], []
        i, n = 0, len(s)
        while i < n:
            exp = []
            if s[i].isdigit():
                if s[i+1].isdigit():
                    digit = s[i]
                    j = i+1
                    while j < n:
                        if s[j].isdigit():
                            digit += s[j]
                            j += 1
                        else:
                            break
                    num.append(int(digit))
                    i = j-1
                else:
                    num.append(int(s[i]))  
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                while stack and stack[-1]!= "[":
                    exp.append(stack.pop())
                stack.pop()
                exp = "".join(exp[::-1])
                stack.append(exp * num[-1])
                num.pop()
            else:
                stack.append(s[i])
            i +=1
        return "".join(stack)
                     