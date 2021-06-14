class Solution:
    def countWays(self, S1, S2):
        # code here 
        self.S1 = S1
        self.S2 = S2
        ans = 0
        for i in S1:
            for j in S2:
                if i == j :
                    ans += 1
        print(ans)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S1 = input()
        S2 = input()
        ob = Solution()
        ans = ob.countWays(S1, S2)
        print(ans)