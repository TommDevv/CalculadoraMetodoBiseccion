import math

def metodo_biseccion(funcion, a, b, error_minimo):
    iteraciones = 0
    tabla_resultados = []

    fa = funcion(a)
    fb = funcion(b)

    if abs(fa) < error_minimo:
        return a, [[0, a, b, a, fa, 0]]
    if abs(fb) < error_minimo:
        return b, [[0, a, b, b, fb, 0]]

    if fa * fb > 0:
        print("El método de bisección no puede aplicarse, ya que no hay garantía de una raíz en el intervalo.")
        return None, []

    while (b - a) / 2 > error_minimo:
        iteraciones += 1
        c = (a + b) / 2
        fc = funcion(c)
        error = (b - a) / 2

        tabla_resultados.append([iteraciones, a, b, c, fc, error])

        if abs(fc) < error_minimo:
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c, tabla_resultados

entrada = input("Ingresa una función matemática en términos de x (ej: x**2 + 3*x - 5 o sin(x)): ")
contexto = {"__builtins__": None, **math.__dict__}
funcion = eval(f"lambda x: {entrada}", contexto)

a = float(input("Ingresa el valor de xi (limite inferior del intervalo): "))
b = float(input("Ingresa el valor de xu (limite superior del intervalo): "))
error_minimo = float(input("Ingresa el error mínimo requerido: "))


raiz, tabla_resultados = metodo_biseccion(funcion, a, b, error_minimo)

if raiz is not None:

    print("\n    n    |    xi    |    xu    |    xr    |  f(xr)   | Error")
    print("-" * 60)
    for fila in tabla_resultados:
        print(f"{fila[0]:9} | {fila[1]:7.5f} | {fila[2]:7.5f} | {fila[3]:7.5f} | {fila[4]:7.5f} | {fila[5]:7.5f}")
    print(f"\nLa raíz aproximada es: {raiz:.6f}")
else:
    print("No se pudo encontrar la raíz.")

input("Presiona Enter para salir...")
