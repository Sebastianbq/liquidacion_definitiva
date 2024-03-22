#clase de error para salario igual o menor que cero
class SalarybaseExcepction(Exception):
    def __init__(self):        
        super().__init__(f"el salario no puede ser igual o menor que 0")
#clase de error para cuando no tiene meses o dias trabajados 
class Months_workendExcepction(Exception):
    def __init__(self):       
        super().__init__(f"no tiene dias o meses trabajados")



#clase para implementar la logica del programa
class Settlementcalculator:
    def __init__(self, salary_base, months_worked, annual_layoffs, interest_losses, bonus_services, vacation_days,
                  extra_hours, night_charges, compensation_dismissal):
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
        self.first_extra_hours = Primeras 8 horas extras con recargo del 25%
        self.value_hours_extra_max = horas extras con recargo del 75%
        """
        self.salary_base = salary_base
        self.months_worked = months_worked
        self.annual_layoffs = annual_layoffs
        self.interest_losses = interest_losses
        self.bonus_services = bonus_services
        self.vacation_days = vacation_days
        self.extra_hours = extra_hours
        self.night_charges = night_charges
        self.compensation_dismissal = compensation_dismissal
        self.first_extra_hours = 8  
        self.value_hours_extra = 1.25
        self.value_hours_extra_max = 1.75
        self.hour_work_per_week= 240


        self.Check_salariobase()
        self.Check_months_worked()

    #metodo que calcula la indemnizacion por despido
    def calculate_severance_pay(self):
        Months_of_years= 12
        if self.annual_layoffs == 0:
            return 0
        return (self.annual_layoffs / Months_of_years) * self.months_worked
    

    #metodo que calcula los intereses por indemnizacion por despido
    def Calculate_severance_interest(self):
        return (self.interest_losses / 100) * self.calculate_severance_pay()

    #metodo que calcula prima de servicios
    def Calculate_bonus_services(self):
        years = 12
        return (self.bonus_services / years) * self.months_worked


    #metodo que calcula los dias de vacaciones
    def Calculate_vacation(self):
        total_days_months= 30
        return (self.salary_base / total_days_months) * self.vacation_days

    #metodo que calcula horas extras 
    def Calulate_extra_hours(self):
        if self.extra_hours <= 8:
            return self.extra_hours * self.salary_base * self.value_hours_extra / self.hour_work_per_week  # Recargo del 25% para las primeras 8 horas extras
        else:            
            additional_overtime = self.extra_hours - self.first_extra_hours  # Horas extras adicionales con recargo del 75%
            return (self.first_extra_hours * self.salary_base * self.value_hours_extra / self.hour_work_per_week) + (additional_overtime * self.salary_base * self.value_hours_extra_max / self.hour_work_per_week)

    #metodo que calcula recargos nocturnos
    def Calulate_night_charges(self):
        fixed_rate = 10000 
        return self.night_charges * fixed_rate  # los recargos nocturnos se calculan como una cantidad fija por cada recargo

    #metodo que calcula el salario bruro total
    def Calculate_gross_total(self):
        total = self.salary_base + self.calculate_severance_pay() + self.Calculate_severance_interest() + \
                self.Calculate_bonus_services() + self.Calculate_vacation() + \
                self.Calulate_extra_hours() + self.Calulate_night_charges() + \
                self.compensation_dismissal
        return total

    #metodo que calcula el total neto 
    def Calculate_net_total(self, taxes):       
        return self.Calculate_gross_total() - taxes
    
    #metodo que lanza la excepcion de salario base igual o menor que cero 
    def Check_salariobase (self):
        if self.salary_base == 0:
            raise SalarybaseExcepction()
        
    #metodo que lanza la excepcion de dias no trabajados
    def Check_months_worked (self):
        if self.months_worked == 0:
            raise Months_workendExcepction()






