# break
# braeak는 for문과 while문 둘 다 사용 가는하다.

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue 예제 - 짝수만 출력하기
# for i in range(1,11):
#     if i % 2 != 0:
#         continue
#     print(i)

password = "1234"

while True:

    user = input("비밀번호 입력: ")

    if user != password:
        print("틀렸습니다.")
        continue # 다시 while로 돌아감

    print("로그인 성공")
    break

print("로그인 완료. 환영합니다.")