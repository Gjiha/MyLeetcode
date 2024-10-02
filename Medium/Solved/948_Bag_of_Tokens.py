class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        
        tokens.sort()
        score = 0

        i = 0
        j = len(tokens) - 1

        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                print(f"token[{i}]: {tokens[i]}, power: {power}, score: {score}")
                i += 1
            
            elif j - i == 0:  # -> elimina il caso in cui l'ultima mossa mangia un token
                break

            elif score > 0:
                power += tokens[j]
                score -= 1
                print(f"token[{j}]: {tokens[j]}, power: {power}, score: {score}")
                j -= 1
            
            else:
                break
        
        return score

sol = Solution()
print(sol.bagOfTokensScore([100, 200], 150))