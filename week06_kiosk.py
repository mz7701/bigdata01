#아아:2000 라떼:2500
drinks = ["아이스 아메리카노", "카페 라때"]
prices = [2000, 2500]

while True:
    menu = input(f"1) 아이스 아메리카노 {prices[0]} 2) 카페 라때 {prices[1]} 3)주문종료 :")
    if menu == "1":
        print("아이스아메리카노 가격 2000원입니다")
    elif menu == "2":
        print("카페라때 2500원")
    elif menu == "3":
        print("주문 종료")
        break
