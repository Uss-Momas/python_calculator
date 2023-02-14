#!/usr/bin/python3
""""Python Calculator"""
import os


def menu():
    while True:
        print("Esolha uma opcao:")
        print("0: Soma")
        print("1: Subtraccao")
        print("2: Multiplicacao")
        print("3: Divisao")
        print("4: Exponenciacao")
        n = int(input("\n"))
        if n >= 0 and n <= 4:
            break
        os.system("clear")
    return n


def main():
    while True:
        opt = menu()
        os.system("clear")
        a = float(input("Introduza o 1o valor:\n"))
        b = float(input("Introduza o 2o valor:\n"))
        if opt == 0:
            operator = "+"
            print("+ escolhido.")
            result = add(a, b)
        elif opt == 1:
            operator = "-"
            print("- escolhido")
            result = sub(a, b)
        elif opt == 2:
            operator = "*"
            print("* escolhido")
            result = mult(a, b)
        elif opt == 3:
            operator = "/"
            print("/ escolhido")
            result = div(a, b)
        elif opt == 4:
            operator = "**"
            print("** escolhido")
            result = power(a, b)
        print("{:.1f} {} {:.1f} = {:.1f}".format(a, operator, b, result))
        opt = int(input("Deseja fazer outra operacao? 0 - SIM, 1 - NAO\n"))
        if opt == 1:
            break
        os.system("clear")


def add(a, b):
    """Performs the sum of 2 elements"""
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def power(a, b):
    return a ** b


if __name__ == "__main__":
    main()
