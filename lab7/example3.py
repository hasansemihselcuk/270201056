books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
for i in range(len(books)):
  lenn = len(books[i])
  unique = len(set(books[i]))
  print(books[i] , (lenn , unique,((lenn+unique)/2)))