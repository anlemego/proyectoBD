import utils.conexion_BD as conn
from utils.entidades import Vehiculo
import mysql.connector

class vehiculos_bd:
    def buscar(self, matricula):
        self.con = conn.conection().connect()
        self.cursor1 = self.con.cursor()
        sql = "SELECT matricula, modelo, marca, color, cliente_id FROM vehiculos WHERE matricula = %s "
        self.cursor1.execute(sql, (matricula,))
        resultado = self.cursor1.fetchone()
        self.con.close()     
        if resultado:
            return resultado
        else:
            return False
        
    def guardar(self,vehiculo:Vehiculo):
        try:
            self.con = conn.conection().connect()
            self.cursor1 = self.con.cursor()
            sql = """
            INSERT INTO vehiculos
            (matricula, modelo, marca, color, cliente_id)
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                vehiculo.get_matricula(),
                vehiculo.get_modelo(),
                vehiculo.get_marca(),
                vehiculo.get_color(),
                vehiculo.get_cliente_id()
            )
            self.cursor1.execute(sql,valores)
            resultado = self.cursor1.fetchone()
            self.con.commit()
            self.con.close() 

            return True, "Vehículo guardado correctamente"
        
        except mysql.connector.Error as e:
            if e.errno == 1062:
                return False, "La matrícula ya existe"

            elif e.errno == 1452:
                return False, "El cliente_id no existe"

            return False, f"Error MariaDB: {e}"