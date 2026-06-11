answer = ['3','7','1']
nums = input("숫자 입력 :")
guess = list(nums)
strike = 0
ball = 0
for i in range(3):
    if answer[i] == guess[i]:
        strike += 1
    elif guess[i] in answer and guess[i] != answer[i]:
        ball += 1
print(strike)
print(ball)