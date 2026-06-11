answer = [1,3,5]
guess = [1,7,3]
strike = 0
ball = 0
for i in range(3):
    if answer[i] == guess[i]:
        strike += 1
    elif guess[i] in answer and guess[i] != answer[i]:
        ball += 1
print(strike)
print(ball)