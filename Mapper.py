#!/usr/bin/env python
# coding=utf-8
#Ajouter le support pour les jeux de caractères non-ASCII

#importation de(s) librairie(s)
import sys

# Lecture du fichier csv ligne par ligne de la sortie de la commande cat nobelFinal.csv.
for index,rows in enumerate(sys.stdin):

#Ignore la 1ère ligne qui correspond à l'entête des colonnes, sinon erreur s'en suit.
	if index > 0:

# Suppression des espaces au début et à la fin de chaque ligne
 		columns = rows.strip().split(',')

# Transformation de chaque ligne en colonnes, pour ne garder ne que les colonnes gender et age lors de 
 		try:
 	 		gender = columns[4]
			age_at_prize=columns[13]
   	 		print ('#%s:\t%s\t%s\t%s' % (index-1,gender, age_at_prize,1))
    		except ValueError:
    	 		pass
