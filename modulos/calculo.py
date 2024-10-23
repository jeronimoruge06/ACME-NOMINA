import json 
from registro import*
from datetime import datetime

def calcularNomina(identificacion, mes, año):

    try:
        empleados = cargarDatos(RutaEmpleados)
        if identificacion not in empleados:
            return None

        empleado = empleados[identificacion]
        salario = empleado["salario"]
        

        descuentoSalud = salario * 0.04
        descuentoPension = salario * 0.04
        

        SalarioMinimo = 1000000
        auxilioTransporte = 0
        if salario < (2 * SalarioMinimo):
            auxilioTransporte = salario * 0.10


        inasistencias = cargarDatos(RutaInasistencias)
        valor_dia = salario / 30
        totalInasistencias = 0
        
        if identificacion in inasistencias:
            for fecha in inasistencias[identificacion]:
                fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
                if fecha_obj.month == mes and fecha_obj.year == año:
                    totalInasistencias += 1
        
        descuentoInasistencias = valor_dia * totalInasistencias

        bonos = cargarDatos(RutaBonos)
        totalBonos = 0
        
        if identificacion in bonos:
            for bono in bonos[identificacion]:
                fecha_obj = datetime.strptime(bono["fecha"], "%Y-%m-%d")
                if fecha_obj.month == mes and fecha_obj.year == año:
                    totalBonos += bono["valor"]

        totalPagar = (salario + auxilioTransporte + totalBonos - 
                    descuentoSalud - descuentoPension - descuentoInasistencias)

        nomina = {
            "identificacion": identificacion,
            "nombre": empleado["nombre"],
            "cargo": empleado["cargo"],
            "salarioBase": salario,
            "auxilioTransporte": auxilioTransporte,
            "descuentoSalud": descuentoSalud,
            "descuentoPension": descuentoPension,
            "descuentoInasistencias": descuentoInasistencias,
            "totalBonos": totalBonos,
            "totalPagar": totalPagar
        }

        nombre_archivo = f"nomina_{identificacion}_{mes}_{año}.json"
        with open(f"datos/{nombre_archivo}", 'w') as f:
            json.dump(nomina, f, indent=4)

        return nomina
    except Exception as e:
        print(f"Error al calcular nómina: {str(e)}")
        return None