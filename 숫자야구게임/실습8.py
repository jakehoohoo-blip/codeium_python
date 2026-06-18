import random
answer = []
count = 0
while len(answer) < 3:
    n = str(random.randint(1,9))
    if n not in answer:
        answer.append(n)
while True:
    nums = input("숫자 입력 :")
    count += 1
    guess = list(nums)
    strike = 0
    ball = 0
    out = 0
    if count >= 20:
        print("시도횟수가 20번이 넘어 게임이 오버되었습니다😭")
        break
    for i in range(3):
        if answer[i] == guess[i]:
            strike += 1
        elif guess[i] in answer and guess[i] != answer[i]:
            ball += 1
        else:
            out += 1
    print(f"{strike}Strike")
    print(f"{ball}Ball")
    print(f"{out}Out")
    if strike == 3:
        print(count, "번째 시도끝에 정답을 맞췄습니다!🎉")
        break
