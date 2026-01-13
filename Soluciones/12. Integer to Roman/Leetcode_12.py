
class Solution(object):
    def intToRoman(self, num):
        numeros_romanos = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

        resultado = []

        for valor, simbolo in numeros_romanos:
            while num >= valor:
                resultado.append(simbolo)
                num -= valor

        return "".join(resultado)