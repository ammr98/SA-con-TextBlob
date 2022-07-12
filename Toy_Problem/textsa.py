# INSTALAR LO SIGUIENTE
# pip install textblob
# python -m textblob.download_corpora

from textblob import TextBlob

ori_count = 0
 
with open("original.txt","r") as f:
  for line in f.read().split('\n'):
    analysis = TextBlob(line)
    #print(line)

    try:
      eng=analysis.translate(from_lang = "es", to='en')
      print("Texto: ")
      print(eng,"\n")
      print("Polaridad: ")
      print(eng.sentiment.polarity,"\n")
      print("Subjetividad: ")
      print(eng.sentiment.subjectivity,"\n")
      ori_count +=1
    except:
    #Mostramos este mensaje en caso de que se presente algún problema
      print ("El elemento no está presente")

print("----------------------------------------------------")
cor_count = 0
 
with open("correct.txt","r") as f:
  for line in f.read().split('\n'):
    analysis = TextBlob(line)
    
    try:
      eng=analysis.translate( from_lang= "es",to='en')
      print(eng,"\n")
      print("Polaridad: ")
      print(eng.sentiment.polarity,"\n")
      print("Subjetividad: ")
      print(eng.sentiment.subjectivity,"\n")
      cor_count +=1
    except:
      print('el elemento no esta presente')
 
#print("Precisión positiva = {}% via {} ejemplos".format(pos_correct/pos_count*100.0, pos_count))
#print("Precisión negativa = {}% via {} ejemplos".format(neg_correct/neg_count*100.0, neg_count))
