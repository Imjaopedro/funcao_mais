"""def area():
    a = int(input("digite um lado do retangulo (em Metros): "))
    b = int(input("digite o tamanho do outro lado (em Metros): "))
    arean = a*b
    print(f"a area do retangulo é {arean}m")

area()"""

"""def escreva(txt = None):
    text = input("escreva algo: ")
    tamanho = len(text)
    print("~" * tamanho)
    print(text)
    print("~" * tamanho)

escreva()"""

def maior():
    maior = 0
    menor = 0
    c = 1
    resp = "S"
    while resp == "S":
        num = int(input("Digite um numero: "))

        if c == 1:
            maior = num
            menor = num

        if num > maior:
            maior = num

        if menor > num:
            menor = num

        c+=1
        
        resp = input("desejar continuar: ").upper()

    print(f"O maior numero foi {maior} e o menor foi {menor}")

maior()

