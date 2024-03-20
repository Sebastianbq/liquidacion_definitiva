

from src.settlement.calculateLogic import Settlementcalculator, SalarybaseExcepction, Months_workendExcepction

def main():
    print("Para usar la calculadora de liquidaciones, porfavor introduzca la informacion necesaria")
    
    try:
         salary_base = float(input("Salario base: "))
         months_worked = int(input("Meses trabajados: "))
         annual_layoffs = float(input("Despidos anuales: "))
         interest_losses = float(input("Pérdidas de interés: "))
         bonus_services = float(input("Servicios de bonificación: "))
         vacation_days = int(input("Días de vacaciones: "))
         extra_hours = float(input("Horas extras: "))
         night_charges = float(input("Recargos nocturnos: "))
         compensation_dismissal = float(input("Compensación por despido: "))
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

if __name__ == "__main__":
    main()
