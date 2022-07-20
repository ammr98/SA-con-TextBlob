# INSTALAR LO SIGUIENTE
# pip install textblob
# python -m textblob.download_corpora

from textblob import TextBlob

pos_pol = 0
neg_pol = 0
pos_count = 0
neg_count = 0
neu_count = 0
pos_subj = 0
neg_subj = 0
neu_subj = 0
count = 0

#Modificar el nombre para obtener resultados de un diferente archivo 
with open("..\DataSet\uno.txt","r") as f:
  for line in f.read().split('\n'):
    analysis = TextBlob(line)
    count +=1
    try:
      eng=analysis.translate(from_lang = "es", to='en')
      if eng.sentiment.polarity == 0.0:
        neu_subj += eng.sentiment.subjectivity
        neu_count += 1
      elif eng.sentiment.polarity > 0.0:
        pos_count += 1
        pos_pol += eng.sentiment.polarity
        pos_subj += eng.sentiment.subjectivity
      else:
        neg_count += 1
        neg_pol += eng.sentiment.polarity
        neg_subj += eng.sentiment.subjectivity

      
    except:
    #Mostramos este mensaje en caso de que se presente algún problema
      print ("El elemento no está presente")
      print(eng)
      print(count)

print("Polaridad positiva = {}% via {} comentarios".format(pos_pol/pos_count*100.0, pos_count))
print("Polaridad negativa = {}% via {} comentarios".format(neg_pol/neg_count*100.0, neg_count))
print("Polaridad media= {}% ".format((neg_pol+pos_pol)/(neg_count+pos_count+neu_count)*100.0, neg_count))
print("Comentarios neutros = {}".format(neu_count))

print("Subjetividad de cometarios positivos = {}% ".format(pos_subj/pos_count*100.0))
print("Subjetividad de cometarios negativos = {}%".format(neg_subj/neg_count*100.0))
print("Subjetividad de cometarios neutros = {}% ".format(neu_subj/neg_count*100.0))
print("Subjetividad media = {}% ".format(((neu_subj +neg_subj+ pos_subj)/(neg_count+pos_count+neu_count))*100.0))
