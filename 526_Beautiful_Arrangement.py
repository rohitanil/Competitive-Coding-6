"""
TC -> O(n!)
SC -> O(n) for the visit array
Logic:
Use the generate all permutations for n logic but instead of creating a result list of all permutations, we check
whether the number follows the condition given. If yes, we recursively call the function.

"""
class Solution:
    def countArrangement(self, n: int) -> int:
        visit = [False] * (n + 1)
        self.count = 0

        def permutations(pos):
            if pos > n:
                self.count += 1
                return
            for num in range(1, n + 1):
                if visit[num] == False and (num % pos == 0 or pos % num == 0):
                    visit[num] = True
                    permutations(pos + 1)
                    visit[num] = False

        permutations(1)
        return self.count
