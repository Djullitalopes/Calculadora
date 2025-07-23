import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Função que executa operações básicas entre dois números.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError
    elif operador == '^':
        result = num1 ** num2

    return result


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Calculadora')
        print('-----------------------------\n')

        try:
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /, ^): ")
            num2 = float(input("Digite o segundo número: "))

            resultado = calculadora(num1, num2, operador)
            if resultado != resultado: 
                print("Operador inválido!")
            else:
                print(f"\nResultado: {num1} {operador} {num2} = {resultado:.2f}")

        except ValueError:
            print("Dados inválidos! -> Tente novamente.")
        except ZeroDivisionError:
            print("Impossível dividir por zero! -> Tente novamente.")

        continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
        if continuar != 's':
            print("\nVolte sempre!\n")
            break
        time.sleep(2)
