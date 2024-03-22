
import sys
sys.path.append("src")
import settlement.calculateLogic as calculateLogic
from settlement.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction

"""
self.salary_base = salario base
self.months_worked = meses trabajados
self.annual_layoffs = despidos anuales
self.interest_losses = perdida de intereses
self.bonus_services = prima de servicios
self.vacation_days = dias de vacaciones
self.extra_hours = horas extras
self.night_charges = cargos nocturnos
self.compensation_dismissal = compensacion de despido
"""

#metodo para consola
def main():
    #aviso de uso del programa
    print("Para usar la calculadora de liquidaciones, porfavor introduzca la informacion necesaria")
    
    # Pedir los datos necesarios al usuario
    try:
         salary_base = float(input("Salario base: "))
         months_worked = int(input("Meses trabajados: "))
         annual_layoffs = float(input("Cesantias anuales: "))
         interest_losses = float(input("Intereses de Cesantias: "))
         bonus_services = float(input("Prima de servicios  : "))
         vacation_days = int(input("Días de vacaciones: "))
         extra_hours = float(input("Horas extras: "))
         night_charges = float(input("Recargos nocturnos: "))
         compensation_dismissal = float(input("Indemnizacion por despido: "))
    #control de excepcciones
         
    except ValueError:
        print("Error: por favor, introduce valores numéricos válidos.")
        return
    
    try:
        settlement_calculator = Settlementcalculator(salary_base, months_worked, annual_layoffs, interest_losses,
                                                      bonus_services, vacation_days, extra_hours, night_charges,
                                                      compensation_dismissal)
        net_total = settlement_calculator.Calculate_net_total(0)
        print(f"La cantidad total a pagar es: {net_total}")
    except SalarybaseExcepction as e:
        print(e)
    except Months_workendExcepction as a:
        print(a)

#metodo para inciar 
if __name__ == "__main__":
    main()
