def optimal_score(cards):
    n = len(cards)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = cards[i]

    for g in dp:
        print(g)
    print()

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            print(i, j)
            dp[i][j] = max(cards[i] - dp[i + 1][j], cards[j] - dp[i][j - 1])
            for g in dp:
                print(g)
            print()

    return dp[0][n - 1]


def find_winner_score(cards):
    total_score = sum(cards)
    player_a_score = (total_score + optimal_score(cards)) // 2
    player_b_score = total_score - player_a_score
    return max(player_a_score, player_b_score)


# Example usage:
cards = [1, 2, 100, 4]
winner_score = find_winner_score(cards)
print("Winner's score:", winner_score)

# Example usage:
cards = [1, 2, 100, 4, 5]
winner_score = find_winner_score(cards)
print("Winner's score:", winner_score)
