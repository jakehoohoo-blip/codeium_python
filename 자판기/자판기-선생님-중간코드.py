# ===============================
# 자판기 프로그램
# ===============================

# 상품 정보
products = {
    "콜라": {
        "price": 1500,
        "stock": 5
    },
    "사이다": {
        "price": 1400,
        "stock": 5
    },
    "물": {
        "price": 1000,
        "stock": 5
    }
}

# 사용자 소지금
wallet = 10000

print("===== 자판기 프로그램 =====")

while True:

    print("\n==============================")
    print(f"현재 소지금 : {wallet}원")
    print("==============================")

    # 메뉴 출력
    print("\n[메뉴]")
    for name, info in products.items():
        print(f"{name} - {info['price']}원 (재고 : {info['stock']}개)")

    print("\n종료를 원하면 '종료'를 입력하세요.")

    # 상품 선택
    choice = input("\n구매할 상품 : ")

    # 종료
    if choice == "종료":
        print("\n프로그램을 종료합니다.")
        break

    # 상품 존재 확인
    if choice not in products:
        print("없는 상품입니다.")
        continue

    # 재고 확인
    if products[choice]["stock"] == 0:
        print("품절된 상품입니다.")
        continue

    # 가격 확인
    price = products[choice]["price"]

    # 소지금 확인
    if wallet < price:
        print("소지금이 부족합니다.")
        continue