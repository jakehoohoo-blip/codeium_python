answer = [1,3,5]
guess = [1,7,3]
ball = 0
for i in range(3):
    if guess[i] in answer and guess[i] != answer[i]:
        ball += 1
print(ball)