import datetime

"""En este codigo se presenta un nivel de encapsulamiento privado, cada una de las clases creadas tienen atributos privados, de manera que para 
acceder a ellos por medio de los metodos setters y getters, estos metodos s dan pie para que los atributos privados se puedan usar en otras 
clases a manera de herencia, en este caso se uso como herencia todos los atrubutos y metodos de la clase Medicamento en la clase Mascota y en 
Sistema, dado que se puede hacer la herencia secuencialmnte, tambien todos los atributos y metodos de la clase Mascota se heredaron a la clase
sistema con el fin de usarlo, para cumplir con las tareas que se establecen en el menu de la  funcion main, en la cual se usa cada una de las 
clases inicalizandolas como objetos cuando se les asigna una varible y en la cual todos los atributos pueden ser usados gracias a que se inicialize
el construtor de las clases  """

"""En cuanto al polimorfismo se usa especialmente todos los metodos como verFechaIngreso, verMedicamento, eliminarMascota, 
eliminarMedicamento,que se definen en la clase base sistemaV. Estos metodos funcionan de manera similar independientemente 
de si se aplican a mascotas caninas o felinas, es decir pueden arrojar diferentes valores, dependiendo del objeto que se haya asociado a 
ellos y como se usaron, y por otro lado  los metodos como verFechaIngreso y verMedicamento devuelven resultados que pueden ser de diferentes
tipos (datetime o None) dependiendo de la situacion. Esto permite manejar de manera flexible diferentes escenarios en el codigo """



class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis =0
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=datetime #se usa datetime con el fin de que se ingrese correctamente  una fecha valida por medio de la libreria, y porteeriemnte en la funcion main se le pida la usuarion ingresar, dia, mes  y año
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:

    """En esta clase se hicieron cambios mayores ya que no se uso las estruturas de listas en el ingreso, la eliminacion y la obtencion de fechas 
    en caso de la obtencion de datos se hace por medio de las llaves del diccionario, ademas se hiciero condicionales con los cuales se espcifico
    como seria las funciones dependido del tipo de animal que se iba a ingresar, espcificamente en que diccioario  se iba a alamcenar, elijminar 
    o buscar """

    def __init__(self):
        self.__lista_Caninos={}
        self.__lista_Felinos={}

   
    def verificarExiste(self, historia, tipo):
        if tipo == 1:
            
            if historia in self.__lista_Caninos:
                return 'canino'
                return True
            else:
                return False
        elif tipo == 2:
            
            if historia == m.verHistoria():
                return 'felino'
                return True
            else:
                return False


        
    def verNumeroMascotas(self,tipo):
        if tipo==1:
            return len(self.__lista_Caninos)
        elif tipo==2:
            return len(self.__lista_Felinos) 
    
    def ingresarMascota(self,historia, mascota,tipo):
        
        if tipo==1:
            self.__lista_Caninos[historia]=mascota
            
        elif tipo==2:
            self.__lista_Felinos[historia]=mascota
   

    def verFechaIngreso(self, historia, tipo):
        if tipo == 1:
            if historia in self.__lista_Caninos:
                return self.__lista_Caninos[historia].verFecha()
            else:
                return None
        elif tipo == 2:
            if historia in self.__lista_Felinos:
                return self.__lista_Felinos[historia].verFecha()
            else:
                return None


    def verMedicamento(self,historia,tipo):
        
        if tipo==1:

            if historia in self.__lista_Caninos:
                return self.__lista_Caninos[historia].verLista_Medicamentos() 
            else:
                return None
        elif tipo==2:
            if historia in self.__lista_Felinos:
                return self.__lista_Felinos[historia].verLista_Medicamentos() 
            else:
                return None

    
    def eliminarMascota(self, historia,tipo):
        
        if tipo==1:
        
            if historia in self.__lista_Caninos:
                del self.__lista_Caninos[historia]  #opcion con el pop
                return True  #eliminado con exito

            return False 
        elif tipo==2:
            if historia in self.__lista_Felinos:
                del self.__lista_Felinos.remove[historia]  #opcion con el pop
                return True  #eliminado con exito
    
  

    def eliminarMedicamento(self, historia, tipo, nombre_medicamento):
        """El metodo se creo para crear la nueva opcion del menu que se solicito, es similar al de eliminarMascotas, con la excepcio que se usa 
        el atributo para ver la lista de medicamentos """
        if tipo == 1:
            for mascota in self.__lista_Caninos.values():
                if historia == mascota.verHistoria():
                    lista_medicamentos = mascota.verLista_Medicamentos()
                    for medicamento in lista_medicamentos:
                        if medicamento.verNombre() == nombre_medicamento:
                            lista_medicamentos.remove(medicamento)
                            return True  # Medicamento eliminado con exito
                    return False  # No se encontró el medicamento en la lista
            return False  # No se encontro la mascota con la historia clinica especificada
        elif tipo == 2:
            for mascota in self.__lista_Felinos.values():
                if historia == mascota.verHistoria():
                    lista_medicamentos = mascota.verLista_Medicamentos()
                    for medicamento in lista_medicamentos:
                        if medicamento.verNombre() == nombre_medicamento:
                            lista_medicamentos.remove(medicamento)
                            return True  # Medicamento eliminado con exito
                    return False  # No se encontró el medicamento en la lista
            return False  # No se encontró la mascota con la historia clínica especificada

    




def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        tipo=int(input("Ingrese tipo de mascota:1-canino\n2-felino"))

        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas(tipo) >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia, tipo) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                peso=int(input("Ingrese el peso de la mascota: "))
                dia=int(input("Ingrese el dia de ingreso:"))
                mes=int(input("Ingrese el mes de ingreso:"))
                año=int(input("Ingrese el año de ingreso:"))
                fecha=datetime.datetime(año, mes, dia )
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):

                    """En cuento a los cambio realizados, para la condicion de que no se pueden ingresar dos medicamentos con el mismo nombre, 
                    se uso un condiconal en el cual se uso medicamento.verNombre()  para vefificar que el nuevo medicamento que se va a 
                    ingresar no se encuentre en la lista."""         

                    while True: 
                        try:
                            nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                            medicamento_existente = False
                            for medicamento in lista_med:
                                if nombre_medicamentos == medicamento.verNombre():
                                    medicamento_existente = True
                                    break
                            if medicamento_existente:
                                print("El medicamento ya esta en la lista, ingrese otro nombre de medicamento ")
                                continue

                            dosis =int(input("Ingrese la dosis: "))
                            medicamento = Medicamento()
                            medicamento.asignarNombre(nombre_medicamentos)
                            medicamento.asignarDosis(dosis)
                            lista_med.append(medicamento)
                            break
                        except ValueError as e:
                            print(e)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(historia,mas,tipo)
                

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q, tipo)
            if fecha is not None:
                print("La fecha de ingreso de la mascota es:", fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas(tipo)
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q,tipo) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q,tipo) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:#Eliminar medicamento 
            g=int(input("Ingrese el numero de historia clinica: "))
            nombre_med=input("Ingrese nombre del medicament: ")
            resultado=servicio_hospitalario.eliminarMedicamento(g,tipo,nombre_med)
            if resultado_operacion == True:
                print("Medicamento eliminado del sistema con exito")
            else:
                print("No se ha podido eliminar el medicamento ")
    

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

