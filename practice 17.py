per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
deposit = []

for bank, percent in per_cent.items():
    deposit_amount = int(money * percent / 100)
    deposit.append(deposit_amount)

print(deposit)
best_deposit = max(deposit)
print(f"Максимальная сумма, которую вы можете заработать — {best_deposit}")