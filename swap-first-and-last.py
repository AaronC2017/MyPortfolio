input = raw_input()
lastletter = input[len(input) - 1]
letter1 = input[:1]
middleletters = input[1:-1]
print lastletter + middleletters + letter1
