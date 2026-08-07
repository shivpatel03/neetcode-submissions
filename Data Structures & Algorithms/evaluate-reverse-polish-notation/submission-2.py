class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:

            if token == "*":
                secondNumber = int(numbers.pop())
                firstNumber = int(numbers.pop())
                numbers.append(firstNumber * secondNumber)
            elif token == "+":
                secondNumber = int(numbers.pop())
                firstNumber = int(numbers.pop())
                numbers.append(firstNumber + secondNumber)
            elif token == "-":
                secondNumber = int(numbers.pop())
                firstNumber = int(numbers.pop())
                numbers.append(firstNumber - secondNumber)
            elif token == "/":
                secondNumber = int(numbers.pop())
                firstNumber = int(numbers.pop())
                numbers.append(int(firstNumber / secondNumber))
            else: 
                numbers.append(int(token))

        return int(numbers.pop())