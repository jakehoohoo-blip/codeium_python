import random
answer = []
while len(answer) < 3:
    n = str(random.randint(1,9))
    if n not in answer:
        answer.append(n)
while True:
    nums = input("숫자 입력 :")
    guess = list(nums)
    strike = 0
    ball = 0
    for i in range(3):
        if answer[i] == guess[i]:
            strike += 1
        elif guess[i] in answer and guess[i] != answer[i]:
            ball += 1
    print(f"{strike}Strike")
    print(f"{ball}Ball")
    if strike == 3:
        break
print("정답을 맞췄습니다!🎉")