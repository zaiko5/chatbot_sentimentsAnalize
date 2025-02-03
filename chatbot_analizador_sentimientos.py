#Desarrollar un chatbot que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y nos responda
#cual es el sentimiento.

from logica_analisis_sentimientos import analizar_sentimiento as analizador #Importamos la funcion para analizar sentimientos.
 
#Funcion para generar una respuesta segun el sentimiento que se identifique.            
def generar_respuesta(sentimiento):
    if sentimiento == "Alegria":
        return "¡Qué bueno! Me alegra saber que estás experimentando alegría. ¡Disfrútalo al máximo!"
    elif sentimiento == "Felicidad":
        return "¡Eso suena genial! Me alegra que estés sintiéndote feliz. Sigue disfrutando de esos buenos momentos."
    elif sentimiento == "Aprobacion":
        return "Me alegra que estés de acuerdo. Es bueno ver una perspectiva positiva como la tuya."
    elif sentimiento == "Sorpresa positiva":
        return "¡Qué sorpresa tan agradable! Me encanta que algo inesperado te haya hecho sentir bien."
    elif sentimiento == "Neutral positivo":
        return "Es bueno escuchar algo positivo, aunque sea más neutral. Espero que todo siga yendo bien."
    elif sentimiento == "Tristeza":
        return "Lamento saber que te sientes triste. Si necesitas hablar, aquí estoy para escucharte."
    elif sentimiento == "Desesperacion":
        return "Siento que te sientas así. Quiero que sepas que no estás solo, y siempre hay formas de encontrar esperanza."
    elif sentimiento == "Desaprobacion":
        return "Entiendo tu punto de vista. Es bueno expresar opiniones para buscar soluciones o mejoras."
    elif sentimiento == "Neutral negativo":
        return "Entiendo tu perspectiva. A veces no todo es perfecto, pero espero que las cosas mejoren."
    elif sentimiento == "Neutral":
        return "Gracias por compartir tu pensamiento. Parece que es un comentario objetivo y equilibrado."
    
#Funcion que maneja al chatbot.
def chatbot():
    sentimiento = analizador() #Se identifica el sentimiento con la funcion analizadora. 
    respuesta = generar_respuesta(sentimiento) #Segun el sentimiento, generamos la respuesta.
    print(f"Sentimiento: {sentimiento}\n{respuesta}") #Imprimimos la respuesta.
    
print("Hola soy el chatbot analizador de sentimientos!")
while True:
    chatbot()