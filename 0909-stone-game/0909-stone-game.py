class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        l, r = 0, len(piles)-1
        turn = 1
        while l <= r:
            print(piles[l], piles[r], turn)
            print("Alice: ",alice," bob: ", bob)
            if piles[l] > piles[r]:
                if turn == 1:
                    alice += piles[l]
                    turn = 0
                else:
                    bob += piles[r]
                    turn = 1
                l += 1
            else:
                if turn == 1:
                    alice += piles[r]
                    turn = 0
                else:
                    bob += piles[l]
                    turn = 1
                r -= 1
        return alice > bob
                
        