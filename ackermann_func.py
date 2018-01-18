def func(n):
    return((c*(c + 1) + 2*c + 1) % 32768)

if __name__ == '__main__':

    for c in range(32768):
        dp = list(range(32768))
        dp[0] = func(c)
        for i in range(1, c + 1):
            dp[i] = (dp[i - 1]*(c + 1) + 2*c + 1) % 32768
        if dp[dp[c]] == 6:
            print(c)
            break
