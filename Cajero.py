class Producto():
    def __init__(self,codigo,nombre,precio):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__precio=precio
    
    #geters
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def precio(self):
        return self.__precio
    
    #Seterrs
    
    @codigo.setter
    def codigo(self,new_code):
        self.__codigo=new_code
        return self.__codigo
    
    @nombre.setter
    def nombre(self,new_name):
        self.__nombre=new_name
        return self.__nombre
        
    @precio.setter
    def precio(self, new_price):
        self.__precio=new_price
        return self.__precio
    
    def __str__(self):
        return f"Codigo:{self.__codigo} Nombre:{self.__nombre} Precio:{self.__precio}"
    
    def Calcular_precio_por_unidades(self,unindades):
        return self.__precio * unindades
    
class Almacen():
    def __init__(self):
        self.__inventario={} # {codigo: (producto, cantidad)}
    
    #getter
    @property
    def inventario(self):
        return self.__inventario
    
    def Agregar_producto(self,producto,cantidad):# producto=clase producto
        if producto.codigo in self.__inventario:
            self.__inventario[producto.codigo][1]+=cantidad
        
        else:
            self.__inventario[producto.codigo]=[producto,cantidad]
        
    def Eliminiar_producto(self,producto,cantidad):
        if producto.codigo in self.__inventario: #Revisa si esta el producto en el invetario
            if self.__inventario[producto.codigo][1]>=cantidad: #Verifica si es posible restar la cantidad
                self.__inventario[producto.codigo][1]-=cantidad
            elif self.__inventario[producto.codigo][1]==cantidad:#Si la cantidad a eliminar es igual se elimina del inventario
                del self.__inventario[producto.codigo]
            else:
                print(f"La cantidad del producto {producto.nombre} es insuficiente para esta operación")      
        else:
            print(f"El producto {producto.nombre} no se encuentra en el inventario")
            
    def mostrar_inventario(self):
        if not self.__inventario:
            print("Inventario vacio")
            return 
        
        maxima_longitud=max(len(str(valor[0].nombre)) for claves,valor in self.__inventario.items())+2#Calculamos la longitud del nombre 
        
        titulo=(f"{'Código':<10}{'Producto':<{maxima_longitud}} ----> {'Disponible':>10} unidades")
        print(titulo)
        print('-' * len(titulo))
        for p,c in self.__inventario.items():
            print(f"{str(p):<10}{str(c[0].nombre):<{maxima_longitud}} ----> {c[1]:>10} unidades")
        print('-' * len(titulo))        
            
class Iterface():
    def __init__(self,Inventario):
        self.__Inventario=Inventario
        self.__voleta={}
        
    @property
    def voleta(self):
        return self.__voleta
    @voleta.setter
    def baucher(self,new_voleta):
        self.__voleta=new_voleta
        return self.__voleta
    
    def agrega_producto(self,producto,cantidad):
        if producto.codigo in self.__Inventario.inventario:#Verificamos si el producto se encuentra en el inventario principal con el objeto de clase convertido en diccionario
            if self.__Inventario.inventario[producto.codigo][1]>=cantidad:
                self.__Inventario.Eliminiar_producto(producto,cantidad)
                if producto.codigo in self.__voleta:
                   self.__voleta[producto.codigo][1]+=cantidad
                else:
                   self.__voleta[producto.codigo]=[producto,cantidad]
            else:
                print(f"La cantidad del producto {producto.nombre} es insuficiente para esta operación")    
            
        else:
            print(F"El producto {producto.nombre} no esta disponible en el inventario")
    
    def eliminar_producto(self,producto,cantidad):
        if producto.codigo in self.__voleta:
            if cantidad < self.__voleta[producto.codigo][1]:#si la cantidad es mayor a las unidades del producto en la voleta
                self.__voleta[producto.codigo][1]-=cantidad
            elif cantidad >= self.__voleta[producto.codigo][1]:
                del self.__voleta[producto.codigo]
            self.__Inventario.Agregar_producto(producto,cantidad)
        else:
            print(F"El producto {producto.nombre} no esta en tu lista de pedidos")
            
    def mostrar_voleta(self):
        if not self.__voleta:
            print("Voleta vacia")
            return 
        
        maxima_longitud=max(len(str(valor[0].nombre)) for claves,valor in self.__voleta.items())+2#Calculamos la longitud del nombre 
        
        titulo=(f"{'Código':<10}{'Producto':<{maxima_longitud}} ----> {'Disponible':>10} unidades")
        print(titulo)
        print('-' * len(titulo))
        for p,c in self.__voleta.items():
            print(f"{str(p):<10} {str(c[0].nombre) :<{maxima_longitud}} ----> {c[1]:>10} unidades")
        print('-' * len(titulo))  
        
                

#pruebas
Pollo=Producto(759368,"Pollo",10)
Carne=Producto(758984,"Carne",15)
Polo=Producto(789451,"Polo",15) 
Manzana=Producto(789541,"Manzana",50)



Despensa=Almacen()
Despensa.Agregar_producto(Pollo,40)
Despensa.Agregar_producto(Carne,50)
Despensa.Agregar_producto(Polo,400)
Despensa.Agregar_producto(Pollo,10)
Despensa.mostrar_inventario()


Baucher=Iterface(Despensa)
Baucher.agrega_producto(Pollo,100)
Baucher.agrega_producto(Carne,10)
Baucher.agrega_producto(Polo,50)
Baucher.eliminar_producto(Manzana,20)
Baucher.mostrar_voleta()

Despensa.mostrar_inventario()



#funcion principal
print("Tienda Angel:")
print('''
¿Qué acción desea realizar?
Ingrese A para añadir productos a su boleta de compra.
Ingrese E para eliminar productos de su boleta de compra.
Ingrese C para crear un nuevo producto e incluirlo en el inventario.
Ingrese V para visualizar su boleta de compra.
Ingrese I para ver el inventario de productos de la tienda.
Ingrese S para salir del programa.
''')


def Accion():
 while True:   
  accion=input("Accion a tomar?:").strip()
  if accion.lower()  in ["a","c","v","i","s","e"]:  
     print("\n")
     print("Productos disponible:")
     return accion
  else:
    print("Porfavor Ingresa una de las opcciones")
    
def main_funcion():
    while True:
     accion=Accion().lower()
    
     if accion == "a":
         while True:
            try:
                codigo = int(input("Ingrese el código del producto: "))
                cantidad = int(input("Ingrese la cantidad que desea agregar: "))
                # Verificar si el código existe en el inventario
                if codigo in Despensa.inventario:
                    producto=Despensa.inventario[codigo][0]
                    Baucher.agrega_producto(producto,cantidad)
                    Baucher.mostrar_voleta()
                    break
                else:
                    print(f"El codigo ingresado no es parte de ningun producto")
                    break
                
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para el código y la cantidad.")
                
     elif accion == "e":
         while True:
            try:
                codigo = int(input("Ingrese el código del producto: "))
                cantidad = int(input("Ingrese la cantidad que desea eliminar: "))
                # Verificar si el código existe en el inventario
                if codigo in Despensa.inventario:
                    producto=Despensa.inventario[codigo][0]
                    Baucher.eliminar_producto(producto,cantidad)
                    Baucher.mostrar_voleta()
                    break
                else:
                    print(f"El codigo ingresado no es parte de ningun producto")
                    break
                
            except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para el código y la cantidad.")

     elif accion=="c":
         while True:
             try:
              codigo=int(input("Ingresa el codigo del producto:").strip())
              nombre=input("Ingresa el nombre del producto:").strip()
              precio=int(input("Igresa el precio del producto:").strip())
              cantidad=int(input("Ingresa la cantidad de productos:").strip())
              
              if codigo in Despensa.inventario:
                  print(f"El codido {codigo} ya se encuentra asignado a otro producto")
                  break
              else:
                  Nuevo_producto=Producto(codigo,nombre,precio)
                  Despensa.Agregar_producto(Nuevo_producto,cantidad)
                  print(f"El producto {nombre} fue creado exitosamente")
                  Despensa.mostrar_inventario()
                  break   
             except ValueError:
                print("Entrada inválida. Asegúrese de ingresar números para el código, la cantidad y el.")

               
     elif accion=="v":
         Baucher.mostrar_voleta()
         
     elif accion=="i":
         Despensa.mostrar_inventario()
                
     elif accion=="s":
         print("Gracias por su compra")
         break
                             
main_funcion()
    
            


                        
