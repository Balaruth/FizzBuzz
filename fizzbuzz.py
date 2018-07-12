print "Welcome to FizzBuzz! This program converts numbers that are multiples of 3 into \"fizz\" and numbers that are multiples of 5 into \"buzz\". If it's a multiple of both, it will convert to \"fizzbuzz\"!"

while True:
  value = raw_input("Please enter a number between 1 and 100 to be fizzbuzzed, or 0 to quit: ")

  try:
    value = int(value)

    if value > 0 and value <= 100:
      fizzy = range(1, value + 1)
      for number in fizzy:
        if number % 3 == 0 and number % 5 == 0:
          print "fizzbuzz"
        elif number % 3 == 0:
          print "fizz"
        elif number & 5 == 0:
          print "buzz"
        else:
          print number
    elif value > 100 or value < 0:
      print "Please choose a number between 1 and 100!"
    elif value == 0:
      print "Thanks for trying FizzBuzz!"
      break

  except ValueError:
    print "Please choose a number between 1 and 100!"