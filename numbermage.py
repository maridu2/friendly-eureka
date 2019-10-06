import random
print("Di un número")
x = 0
y = random.choice([2, 5] + list(range(40, 50)))
while x != y:
    x = int(input())
    if x < y: 
        print("Un poquitintín más")
    if x > y:
        print("LOKOOOOO, te has pasadooooo")
print(random.choice(["Eres tremendamente listo", "Has acertado :)", "Enhorabuena :D", "Yeeeeeey, por fin"]))
