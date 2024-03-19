



#Una de las formas de realizar errores es condicionando las caracteristicas de tal forma que 
#si se proporcionan argumentos inválidos al inicializar la calculadora o al calcular el total neto se lanzarán excepciones ValueError
#Ejemplo 1
class CalculadoraLiquidacion:
    def __init__(self, salario_base, meses_trabajados, cesantias_anuales, intereses_cesantias, prima_servicios, dias_vacaciones, horas_extras, recargos_nocturnos, indemnizacion_despido):
        if salario_base < 0:
            raise ValueError("El salario base no puede ser negativo.")

#Ejemplo 2 Tambien podemos generar un error en los casos de prueba añadiendo valores incorrectos en los casos prueba
 # Prueba de excepciones (por ejemplo, calcular_total_neto con impuestos negativos)
        with self.assertRaises(ValueError):
            valor_neto = result.calcular_total_neto(-1000000)

#Ejemplo 3 Podemos generar errores verificando con valores incorrectos en la calculadora
    def calcular_total_neto(self, impuestos):
        # Verificación de divisiones por cero
        if impuestos == 0:
            raise ValueError("Los impuestos no pueden ser cero")
        return self.calcular_total_bruto() - impuestos
