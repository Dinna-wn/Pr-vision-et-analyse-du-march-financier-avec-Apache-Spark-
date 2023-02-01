# Pr-vision-et-analyse-du-march-financier-avec-Apache-Spark-


Note : le fichier csv ajouté dans le dossier c'est le jeu de données apres traitement, le lien de notre source de données originale qu'avait pris de Kaggle.

https://www.kaggle.com/datasets/bahramjannesarr/nobel-prize-from-1901-till-2020


Traitement MapReduce:

We introduced 2 dictionaries 'gender_prize_count' and 'gender_prize_age' to combine the number of occurrences that a Nobel has been awarded to a man or a woman as well as the number of occurrences of the age of the Nobel laureates by gender, in other words the sum of the ages of the Nobel laureates by gender


Finally by reading the values of the keys ('Female', 'Male') of the dictionary 'gender_prize_count' We will display the number of Nobel laureate by sex. By reading the values of the keys ('Female', 'Male') of the dictionary 'gender_prize_age' We will display the sum of the ages of the Nobel laureate by sex when he/she obtained a Nobel. Dividing the total of the ages by the number of times a laureate has won a Nobel, gives us the average of the ages of the Nobel laureates 

Traitement SparkSQL:

Our second processing will focus on the relationship between universities and Nobel Prizes, we have grouped the names of the different universities according to the year in which the winner won the Nobel Prize with which university as well as in which category did he win this prize.
