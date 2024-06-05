ticket_num = int(input())
total_price = 0
for _ in range(tickt_num):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        ticket_price = 0
    elif 18 <= age < 25:
        ticket_price = 900
    else:
        ticket_price = 1390
    total_price += ticket_price

if ticket_num > 3:
    total_price *= 0.9

print(f"Сумма к оплате: {total_price} руб.")