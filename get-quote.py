import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", encoding = 'utf8')
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
