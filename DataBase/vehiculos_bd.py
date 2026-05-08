import utils.conexion_BD as conn
import utils.entidades as entidades

class vehiculos_bd:
    def BuscarPorCliente(self, Cliente):
        self.con = conn.conection().connect()
        self.cursor1 = self.con.cursor()
        sql = "SELECT matricula, marca, modelo, color, cliente_id FROM vehiculos WHERE cliente_id = %s"
        self.cursor1.execute(sql, (Cliente.get_cliente_id(),))
        resultados = self.cursor1.fetchall()
        
        lista_vehiculos = []
        for res in resultados:
            v = entidades.Vehiculo()
            v.set_matricula(res[0])
            v.set_marca(res[1])
            v.set_modelo(res[2])
            v.set_color(res[3])
            v.set_cliente_id(res[4])
            lista_vehiculos.append(v)
            
        self.con.close()
        return lista_vehiculos

    def BuscarPorMatricula(self, Vehiculo):
        self.con = conn.conection().connect()
        self.cursor1 = self.con.cursor()
        sql = "SELECT matricula, marca, modelo, color, cliente_id FROM vehiculos WHERE matricula = %s"
        self.cursor1.execute(sql, (Vehiculo.get_matricula(),))
        resultado = self.cursor1.fetchone()
        self.con.close()

        if resultado:
            v = entidades.Vehiculo()
            v.set_matricula(resultado[0])
            v.set_marca(resultado[1])
            v.set_modelo(resultado[2])
            v.set_color(resultado[3])
            v.set_cliente_id(resultado[4])
            return v
        return None
