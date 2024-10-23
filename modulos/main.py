from registro import* 
from calculo import*
import time

def menu():
    print("""
==============================================
                ---ACME---
                  NOMINA 
==============================================

1. Registro de empleados 
2. Registro de inasistencias 
3. Registro de bonos extra-legales
4. Calculo de la nomina 
0. Salir
""")
    return input("Ponga una opción que desea abrir : ")

    crear_archivos()
    
while True:
    try:
        opcion = menu()
        
        if opcion == "1":
            print('''
==============================================
                ---ACME---
            REGISTRO DE EMPLEADO 
==============================================
''')
            identificacion = input("Ingrese identificación: ").strip()
            nombre = input("Ingrese nombre: ").capitalize()
            cargo = input("Ingrese cargo: ").lower()
            salario = float(input("Ingrese salario: "))
            time.sleep(2)
            print(registrarEmpleado(identificacion, nombre, cargo, salario))

        elif opcion == "2":
            print('''
==============================================
                ---ACME---
        REGISTRO DE INASISTENCIAS 
==============================================
''')
            identificacion = input("Ingrese identificación: ").strip()
            fecha = input("Ingrese fecha (YYYY-MM-DD)y que especifique con un - por cada fecha : ")
            time.sleep(2)
            print(registrarInasistencia(identificacion,fecha))

        elif opcion == "3":
            print('''
==============================================
                ---ACME---
        REGISTRO DE BONOS EXTRA-LEGALES 
==============================================
''')
            identificacion = input("Ingrese identificación: ").strip()
            fecha = input("Ingrese fecha (YYYY-MM-DD) y que especifique con un - por cada fecha : ")
            valor = float(input("Ingrese valor del bono: "))
            concepto = input("Ingrese concepto del bono: ")
            time.sleep(2)
            print(registrarBono(identificacion, fecha, valor, concepto))

        elif opcion == "4":
            print('''
==============================================
                ---ACME---
            CALCULO DE NOMINA 
==============================================
''')
            identificacion = input("Ingrese identificación: ").strip()
            mes = int(input("Ingrese mes (1-12): "))
            año = int(input("Ingrese año: "))
            nomina = calcularNomina(identificacion, mes, año)
            
            if nomina:
                print(f"Empleado: {nomina['nombre']}")
                print(f"Cargo: {nomina['cargo']}")
                print(f"Salario base: ${nomina['salarioBase']}")
                print(f"Auxilio transporte: ${nomina['auxilioTransporte']}")
                print(f"Descuento salud: ${nomina['descuentoSalud']}")
                print(f"Descuento pensión: ${nomina['descuentoPension']}")
                print(f"Descuento inasistencias: ${nomina['descuentoInasistencias']}")
                print(f"Total bonos: ${nomina['totalBonos']}")
                print(f"Total a pagar: ${nomina['totalPagar']}")

        elif opcion == "0":
            print("FINALIZANDO EL PROGRAMA, GRACIAS POR USAR EL SISTEMA")
            time.sleep(2)
            break
            
        else:
            print("Opción no válida, ingrese una funcion que se encuentre en el menu ")
            
    except ValueError as e:
        print("Error: Ingrese un valor válido")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

