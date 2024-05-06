dinero = 0
respuestas_correctas = 0
respuestas_incorrectas = 0
respuestas_incorrectas_pista = 0
pistas = 2
puntaje=0
contador =0
total_dinero = 0

lista_nivel1= [{'Pregunta':"¿Cuál es el próximo número en la secuencia: 2, 4, 6, 8, _?",'Opciones: ':"A. 10 \nB. 15 \nC. 20", 'Respuesta':"A"},
         {'Pregunta':"Si todos los gatos son animales y todos los leones son gatos, ¿todos los leones son animales?",'Opciones: ':"A. Verdadero \nB. Falso",'Respuesta':"B"},
         {'Pregunta':"¿Cuál de estos no pertenece al grupo: manzana, naranja, zanahoria?",'Opciones: ':"A. Manzana \nB. Zanahoria \nC. Naranja",'Respuesta':"B"},
         {'Pregunta':"Si siempre llueve cuando hay nubes en el cielo, y hoy hay nubes en el cielo, ¿Hoy va a llover?",'Opciones: ':"A. Verdadero \nB. Falso" ,'Respuesta':"B"},
         {'Pregunta':"Si 5 manzanas cuestan 10 dólares, ¿cuánto cuestan 15 manzanas?",'Opciones: ':"A. 15 \nB. 30\nC. 12",'Respuesta':"B"}]
pistas1=["El numero es par","¿Los leones son gatos?","No es fruta", "No siempre llueve","Multiplica y venceras"]

def oro (valor, resta):
    valor -=resta
    return valor

def reiniciar_juego(nivel):
    resp_reiniciar = input("¿Desea reiniciar el nivel? Escriba 'S' para reiniciar el juego: ").lower()
    print("Si lo hace se le restaran 500 de oro")
    if resp_reiniciar == "s":
        total_dinero = oro(dinero, 500)
        print("Dinero: ", total_dinero)
        if nivel == 1:
            nivel1()
        elif nivel == 2:
            nivel2()
        elif nivel == 3:
            nivel3()
        elif nivel == 4:
            nivel4()
        elif nivel == 5:
            nivel5()
        print("Juego reiniciado")
    else:
        print("Juego terminado")
        
    return resp_reiniciar
      
def nivel1():
    global dinero, respuestas_incorrectas, respuestas_correctas, respuestas_incorrectas_pista, puntaje, pistas, contador, pistas, puntaje
    dinero = total_dinero
    puntaje = 0
    respuestas_incorrectas = 0
    respuestas_incorrectas_pista = 0
    for h in lista_nivel1:
        pregunta = h['Pregunta']
        opciones = h['Opciones: ']
        respuesta = h['Respuesta']
        print("\nPregunta")
        print(pregunta)
        print(opciones)
        guardada = input("Ingrese su respuesta ").upper()
        if guardada == respuesta:
            print("Respuesta correcta")
            puntaje +=15
            dinero += 250
            respuestas_correctas += 1
            print("Dinero ganado: ", dinero)
            print("Puntaje: ", puntaje)
        else:
            print("Respuesta incorrecta")
            respuestas_incorrectas += 1
            puntaje -= 5
            print("Dinero ganado: ", dinero)
            print("Puntaje: ", puntaje)
            if pistas > 0:
                resp_pista = input("¿Desea obtener una pista?. Escriba 'S' para obtener la pista: ").lower()
                if resp_pista == "s":
                    pistas -= 1
                    print(pistas1[contador])
                    guardada = input("Ingrese su respuesta ").upper()
                    if guardada == respuesta:
                        respuestas_correctas += 1
                        puntaje += 5
                        print("Respuesta correcta")
                        print("Dinero ganado: ", dinero)
                        print("Puntaje: ", puntaje)
                    else:
                        respuestas_incorrectas_pista += 1
                        puntaje -= 5
                        print("Respuesta incorrecta")
                        print("Dinero ganado: ", dinero)
                        print("Puntaje: ", puntaje)
                else:
                    print("Juego terminado")
                    print("Dinero ganado: ", dinero)
                    print("Puntaje: ", puntaje)
                    break
            elif pistas == 0:
                reiniciar_juego(1)
        contador+=1
    if respuestas_incorrectas >= 3 and respuestas_incorrectas_pista > 2:
        reiniciar_juego(1)
    else:
        print("\n¡Felicidades, puedes pasar al siguiente nivel!")
    return puntaje

lista_nivel2 = [{'pregunta': "Si me tumbas, soy todo. Si me cortas por la cintura, me quedo en nada. ¿Qué soy?", 'respuesta': "8"},
          {'pregunta': "¿Cuántos ladrillos se necesitan para completar un edificio hecho de ladrillos?", 'respuesta': "1"},
          {'pregunta': "20+20+20=60. ¿Cómo puedes hacer 60 nuevamente usando el mismo número 3 veces?", 'respuesta': "55+5"},
          {'pregunta': "¿Cuál es el siguiente número de esta serie: 3.829, 9.382, 2.938…?", 'respuesta': "8.293"},
          {'pregunta': "Encuentra el número de cuatro dígitos en el que el primer dígito es un cuarto del último dígito, el segundo dígito es 6 veces el primer dígito y el tercer dígito es el segundo dígito más 3. ¿Cuál es?", 'respuesta': "1694"}]

pistas2 = ["Es un número par", "Es un número impar", "La multiplicación de los números da 125", "Mueve a izquierda", "Empieza en 1"]

def nivel2():
    global dinero
    puntaje = 0
    for elemento in lista_nivel2:
        print()
        pregunta = elemento['pregunta']
        respuesta_correcta = elemento['respuesta']
        print("Pregunta")
        print(pregunta)
        respuesta = input("Ingrese su respuesta: ")
        
        if respuesta == respuesta_correcta:
            print("Respuesta correcta")
            dinero +=250
            puntaje += 1
        else:
            print("Respuesta incorrecta")
            
    oro(dinero,0)
    return puntaje
            
lista_nivel3= [{'Pregunta':"¿Cuál es el próximo número en la secuencia: 1, 4, 9, 16, _?",'Opciones: ':"A. 20  \nB. 25  \nC. 30", 'Respuesta':"B"},
         {'Pregunta':"Si todos los perros son mamíferos y todos los mamíferos respiran aire, ¿todos los perros respiran aire? ",'Opciones: ':"A. Verdadero \nB. Falso",'Respuesta':"A"},
         {'Pregunta':"¿Cuál de estos no pertenece al grupo: pi, e, phi, 2?",'Opciones: ':"A. pi  \nB. e  \nC. 2",'Respuesta':"C"},
         {'Pregunta':"Si siempre hace calor cuando el sol brilla y hoy hace calor, ¿está brillando el sol hoy?",'Opciones: ':"\nA. Verdadero \nB. Falso" ,'Respuesta':"V"},
         {'Pregunta':" Si 5 manzanas y 3 naranjas cuestan 8 dólares, ¿cuánto cuestan 10 manzanas y 6 naranjas?",'Opciones: ':"A. 10  \nB. 15 \nC. 16 ",'Respuesta':"C"}]
        
def nivel3():
    puntaje=0
    contador =0
    global dinero
    for h in lista_nivel1:
        
        pregunta = h['Pregunta']
        opciones = h['Opciones: ']
        respuesta = h['Respuesta']
        print(pregunta)
        print(opciones)
        guardada = input("Ingrese su respuesta \nSi deseas una pista digita S ").upper()
        if guardada == "S":
            pista =pistas1[contador]
            print(pista)
            guardada = input("Ingrese su respuesta ").upper()
            if guardada == respuesta:
                print("Respuesta correcta")
                puntaje +=1
                dinero+=250
            else:
                print("Respuesta incorrecta")
        elif guardada == respuesta:
            print("Respuesta correcta")
            puntaje +=1
        else:
            print("Respuesta incorrecta")
        contador+=1
    return puntaje

lista_nivel4 = [{'pregunta': "Tom mide 1,80, es ayudante en una carnicería y lleva zapatos de la talla 45. ¿Qué pesa?", 'respuesta': "carne"},
          {'pregunta': "El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía.", 'respuesta': "ataud"},
          {'pregunta': "¿Qué es lo que no está ni dentro ni fuera de la casa, pero que es necesario para cualquier hogar?", 'respuesta': "ventanas"},
          {'pregunta': "Si lo tengo, no lo comparto. Si la comparto, no lo tengo. ¿Qué es?", 'respuesta': "secreto"},
          {'pregunta': "El día anterior a dos días después del día anterior a mañana es sábado. ¿Qué día es hoy?", 'respuesta': "viernes"}]

pistas4 = ["Es una alimento", "Lo usan los vampiros", "Se puede mirar a través de este", "Es un s...", "Dia antes del fin de semana"]

def nivel4():
    puntaje = 0
    global dinero
    for elemento in lista_nivel2:
        print()
        pregunta = elemento['pregunta']
        respuesta_correcta = elemento['respuesta']
        print("Pregunta")
        print(pregunta)
        respuesta = input("Respuesta: ").lower
        
        if respuesta == respuesta_correcta:
            print("Respuesta correcta")
            dinero+=250
            puntaje += 1
        else:
            print("Respuesta incorrecta")
    
    return puntaje

lista_nivel5 = [{'pregunta': "Hay un pato entre dos patos, un pato detrás de un pato y un pato delante de otro pato. ¿De cuántos patos estamos hablando?", 'respuesta': "3"},
          {'pregunta': "¿Cuál es el número en la secuencia 3, 13, 30, 31, 32 ...?", 'respuesta': "33"},
          {'pregunta': "Una casa tiene cuatro esquinas, cada esquina tiene un gato, cada gato ve a tres gatos. ¿Cuántos gatos hay en la casa?", 'respuesta': "4"},
          {'pregunta': "En el taxi en el que entré había 8 pasajeros. Poco después, 3 personas bajaron y dos entraron. ¿Cuántas personas hay en el taxi ahora?", 'respuesta': "9"},
          {'pregunta': "Un hombre sin techo recoge colillas de cigarrillos de la calle. Puede hacer un cigarro con cinco colillas. Hoy está de suerte, ha encontrado 25 colillas. ¿Cuántos cigarrillos podrá hacer", 'respuesta': "6"}]

pistas5 = ["Es un número impar", "Empieza con la letra t..", "Los lados de un rectángulo son...", "Los lados de un triángulo son...", "Dia antes del fin de semana"]

def nivel5():
    puntaje = 0
    global dinero
    for elemento in lista_nivel2:
        print()
        pregunta = elemento['pregunta']
        respuesta_correcta = elemento['respuesta']
        print("Pregunta")
        print(pregunta)
        respuesta = input("Respuesta: ").lower
        
        if respuesta == respuesta_correcta:
            print("Respuesta correcta")
            dinero+=250
            puntaje += 1
        else:
            print("Respuesta incorrecta")
    
    return puntaje
