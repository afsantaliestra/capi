# Definir una clase de ejemplo
class MiClase:
    def __init__(self):
        self.valor = 0


# Definir la firma y el cuerpo de la función como cadenas de texto
nombre_funcion = "metodo_dinamico"
argumentos = "self, x, y"
cuerpo = "return x + y + self.valor"

# Crear la definición completa de la función como una cadena de texto
codigo_funcion = f"def {nombre_funcion}({argumentos}):\n    {cuerpo}"

# Usar exec para ejecutar la definición de la función
exec(codigo_funcion, globals())

# Asignar la función generada a la clase
setattr(MiClase, nombre_funcion, globals()[nombre_funcion])

# Probar el método dinámico en una instancia de MiClase
instancia = MiClase()
resultado = instancia.metodo_dinamico(5, 3)
print(resultado)  # Debería imprimir 8 si self.valor es 0
