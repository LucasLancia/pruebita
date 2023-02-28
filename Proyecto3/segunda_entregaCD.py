class Cliente:

    def __init__(self,nombre,apellido,dni,telefono):

        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.telefono=telefono

    def comprar(self,articulo):
        print(f"{self.nombre, self.apellido} ha comprado el siguiente articulo {articulo}.")

    def pedir_devolucion(self,articulo):

        print(f"{self.nombre, self.apellido} ha devuelvo el articulo {articulo} ")

    def __str__(self):

        return (f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Telefono: {self.telefono}")
