# Google STEP Program
# Week3 Homework 3

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
    return False
  return token, index + 1


# calculate the inside of the parentheses
def culculateParentheses(line, index):
  index += 1
  inside_tokens = []    # tokenize the expressions in the parentheses
  while line[index] != ')':
    if line[index].isdigit():
      (inside_token, index) = readNumber(line, index)
    elif line[index] == '(':
      (inside_token, index) = culculateParentheses(line, index)
    else:
      if not readOperator(line, index):     # if it is not an operator
        print('Invalid character found: ' + line[index])
        exit(1)
      else:     # the case it is an operator
        (inside_token, index) = readOperator(line, index)
    inside_tokens.append(inside_token)
  # evaluate the expressions in the parentheses
  num_in_parentheses = evaluate(inside_tokens)
  token = {'type': 'NUMBER', 'number': num_in_parentheses}    # return the culculated result as a number
  return token, index + 1



def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '(':
      (token, index) = culculateParentheses(line, index)    # calculate sub-expressions in parentheses
    else:
      if not readOperator(line, index):     # if it is not an operator
        print('Invalid character found: ' + line[index])
        exit(1)
      else:     # the case it is an operator
        (token, index) = readOperator(line, index)

    tokens.append(token)
  return tokens


def evaluate(tokens):
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  new_tokens = []  # a list for new tokens after evaluating multiplication and division in the 1st loop
  new_tokens.append({'type': 'PLUS'})  # Append a dummy '+' token
  index = 1
  tmp = 1   # a varable used to calculate multiplication and division
  # the loop to caluculate multiplication and division first
  # it does not calculate addition and subtraction in this loop
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
  #print(new_tokens)
  answer = 0
  index = 1     # start from index 1 again
  # the second loop to calculate addition and subtraction
  while index < len(new_tokens):
    if new_tokens[index]['type'] == 'NUMBER':
      if new_tokens[index - 1]['type'] == 'PLUS':
        answer += new_tokens[index]['number']
      elif new_tokens[index - 1]['type'] == 'MINUS':
        answer -= new_tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
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
  test("(3.0+4*(2-1))/5")
  test("(3.0+4*(2-1))/5+(6-4)*2")
  test("(4/(5+9.0))*6")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
