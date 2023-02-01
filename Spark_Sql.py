
#Nous ajoutons le format de transformation unicode pour les encodages
#-*-coding:utf-8-*-


#importation des librairies

from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as f


#generer le SparkContext avec lurl du cluster auquel il se connecte
sc= SparkContext("local","first app")
#generer le SQLContext avec le SparkContext
sqlContext= SQLContext(sc)



#creation dun schema en specifiant le nom, le Datatype et si la valeur peut etre nulle ou pas
nobel_final_schema = StructType([
StructField("firstname", StringType(), True),
StructField("surname", StringType(), True),
StructField("born_country_code", StringType(), True),
StructField("died_country_code", StringType(), True),
StructField("gender", StringType(), True),
StructField("year", IntegerType(), True),
StructField("category", StringType(), True),
StructField("share", IntegerType(), True),
StructField("name_of_university", StringType(), True),
StructField("city_of_university", StringType(), True),
StructField("country_of_university", StringType(), True),
StructField("born_month",StringType(), True),
StructField("age", IntegerType(), True),
StructField("age_get_prize", IntegerType(), True)])



# Importation de fichier csv et creation de RDD
fichier= sc.textFile("/user/cloudera/finalNobel.csv")
rdd = fichier.map(lambda x:x.split(",")).map(lambda x:(x[0], x[1],x[2],x[3],x[4],
           int(x[5]),x[6],int(x[7]),x[8],x[9],x[10],x[11],int(x[12]),int(x[13])))



#Creation dun dataframe a partir dun RDD en specifiant le schema
df1=sqlContext.createDataFrame(rdd,nobel_final_schema)


#Nous avons selectionne le nom de l'universite, l'annee et la categorie
df_select=df1.select("name_of_university","year","category")

#Nous avons utilise groupBy pour le regroupement des resultats en fonction du nom de 
#luniversite lannee et la categorie et avec la methode count nous avons compter 
#combien de prix luniversite a gagne dans telle annee et dans quel domaine 
df_grouped=df_select.groupBy("name_of_university","year","category").count()

#Nous souhaitons ordonner le resultat en fonction du nom de luniversite 
df_ordered=df_grouped.orderBy(col("name_of_university"))

#Afficher les 100 premieres lignes de resultat
df_ordered.show(100)


######### Verification ##########
#filtrer les gagnants du prix dans l'institut Basel et pour l'annee 1984
print("les 2 gagnants du prix dans l'institut Basel et pour l'annee 1984")
dd=df1.filter(df1.name_of_university == 'Basel Institute for Immunology')
dd.filter(dd.year == '1984').show()

#filtrer les gagnants du prix en medecine pendant l'annee 1984
print("les 3 gagnants du prix en medecine pendant l'annee 1984")
dd1=df1.filter(df1.category == 'medicine')
dd1.filter(dd1.year == '1984').show()



