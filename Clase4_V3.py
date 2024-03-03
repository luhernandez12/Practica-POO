class Paciente:
    """En esta  clase se evidencia el nivel de encapsulamiento, los atributos son privados y por lo mismo son necesarios los metodos que permitan
    acceder a ellos """
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
     
    """se evidencia claramente el uso de setters y getter, tieniendo en claro que el encapsulamiento de la clase es de caracter privado,  
    cse crea estos metodos con el fin de usar otros atrubutos a en algunas clases ahorrando codigo y usando uno de los pilares de la
    programacion orientada a objetos, la herencia
    los metodos set ayudan a la asiganacion de los atributos privados de la clase y los get a retornar  la informacion que se almacenara en 
    el objeto creado  """
    #metodos get    
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    """ En esta clase se presenta claramente la herencia pues, para los metodos creados se usaron diferentes metodos de la clase Pacientes evidentemente
    heredadolos; el metodo verificarPcientes() y verDAtosPaciente() paciente usa el metodo verCedula() y verNombre() con el fin de obtener infomacion y manipularla para usarla 
    posteriormente, esto optizando el codigo y evitando hacer codigo de mas    """

    def __init__(self):
        self.__lista_pacientes = [] 
        
    
    def verificarPaciente(self, dato):
        for p in self.__lista_pacientes:
            if dato == p.verCedula() or dato == p.verNombre():       #se uso el atributo de la clase pacientes con el fin de que al verificar la existencia de un paciente en la lista tambien se haga por medio del nombre 
                return True
            else:
                partes = p.verNombre().split()   # tambien se uso el metodo ver nombre, pero esta vez se uso split con el fin de separ los nombre y apellidos, y postromente formateralos, para que al hacer la verificacion se pueda buscar al paciente tambien por el apellido o el nombre 
                nombre = partes[0]
                apellido = partes[-1]
                if dato in nombre or dato in apellido:
                    return True
        return False

    def verDatosPaciente(self, c):
        for p in self.__lista_pacientes:
            if c == p.verCedula() or c == p.verNombre():
                return p
            else: #se incluyo la opcion de verificacion y visucalizacion de la informacion del paciente por medio de las busquedas de su nombre o partes de este 
                partes = p.verNombre().split()
                nombre = partes[0]
                apellido = partes[-1]
                if c in nombre or c in apellido:
                    return p            #retorno del objeto que contiene la informacion del paciente de acuedo a la verificacion 
        return None

    
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True                

            
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 
        

def main():
    sis = Sistema()
    """creando el objeto Sistema() con la asignacion de una variable, hace que el construtor __int__ de la clase sistema se inicialize y junto con 
    ella todos lo atruburtos alli contenido, los cuales eran manipilados por medio de los metodos(setter y getters) en la siguientes 
    partes del codigo, """
    
    while True:
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> "))
         
        """se presenta recurrente uso de polimorfismos """
        
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
       
        elif opcion == 2:
            #1. solicito la cedula o algun nombre para verificar la informacion del paciente 
            men= int(input("Ingrese el numero segun del dato por el cual va a buscar: 1-Cedula \n 2.Nombre:  ")) 
             
            if men==1: #busqueda por medio de numero de cedula 
                c=int(input("Ingrese el numero de cedula: "))
                p = sis.verDatosPaciente(c) 
                #2. si encuentro al paciente imprimo los datos
                if p != None:
                    print("Nombre: " + p.verNombre()) 
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio()) 
                else:
                    print("No existe un paciente con esa cedula")
            
            elif men==2:     #busqueda por medio del nombre o partes de el 
                n=input("ingrese el nombre  ")
                p=sis.verDatosPaciente(n)
                if p !=None:
                    print("Nombre: " + p.verNombre()) 
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio()) 
                    
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
