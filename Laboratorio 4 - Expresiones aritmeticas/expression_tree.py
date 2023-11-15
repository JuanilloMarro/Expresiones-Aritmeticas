from __future__ import annotations
from typing import TypeVar
from node import Node

T = TypeVar('T')


class ExpressionTree:
    def __init__(self, expression: str):
        self.expression: str = expression
        self.__root = Node('')
        self.build()

    def __build(self, subtree: Node | None) -> None:
        if self.expression != '':
            self.current_token = self.expression[0]
            self.expression = self.expression[1:]

            if self.current_token == '(':
                new_node = Node('')
                subtree.left = new_node
                self.__build(subtree.left)

                self.current_token = self.expression[0]
                self.expression = self.expression[1:]
                subtree.data = self.current_token

                if self.expression.startswith('!'):
                    subtree.data += '!'
                    self.expression = self.expression[1:]

                subtree.right = Node('')
                self.__build(subtree.right)

                self.expression = self.expression[1:]

            else:
                subtree.data = self.current_token

                if self.expression.startswith('!'):
                    subtree.data += '!'
                    self.expression = self.expression[1:]

    def build(self):
        return self.__build(self.__root)

    def __evaluate(self, number, variable, subtree):
        if subtree is None:
            return 0
        if subtree.left is None and subtree.right is None:
            return subtree.data

        left_evaluation = self.__evaluate(number, variable, subtree.left)
        rigth_evaluation = self.__evaluate(number, variable, subtree.right)

        if left_evaluation == variable:
            left_evaluation = number
        elif rigth_evaluation == variable:
            rigth_evaluation = number

        if subtree.data == '+':
            return int(left_evaluation) + int(rigth_evaluation)

        elif subtree.data == '-':
            return int(left_evaluation) - int(rigth_evaluation)

        elif subtree.data == '*':
            return int(left_evaluation) * int(rigth_evaluation)

        elif subtree.data == '/':
            return int(left_evaluation) / int(rigth_evaluation)

        elif subtree.data == '÷':
            return int(left_evaluation) // int(rigth_evaluation)

        elif subtree.data == '%':
            return int(left_evaluation) % int(rigth_evaluation)

        elif subtree.data == '^':  
            return int(left_evaluation) ** int(rigth_evaluation)

    def evaluate(self, number, variable):
        return self.__evaluate(number, variable, self.__root)

    def __prefijo(self, subtree: Node | None):
        if subtree is not None:
            if subtree.is_leaf():
                return str(subtree.data)
            else:
                result = str(subtree.data) + ''
                result += self.__prefijo(subtree.left) + ''
                result += self.__prefijo(subtree.right) + ''
                return result

    def prefijo(self):
        return self.__prefijo(self.__root)

    def __infijo(self, subtree: Node | None):
        if subtree is not None:
            if subtree.is_leaf():
                return str(subtree.data)
            else:
                result = ''
                result += self.__infijo(subtree.left) + ''
                result += str(subtree.data) + ''
                result += self.__infijo(subtree.right) + ''
                return result

    def infijo(self):
        return self.__infijo(self.__root)

    def __postfijo(self, subtree: Node | None):
        if subtree is not None:
            if subtree.is_leaf():
                return str(subtree.data)
            else:
                result = ''
                result += self.__postfijo(subtree.left) + ''
                result += self.__postfijo(subtree.right) + ''
                result += str(subtree.data) + ''
                return result

    def postfijo(self):
        return self.__postfijo(self.__root)