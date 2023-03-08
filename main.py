print('calculadora de perimetro e area')
print('escolha a forma da qual quer calcular')
forma = int(
  input("(1)Triangulo,(2)Quadrado,(3)Retangulo,(4)Poligono,(5)Circulo"))
if forma == 1:
  calc = int(input("Oque deseja calcular: (1)area, (2)perimetro"))
  if calc == 1:
    b = int(input("Indique a base do triangulo"))
    h = int(input("Indique a altura do triangulo"))
    a = (b * h) / 2
    print(f"{a} cm2 e a area do triangulo")
  elif calc == 2:
    l1 = int(input("Indique o lado 1"))
    l2 = int(input("Indique o lado 2"))
    l3 = int(input("Indique o lado 3"))
    p = l1 + l2 + l3
    print(f"{p} cm e o perimetro do triangulo")

elif forma == 2:
  calc = int(input("Oque deseja calcular: (1)area, (2)perimetro"))
  if calc == 1:
    l1 = int(input("Indique o lado do quadrado"))
    a = l1 * 2
    print(f"{a} cm2 e a area do quadrado")
  elif calc == 2:
    l1 = int(input("Indique o lado do quadrado"))
    p = l1 * 4
    print(f"{p} cm e o perimetro do triangulo")
elif forma == 3:
  calc = int(input("Oque deseja calcular: (1)area, (2)perimetro"))
  if calc == 1:
    l1 = int(input("Indique o primeiro lado do retangulo"))
    l2 = int(input("Indique o segundo lado do retangulo"))
    a = l1 * l2
    print(f"{a} cm2 e a area do quadrado")
  elif calc == 2:
    l1 = int(input("Indique o um dos lados do retangulo"))
    l2 = int(input("Indique o um dos lados do retangulo"))

    p = (l1 * 2) + (l2 * 2)
    print(f"{p} cm e o perimetro do triangulo")
elif forma == 4:
  ql = int(input("Digite a quantidade de lados do polígono regular: "))
  l = float(input("Digite a medida em cm de um dos lados do polígono: "))
  p = ql * l
  print(f"O perímetro do polígono regular é de {p} cm.")
elif forma == 5:
  calc = int(input("Oque deseja calcular: (1)area, (2)perimetro"))
  pi = 3.14
  if calc == 1:
    print('pi considerado como : 3.14')
    r = int(input("informe o raio da circunferencia"))
    a = r * r * pi
    print(f"{a} cm2 e a area do quadrado")
  elif calc == 2:
    r = int(input("informe o raio da circunferencia"))
    a = 2 * pi * r
    print(f"{p} cm e o perimetro do triangulo")
else:
  print('Esse valor nao esta computado')
