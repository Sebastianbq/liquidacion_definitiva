import unittest
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


class CalculTest(unittest.TestCase):
    
    # Caso de prueba 1: Empleado que renuncia voluntariamente después de 6 meses de trabajo
    def test_1(self):
        base_salary = 5000000
        months_worked = 6
        annual_layoffs= 8.33
        interest_losses= 12 
        bonus_services= 8.33 
        vacation_days= 10 
        extra_hours= 5 
        night_charges= 2 
        compensation_dismissal= 0
        expected_liquidation= 5816883.8297999995

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)
    
        valor_neto = result.Calculate_net_total(1000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)


    # Caso de prueba 2: Empleado despedido sin justa causa después de 12 meses de trabajo
    def test_2(self):
        base_salary = 6000000
        months_worked = 12
        annual_layoffs= 8.33
        interest_losses= 12 
        bonus_services= 8.33 
        vacation_days= 15 
        extra_hours= 8 
        night_charges= 3 
        compensation_dismissal= 7500000
        expected_liquidation= 15780017.6596

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(1000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
        

    # Caso de prueba 3: Empleado con contrato a plazo fijo que finaliza después de 8 meses
    def test_3(self):
        base_salary = 5500000
        months_worked = 8
        annual_layoffs= 8.33
        interest_losses= 12 
        bonus_services= 8.33 
        vacation_days= 12 
        extra_hours= 10 
        night_charges= 4
        compensation_dismissal= 0
        expected_liquidation= 7049386.773066668

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(1000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
    
    # Caso de prueba 4: Empleado con horas extras y recargos nocturnos
    def test_4(self):
        base_salary = 6000000
        months_worked = 10
        annual_layoffs = 8.33
        interest_losses = 12 
        bonus_services = 8.33 
        vacation_days = 20 
        extra_hours = 15 
        night_charges = 5 
        compensation_dismissal = 0
        expected_liquidation = 9106264.716333333

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(1500000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 5: Empleado con indemnización por despido
    def test_5(self):
        base_salary = 7000000
        months_worked = 24
        annual_layoffs = 8.33
        interest_losses = 12 
        bonus_services = 8.33 
        vacation_days = 30 
        extra_hours = 12 
        night_charges = 4 
        compensation_dismissal = 10000000
        expected_liquidation = 22535868.652533337

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(2000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)
    
    # Caso de prueba 6: Empleado con salario base y sin beneficios adicionales
    def test_6(self):
        base_salary = 4500000
        months_worked = 9
        annual_layoffs = 8.33
        interest_losses = 12 
        bonus_services = 8.33 
        vacation_days = 15 
        extra_hours = 0 
        night_charges = 0 
        compensation_dismissal = 0
        expected_liquidation = 5750013.244699999

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(1000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 7: Empleado con indemnización por despido y sin otros beneficios adicionales
    def test_7(self):
        base_salary = 5000000
        months_worked = 12
        annual_layoffs = 8.33
        interest_losses = 12 
        bonus_services = 8.33 
        vacation_days = 20 
        extra_hours = 0 
        night_charges = 0 
        compensation_dismissal = 10000000
        expected_liquidation = 16833350.992933333

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(1500000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 8: Empleado con todos los beneficios posibles
    def test_8(self):
        base_salary = 5500000
        months_worked = 18
        annual_layoffs = 8.33
        interest_losses = 12 
        bonus_services = 8.33 
        vacation_days = 25 
        extra_hours = 10 
        night_charges = 3 
        compensation_dismissal = 9000000
        expected_liquidation = 17422734.822733335

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                        interest_losses, bonus_services, vacation_days,
                                        extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(2000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)



    # Caso de prueba 9:Contrato de trabajo a término indefinido sin cesantías
    def test_9(self):
        base_salary=6000000
        months_worked=24
        annual_layoffs=0
        interest_losses=12
        bonus_services=8.33
        vacation_days=15
        extra_hours=8
        night_charges=3
        compensation_dismissal=0
        expected_liquidation = 7280016.66

        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                            interest_losses, bonus_services, vacation_days,
                                            extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(2000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

    # Caso de prueba 10: salario base 0
    def test_10(self):
        base_salary= 0
        months_worked=24
        annual_layoffs=0
        interest_losses=12
        bonus_services= 0
        vacation_days=15
        extra_hours=8
        night_charges=3
        compensation_dismissal=0        

        self.assertRaises(SalarybaseExcepction, Settlementcalculator, base_salary, months_worked, annual_layoffs,
                                            interest_losses, bonus_services, vacation_days,
                                            extra_hours, night_charges, compensation_dismissal)
        
    # Caso de prueba 11: ningun dia trabajado
    def test_11(self):
        base_salary= 600000
        months_worked=0
        annual_layoffs=0
        interest_losses=12
        bonus_services= 0
        vacation_days=15
        extra_hours=8
        night_charges=3
        compensation_dismissal=0        

        self.assertRaises(Months_workendExcepction, Settlementcalculator, base_salary, months_worked, annual_layoffs,
                                            interest_losses, bonus_services, vacation_days,
                                            extra_hours, night_charges, compensation_dismissal)
        
    # Caso de prueba 12:
    def test_12(self):
        base_salary= 600000
        months_worked=0
        annual_layoffs=0
        interest_losses=12
        bonus_services= 0
        vacation_days=15
        extra_hours=8
        night_charges=3
        compensation_dismissal=0        

        self.assertRaises(Months_workendExcepction, Settlementcalculator, base_salary, months_worked, annual_layoffs,
                                            interest_losses, bonus_services, vacation_days,
                                            extra_hours, night_charges, compensation_dismissal)

    # Caso de prueba 13: Empleado con salario base y beneficios retenidos durante disputa legal
    def test_13(self):
        base_salary = 6000000
        months_worked = 24
        annual_layoffs = 8.33
        interest_losses = 12 
        bonus_services = 8.33 
        vacation_days = 15 
        extra_hours = 8 
        night_charges = 3 
        compensation_dismissal = 0
        expected_liquidation= 7280035.32
        
        result = Settlementcalculator(base_salary, months_worked, annual_layoffs,
                                            interest_losses, bonus_services, vacation_days,
                                            extra_hours, night_charges, compensation_dismissal)

        valor_neto = result.Calculate_net_total(2000000)
        
        self.assertAlmostEqual(expected_liquidation, valor_neto, 2)

#Esto es para realizar las pruebas unitarias
if __name__ == '__main__':
    unittest.main()