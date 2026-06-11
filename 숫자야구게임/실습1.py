answer = [1,3,5]
guess = [1,7,3]
strike = 0
for i in range(3):
    if answer[i] == guess[i]:
        strike += 1
print(strike)