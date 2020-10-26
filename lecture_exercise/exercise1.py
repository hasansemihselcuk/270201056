book_price = 24.95

r_book_prices = book_price * (6 / 10)

f_copy = 3
additional_copy = 0.75
copies = 60

shipping = f_copy + (additional_copy * (copies-1))

total = shipping + (r_book_prices *copies)
print(total)
