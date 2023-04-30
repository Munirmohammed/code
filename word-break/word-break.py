class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            # check each word in wordDict rather than iterating from 0 to i
            for word in wordDict:
                if len(word) > i:
                    continue
                if s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = dp[i - len(word)]
                    break
        return dp[len(s)]        