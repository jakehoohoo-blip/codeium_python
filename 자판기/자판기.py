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

    if choice == "관리자":
        admin_menu = input("1.재고추가\n2.가격변경\n0.관리자 메뉴 나가기\n번호입력 : ")

        if admin_menu == 1:
            target_menu = input("재고를 추가할 상품명을 입력해 주십시오")
            target_add = input("재고를 얼마나 추가할까요?")
            products[target_menu]["stock"] += target_add
            print("재고가 추가 되었습니다.")
            continue
        if admin_menu == 2:
            target_menu = input("어떤 상품의 가격을 변경하시겠습니까? : ")
            target_price = input("얼마로 변경하시겠습니까. : ")
            products[target_menu]["price"] = target_price
            print("가격 변경을 성공했습니다.")
            continue

        if admin_menu == 0:
            print("관리자 매뉴를 나갑니다.")
            continue

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

    if wallet >= price:
        print("구매중")
        # products[choice]["stock"] -= 1
        products[choice]["stock"] = products[choice]["stock"] - 1
        # wallet -= products[choice]["price"]
        wallet = wallet - products[choice]["price"]
        # print(f"구입완료! {choice}가 배출되었습니다.")
        print("구입완료",choice,"가 배출되었습니다.")
        # print(f"남은 소지금은{wallet}원입니다.")
        print("남은 소지금은",wallet,"원입니다.")

    again = ""
    while again != 'y' or again !='n':
        again = input("추가구매 하실건가요?(y/n) : ")
        if again.upper() == "N":
            print("이용해주셔서 감사합니다.")
            print(f"남은 소지금 : {wallet}원")
            break