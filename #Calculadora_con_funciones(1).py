#Calculadora_con_funciones

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir(a,b):
    if b==0:
        return "Error: div/0"
    return a/b

while True:
    print("===CALCULADORA===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    try:
        Opcion=int(input("Seleccione su opción(1-5): "))
        if Opcion==5:
            print("Saliendo del sistema...")
            break
        if Opcion>=1 and Opcion<=4:
            num1=float(input("Ingrese el primer número: "))
            num2=float(input("Ingrese el segundo número: "))
            if Opcion==1:
                resultado=sumar(num1, num2)
                print("Resultado: ",resultado)
            elif Opcion==2:
                resultado=restar(num1, num2)
                print("Resultado: ",resultado)
            elif Opcion==3:
                resultado=multiplicar(num1, num2)
                print("Resultado: ",resultado)
            elif Opcion==4:
                resultado=dividir(num1, num2)
                print("Resultado: ",resultado)
        else:
            print("Error. Seleccione una opción valida.")
    except ValueError:
        print("Error. Ingrese valores númericos válidos.")