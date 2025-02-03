#Modulo para la logica del analisis del sentimiento.
from textblob import TextBlob #Importamos textblob, un analizador de textos que devuelve la polaridad y la subjetividad.

#Funcion para la entrada de datos.
def entrada_user():
    while True:
        texto = input("Ingresa el texto que quieres que se analice: ").strip() #La funcion strip quita los espacios antes y despues del texto.
        if texto:
            return texto
        else:
            print("Error: El texto no puede estar vacio, intentalo nuevamente.") #Si no hay texto...

#Funcion para analizar sentimientos.            
def analizar_sentimiento(): 
    texto = entrada_user() #El texto no lo introduzco yo, se pide adentro de esta funcion.
    blob = TextBlob(texto) #Creando el objeto der la clase textblob.
    polaridad = blob.sentiment.polarity #Obteniendo tanto la polaridad y la subjetividad de mi texto.
    subjetividad = blob.sentiment.subjectivity 
    
    #Analizar la polaridad y subjetividad del texto.
    if polaridad > 0.6 and subjetividad > 0.5:
        sentimiento = "Alegria"
    elif 0.3 < polaridad <= 0.6 and subjetividad > 0.5:
        sentimiento = "Felicidad"
    elif 0.1 < polaridad <= 0.3 and subjetividad > 0.5:
        sentimiento = "Aprobacion"
    elif 0 < polaridad <= 0.1 and subjetividad > 0.5:
        sentimiento = "Sorpresa positiva"
    elif 0 < polaridad <= 0.1 and subjetividad <= 0.5:
        sentimiento = "Neutral positivo"
    elif polaridad < -0.6 and subjetividad > 0.5:
        sentimiento = "Desesperacion"
    elif -0.6 <= polaridad < -0.3 and subjetividad > 0.5:
        sentimiento = "Tristeza"
    elif -0.6 <= polaridad < -0.3 and subjetividad <= 0.5:
        sentimiento = "Desaprobacion"
    elif -0.3 < polaridad <= -0.1 and subjetividad <= 0.5:
        sentimiento = "Neutral negativo"
    else:
        sentimiento = "Neutral"
    print(f"Polaridad: {polaridad}")
    print(f"Subjetividad: {subjetividad}")
    return sentimiento #Retornamos el sentimiento para trabajar en la respuesta.
    