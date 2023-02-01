#!/usr/bin/env python
# coding=utf-8
#Ajouter le support pour les jeux de caractères non-ASCII
#importation de(s) librairie(s)
import sys
gender_prize_count= {}
gender_prize_age = {}

# Récuperation du flux d'entrée depuis STDIN
for line in sys.stdin:
# Suppression des espaces au début et à la fin des lignes
	line = line.strip()
# Analyse de l'entrée reçue depuis mapper.py et décomposition des lignes en colonnes
	index, gender, age_at_prize, count = line.split('\t', 4)
# Conversion du type des colonnes pertinentes, actuellement en chaines de caractères, en entiers
	try:
		count = int(count)
		age_at_prize = int(age_at_prize)
# Si erreur au niveau du type des valeurs, continuer le traitement sans interruption
	except ValueError:
        	continue

# Compter le nombre d'occcurence du genre et la somme des ages au décernement du prix Nobel
    	
	try:
		gender_prize_count[gender]= gender_prize_count[gender]+count
		gender_prize_age[gender] = gender_prize_age[gender]+age_at_prize
    	except:
    		gender_prize_count[gender]= count
		gender_prize_age[gender] = age_at_prize

for count,age in zip(gender_prize_count.keys(),gender_prize_age.keys()):
	msg = 'homme' if count == "male" else "femme"
	print '\n- %s fois un prix Nobel a été attribué à des %ss ' % (gender_prize_count[count],msg)
	print '- Σ des ages des %ss qui ont remporté un Nobel: %s' % (msg,gender_prize_age[age])
	print '- Moyenne des ages des %ss à qui on a attribué un prix Nobel: %s' % (msg,"%.2f"%(float(gender_prize_age[age])/float(gender_prize_count[count])))

