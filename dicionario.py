# school_class = {}

# while True:
#     name = input("Digite o nome do aluno: ")
#     if name == '':
#         break

#     score = int(input("Insira a pontuação do aluno (0-10): "))
#     if score not in range(0, 11):
#         break

#     id name in school_class:
#     school_class[name] += (score,)
#     else:
#     school_class[name] = (score,)
try:
    value = input("Entre um valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorreta...")
except ZeroDivisionError:
    print("Entrada muito ruim...")
except TypeError:
    print("muito muito ruim entrada...")
except:
    print("Booo!")