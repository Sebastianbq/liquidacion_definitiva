class SalarybaseExcepction(Exception):
    def __init__(self):        
        #
        super().__init__(f"el salario no puede ser igual o menor que 0")
class Months_workendExcepction(Exception):
    def __init__(self):        
        #
        super().__init__(f"no tiene dias o meses trabajados")



#
class Settlementcalculator:
    def __init__(self, salary_base, months_worked, annual_layoffs, interest_losses, bonus_services, vacation_days,
                  extra_hours, night_charges, compensation_dismissal):
        #
        self.salary_base = salary_base
        self.months_worked = months_worked
        self.annual_layoffs = annual_layoffs
        self.interest_losses = interest_losses
        self.bonus_services = bonus_services
        self.vacation_days = vacation_days
        self.extra_hours = extra_hours
        self.night_charges = night_charges
        self.compensation_dismissal = compensation_dismissal

    def calculate_severance_pay(self):
        if self.annual_layoffs == 0:
            return 0
        return (self.annual_layoffs / 12) * self.months_worked

    def Calculate_severance_interest(self):
        return (self.interest_losses / 100) * self.calculate_severance_pay()

    def Calculate_bonus_services(self):
        return (self.bonus_services / 12) * self.months_worked

    def Calculate_vacation(self):
        return (self.salary_base / 30) * self.vacation_days

    def Calulate_extra_hours(self):
        if self.extra_hours <= 8:
            return self.extra_hours * self.salary_base * 1.25 / 240  # Recargo del 25% para las primeras 8 horas extras
        else:
            first_extra_hours = 8  # Primeras 8 horas extras con recargo del 25%
            additional_overtime = self.extra_hours - first_extra_hours  # Horas extras adicionales con recargo del 75%
            return (first_extra_hours * self.salary_base * 1.25 / 240) + (additional_overtime * self.salary_base * 1.75 / 240)

    def Calulate_night_charges(self):
        return self.night_charges * 10000  # los recargos nocturnos se calculan como una cantidad fija por cada recargo

    def Calculate_gross_total(self):
        total = self.salary_base + self.calculate_severance_pay() + self.Calculate_severance_interest() + \
                self.Calculate_bonus_services() + self.Calculate_vacation() + \
                self.Calulate_extra_hours() + self.Calulate_night_charges() + \
                self.compensation_dismissal
        return total


    def Calculate_net_total(self, taxes):       
        self.Check_salariobase
        return self.Calculate_gross_total() - taxes
    

    def Check_salariobase (self):
        if self.salary_base == 0:
            raise SalarybaseExcepction()






