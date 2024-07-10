class Solution:
    def minOperations(self, logs: List[str]) -> int:
        main = ""
        fol = []
        for i in logs:
            if i == '../':
                curr = main
                if len(fol) >0:
                    fol.pop()
            elif i == './':
                curr = main
            else:
                if main == "":
                    main = curr = i
                    fol.append(main)
                else:
                    curr = i
                    fol.append(curr)
        n = len(fol)
        if  n == 1:
            if curr == main:
                return 1
            return 0
        return n
        