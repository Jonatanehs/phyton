from juego import nivel1, nivel2,nivel3,nivel4,nivel5
print("!Bienvenidos a esta nueva aventura¡")
print("\nEn este juego, te enfrentaras a diferentes preguntas en las que pondrás a prueba tu inteligencia. "\
    "El juego consta de 5 niveles, los cuales tienen diferentes preguntas y acertijos matemáticos y de lógica.")
print("\nReglas:")
print("Tendras la oportunidad de obtener 2 pistas en cada nivel", "\nPor cada pregunta con respuesta correcta"
        " recibiras 250 de oro, ", "y 10 puntos, si contestas mal perderas 5 puntos" 
        "\nPara poder superar un nivel deberas obtener por lo menos 3 respuestas correctas"
        "\nSi no obtienes las respuestas correctas suficientes podrás usar el oro para reiniciar el nivel" 
        "\nSi te quedas sin pistas y no has respondido todas las preguntas para pasar de nivel podrás usar el oro para reiniciar el nivel"
        "\nPero si reinicias el nivel tus puntos iniciaran en 0"     
        "\nSi no respondes correctamente a las preguntas y no tienes el oro suficiente el juego se terminara")
print("\n¡Comencemos!")

puntaje =nivel1()
if puntaje>30:
    print("¡Felicidades, puedes pasar al siguiente nivel!")
    puntaje =nivel2()
    if puntaje > 30:
        print("¡Felicidades, puedes pasar al siguiente nivel!")
        puntaje =nivel3()
        if puntaje >30:
            print("¡Felicidades, puedes pasar al siguiente nivel!")
            puntaje =nivel4()
            if puntaje > 30:
                print("¡Felicidades, puedes pasar al siguiente nivel!")
                puntaje =nivel5()
                
