dinero = 0
lista_nivel1= [{'Pregunta':"¿Cuál es el próximo número en la secuencia: 2, 4, 6, 8, _?",'Opciones: ':"A. 10 \nB. 15 \nC. 20", 'Respuesta':"A"},
         {'Pregunta':"Si todos los gatos son animales y todos los leones son gatos, ¿todos los leones son animales?",'Opciones: ':"A. Verdadero \nB. Falso",'Respuesta':"B"},
         {'Pregunta':"¿Cuál de estos no pertenece al grupo: manzana, naranja, zanahoria?",'Opciones: ':"A. Manzana \nB. Zanahoria \nC. Naranja",'Respuesta':"B"},
         {'Pregunta':"Si siempre llueve cuando hay nubes en el cielo, y hoy hay nubes en el cielo, ¿Hoy va a llover?",'Opciones: ':"\nA. Verdadero \nB. Falso" ,'Respuesta':"B"},
         {'Pregunta':"Si 5 manzanas cuestan 10 dólares, ¿cuánto cuestan 15 manzanas?",'Opciones: ':"A. 15 \nB. 30\nC. 12",'Respuesta':"B"}]
pistas1=["El numero es par","¿Los leones son gatos?","No es fruta", "No siempre llueve","Multiplica y venceras"]     
def oro (valor, resta):
    valor+=dinero
    valor -=resta
    return valor
     
def nivel1():
    global dinero
    puntaje=0
    contador =0
    for h in lista_nivel1:
        
        pregunta = h['Pregunta']
        opciones = h['Opciones: ']
        respuesta = h['Respuesta']
        print(pregunta)
        print(opciones)
        guardada = input("Ingrese su respuesta ").upper()
        
        if guardada == respuesta:
            print("Respuesta correcta")
            puntaje +=1
            dinero +=250
        elif guardada == "S":
            
            quita = 100
            pierdo =oro(0,0)
            print(oro(0,0))
            if quita > pierdo:
                print("No te alcanza el dinero")
                oro(0,quita)
            else:
                pista =pistas1[contador]
                print(pista)
                guardada = input("Ingrese su respuesta ").upper()    
        else:
            print("Respuesta incorrecta")
            print(pistas1[contador])
            guardada = input("Ingrese su respuesta ").upper()
            if guardada == respuesta:
               print("Respuesta correcta") 
        contador+=1
    oro(dinero,0)
    return puntaje

# lista_nivel2 = [{'pregunta': "Si me tumbas, soy todo. Si me cortas por la cintura, me quedo en nada. ¿Qué soy?", 'respuesta': "8"},
#           {'pregunta': "¿Cuántos ladrillos se necesitan para completar un edificio hecho de ladrillos?", 'respuesta': "1"},
#           {'pregunta': "20+20+20=60. ¿Cómo puedes hacer 60 nuevamente usando el mismo número 3 veces?", 'respuesta': "55+5"},
#           {'pregunta': "¿Cuál es el siguiente número de esta serie: 3.829, 9.382, 2.938…?", 'respuesta': "8.293"},
#           {'pregunta': "Encuentra el número de cuatro dígitos en el que el primer dígito es un cuarto del último dígito, el segundo dígito es 6 veces el primer dígito y el tercer dígito es el segundo dígito más 3. ¿Cuál es?", 'respuesta': "1694"}]

# pistas2 = ["Es un número par", "Es un número impar", "La multiplicación de los números da 125", "Mueve a izquierda", "Empieza en 1"]

# def nivel2():
#     global dinero
#     puntaje = 0
#     for elemento in lista_nivel2:
#         print()
#         pregunta = elemento['pregunta']
#         respuesta_correcta = elemento['respuesta']
#         print("Pregunta")
#         print(pregunta)
#         respuesta = input("Respuesta: ")
        
#         if respuesta == respuesta_correcta:
#             print("Respuesta correcta")
#             dinero +=250
#             puntaje += 1
#         else:
#             print("Respuesta incorrecta")
            
#     oro(dinero,0)
#     return puntaje
            
# lista_nivel3= [{'Pregunta':"¿Cuál es el próximo número en la secuencia: 1, 4, 9, 16, _?",'Opciones: ':"A. 20  \nB. 25  \nC. 30", 'Respuesta':"B"},
#          {'Pregunta':"Si todos los perros son mamíferos y todos los mamíferos respiran aire, ¿todos los perros respiran aire? ",'Opciones: ':"A. Verdadero \nB. Falso",'Respuesta':"A"},
#          {'Pregunta':"¿Cuál de estos no pertenece al grupo: pi, e, phi, 2?",'Opciones: ':"A. pi  \nB. e  \nC. 2",'Respuesta':"C"},
#          {'Pregunta':"Si siempre hace calor cuando el sol brilla y hoy hace calor, ¿está brillando el sol hoy?",'Opciones: ':"\nA. Verdadero \nB. Falso" ,'Respuesta':"V"},
#          {'Pregunta':" Si 5 manzanas y 3 naranjas cuestan 8 dólares, ¿cuánto cuestan 10 manzanas y 6 naranjas?",'Opciones: ':"A. 10  \nB. 15 \nC. 16 ",'Respuesta':"C"}]
        
# def nivel3():
#     puntaje=0
#     contador =0
#     global dinero
#     for h in lista_nivel1:
        
#         pregunta = h['Pregunta']
#         opciones = h['Opciones: ']
#         respuesta = h['Respuesta']
#         print(pregunta)
#         print(opciones)
#         guardada = input("Ingrese su respuesta \nSi deseas una pista digita S ").upper()
#         if guardada == "S":
#             pista =pistas1[contador]
#             print(pista)
#             guardada = input("Ingrese su respuesta ").upper()
#             if guardada == respuesta:
#                 print("Respuesta correcta")
#                 puntaje +=1
#                 dinero+=250
#             else:
#                 print("Respuesta incorrecta")
#         elif guardada == respuesta:
#             print("Respuesta correcta")
#             puntaje +=1
#         else:
#             print("Respuesta incorrecta")
#         contador+=1
#     return puntaje

# lista_nivel4 = [{'pregunta': "Tom mide 1,80, es ayudante en una carnicería y lleva zapatos de la talla 45. ¿Qué pesa?", 'respuesta': "carne"},
#           {'pregunta': "El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía.", 'respuesta': "ataud"},
#           {'pregunta': "¿Qué es lo que no está ni dentro ni fuera de la casa, pero que es necesario para cualquier hogar?", 'respuesta': "ventanas"},
#           {'pregunta': "Si lo tengo, no lo comparto. Si la comparto, no lo tengo. ¿Qué es?", 'respuesta': "secreto"},
#           {'pregunta': "El día anterior a dos días después del día anterior a mañana es sábado. ¿Qué día es hoy?", 'respuesta': "viernes"}]

# pistas4 = ["Es una alimento", "Lo usan los vampiros", "Se puede mirar a través de este", "Es un s...", "Dia antes del fin de semana"]

# def nivel4():
#     puntaje = 0
#     global dinero
#     for elemento in lista_nivel2:
#         print()
#         pregunta = elemento['pregunta']
#         respuesta_correcta = elemento['respuesta']
#         print("Pregunta")
#         print(pregunta)
#         respuesta = input("Respuesta: ").lower
        
#         if respuesta == respuesta_correcta:
#             print("Respuesta correcta")
#             dinero+=250
#             puntaje += 1
#         else:
#             print("Respuesta incorrecta")
    
#     return puntaje

# lista_nivel5 = [{'pregunta': "Tom mide 1,80, es ayudante en una carnicería y lleva zapatos de la talla 45. ¿Qué pesa?", 'respuesta': "carne"},
#           {'pregunta': "El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía.", 'respuesta': "ataud"},
#           {'pregunta': "¿Qué es lo que no está ni dentro ni fuera de la casa, pero que es necesario para cualquier hogar?", 'respuesta': "ventanas"},
#           {'pregunta': "Si lo tengo, no lo comparto. Si la comparto, no lo tengo. ¿Qué es?", 'respuesta': "secreto"},
#           {'pregunta': "El día anterior a dos días después del día anterior a mañana es sábado. ¿Qué día es hoy?", 'respuesta': "viernes"}]

# pistas5 = ["Es una alimento", "Lo usan los vampiros", "Se puede mirar a través de este", "Es un s...", "Dia antes del fin de semana"]

# def nivel5():
#     puntaje = 0
#     global dinero
#     for elemento in lista_nivel2:
#         print()
#         pregunta = elemento['pregunta']
#         respuesta_correcta = elemento['respuesta']
#         print("Pregunta")
#         print(pregunta)
#         respuesta = input("Respuesta: ").lower
        
#         if respuesta == respuesta_correcta:
#             print("Respuesta correcta")
#             dinero+=250
#             puntaje += 1
#         else:
#             print("Respuesta incorrecta")
    
#     return puntaje

nivel1()
# nivel2()
print(oro(0,0))