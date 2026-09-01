# Daftar Harga buah
fruit_list = [
    # product_name, price, stock
    ["apple", 10_000,10],
    ["orange", 15_000,10],
    ["grape", 20_000, 10]
]

# Menu Input
apple_qty = int(input("Masukkan jumlah apel: "))
orange_qty = int(input("Masukkan jumlah jeruk: "))
grape_qty = int(input("Masukkan jumlah anggur: "))

# Detail belanja
total_price_apple = apple_qty * fruit_list[0][1]
total_price_orange = orange_qty * fruit_list[1][1]
total_price_grape = grape_qty * fruit_list[2][1]
total_price = total_price_apple + total_price_orange + total_price_grape

print("\nDetail Belanja\n")
print(f"Apel: {apple_qty} x {fruit_list[0][1]} = {total_price_apple}")
print(f"Jeruk: {orange_qty} x {fruit_list[1][1]} = {total_price_orange}")
print(f"Anggur: {grape_qty} x {fruit_list[2][1]} = {total_price_grape}")
print(f"\nTotal : {total_price}")

# Main menu -> menggunakan looping

# Payment feature
print("-"*20)   # dekorasi pembatas
payment = int(input("\nMasukkan jumlah uang: "))
selisih = total_price - payment
if payment < total_price:
    print("\n[X]Transaksi dibatalkan !")
    print(f"Uang kurang sebesar {selisih}")
else:
    print("\nTerima kasih !")
    if selisih:
        print(f"\nUang kembalian anda: {abs(selisih)}")
