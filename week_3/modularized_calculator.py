# Google STEP Program
# Week3 Homework 1 & 2

def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


# read operators ('+', '-', '*', '/')
def readOperator(line, index):
  if line[index] == '+':
    token = {'type': 'PLUS'}
  elif line[index] == '-':
    token = {'type': 'MINUS'}
  elif line[index] == '*':
    token = {'type': 'MUL'}
  elif line[index] == '/':
    token = {'type': 'DIV'}
  else:
    return None
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    else:
      parsed = readOperator(line, index)
      if parsed is None: # if it is not an operator
        print('Invalid character found: ' + line[index])
        exit(1)
      token, index = parsed
    tokens.append(token)
  return tokens


# a function to caluculate only multiplication and division 
def evaluate_mul_div(tokens):
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  new_tokens = []  # a list for new tokens after evaluating multiplication and division
  new_tokens.append({'type': 'PLUS'})  # Append a dummy '+' token
  index = 1
  tmp = 1   # a varable used to calculate multiplication and division
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS' or tokens[index - 1]['type'] == 'MINUS':
        if index > 1:
          new_tokens.append({'type': 'NUMBER', 'number': tmp})
          new_tokens.append(tokens[index - 1])
        tmp = tokens[index]['number']
        if index == len(tokens) - 1:    # the case if the number is the last one
          new_tokens.append({'type': 'NUMBER', 'number': tmp})
      elif tokens[index - 1]['type'] == 'MUL':
        tmp *= tokens[index]['number']
        if index == len(tokens) - 1:    # the case if the number is the last one
          new_tokens.append({'type': 'NUMBER', 'number': tmp})
      elif tokens[index - 1]['type'] == 'DIV':
        tmp /= tokens[index]['number']
        if index == len(tokens) - 1:    # the case if the number is the last one
          new_tokens.append({'type': 'NUMBER', 'number': tmp})
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return new_tokens


# a function to caluculate only addition and subtraction
def evaluate_add_sub(tokens):
  answer = 0
  index = 1     # start from index 1 again
  # the second loop to calculate addition and subtraction
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def evaluate(tokens):
  # calculate only multiplication and division first and get a new tokens
  new_tokens = evaluate_mul_div(tokens)
  answer = evaluate_add_sub(new_tokens)
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("0")
  test("0+0")
  test("1+2")
  test("1.0+2.1-3")
  test("1")
  test("2*3")
  test("2*4.5")
  test("1/3")
  test("2.0/3")
  test("1+2*3")
  test("1*9*9-8.0")
  test("10+4.0/6+18")
  test("8*7.0/3.0-9")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
