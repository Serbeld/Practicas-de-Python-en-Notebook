# -*- coding: utf-8 -*-

def buscar_un_paciente(id, diccionario):
    
    try:
        
        valor_de_prueba_de_errores = diccionario[id]['Nombre']
        
        print("***** INFORMACIÓN DEL PACIENTE *****")
        print("Nombre: " + str(diccionario[id]['Nombre']))
        print("Id: " + str(diccionario[id]['Id']))
        print("Género: " + str(diccionario[id]['Sexo']))
        print("EPS: " + str(diccionario[id]['EPS']))
        print("*** Información del perfil lipídico ***")
        print("COL TOTAL: " + str(diccionario[id]['Perfil lipídico']['COLT']))
        print("HDL: " + str(diccionario[id]['Perfil lipídico']['HDL']))
        print("LDL: " + str(diccionario[id]['Perfil lipídico']['LDL']))
        print("Triglicéridos: " + str(diccionario[id]['Perfil lipídico']['TRIG']))
        print("*** Información de diabetes ***")
        print("HbA1C: " + str(diccionario[id]['Diabetes']['HbA1c']))
        print("Glucosa: " + str(diccionario[id]['Diabetes']['Glucosa']))
    
    except:
        
        print( "El paciente no existe en la base de datos")