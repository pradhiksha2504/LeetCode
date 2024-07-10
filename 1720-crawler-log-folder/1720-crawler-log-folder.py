class Solution:
    def minOperations(self, logs: List[str]) -> int:
        main = ""
        fol = []
        for i in range(len(logs)):
            if logs[i] == '../':
                curr = main
                if len(fol) >0:
                    fol.pop()
            elif logs[i] == './':
                curr = main
            else:
                if main == "":
                    main = logs[i]
                    fol.append(main)
                    curr = main
                else:
                    curr = logs[i]
                    fol.append(curr)
        # print(fol,curr,main)
        if  len(fol) == 1:
            if curr == main:
                return 1
            return 0
        
        return len(fol)
        