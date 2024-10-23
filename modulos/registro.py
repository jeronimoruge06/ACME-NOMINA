import json
from datetime import datetime
import os

# Rutas de archivos
RutaEmpleados = "datos/empleados.json"
RutaInasistencias = "datos/inasistencias.json"
RutaBonos = "datos/bonos.json"

def crearArchivos():
    """Crea los archivos necesarios si no existen"""
    try:
        os.makedirs("datos", exist_ok=True)
        for ruta in [RutaEmpleados, RutaInasistencias, RutaBonos]:
            if not os.path.exists(ruta):
                with open(ruta, 'w') as f:
                    json.dump({}, f)
    except Exception as e:
        print(f"Error al crear archivos: {str(e)}")
#=========================================================================================#

def cargarDatos(ruta):
    """Carga datos desde un archivo JSON"""
    try:
        with open(ruta, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

#=========================================================================================#
def guardarDatos(datos, ruta):
    """Guarda datos en un archivo JSON"""
    try:
        with open(ruta, 'w') as f:
            json.dump(datos, f, indent=4)
    except Exception as e:
        print(f"Error al guardar datos: {str(e)}")

#=========================================================================================#
def registrarEmpleado(identificacion, nombre, cargo, salario):

    try:
        empleados = cargarDatos(RutaEmpleados)
        if identificacion in empleados:
            return "El codigo del empleado ya existe"
        
        empleados[identificacion] = {
            "nombre": nombre,
            "cargo": cargo,
            "salario": float(salario)
        }
        guardarDatos(empleados, RutaEmpleados)
        return "Empleado registrado exitosamente"
    except Exception as e:
        return f"Error al registrar empleado: {str(e)}"

#=========================================================================================#
def registrarInasistencia(identificacion, fecha):
    
    try:
        empleados = cargarDatos(RutaEmpleados)
        if identificacion not in empleados:
            return "Empleado no encontrado"

        inasistencias = cargarDatos(RutaInasistencias)
        if identificacion not in inasistencias:
            inasistencias[identificacion] = []
        
        inasistencias[identificacion].append(fecha)
        guardarDatos(inasistencias, RutaInasistencias)
        return "Inasistencia registrada exitosamente"
    except Exception as e:
        return f"Error al registrar inasistencia: {str(e)}"

#=========================================================================================#
def registrarBono(identificacion, fecha, valor, concepto):
    
    try:
        empleados = cargarDatos(RutaEmpleados)
        if identificacion not in empleados:
            return "Empleado no encontrado"

        bonos = cargarDatos(RutaBonos)
        if identificacion not in bonos:
            bonos[identificacion] = []
        
        bonos[identificacion].append({
            "fecha": fecha,
            "valor": float(valor),
            "concepto": concepto
        })
        guardarDatos(bonos, RutaBonos)
        return "Bono registrado exitosamente"
    except Exception as e:
        return f"Error al registrar bono: {str(e)}"
    

