# projet_tas_de_sable-
#########################################
# groupe TD3
# Mathis DESPRES
# Maura VASILE 
# Inès RADELET
# https://github.com/uvsq22102805/projet_tas_de_sable-
#########################################

Fonctionnement des fonctions:

fonction simulation, contient toutes les fonctions nécessaires au mode simulation dont la fonction click_boules qui sert à définir la position des boules dans le boulier en fonction de quand on clique dessus. Fonction réinitialiser permet de réinitialiser la position des boules en mode simulation. 
fonction hover_style sert juste à colorer les boules en mode simulation lorsque l'on passe le curseur dessus.
la fonction opération contient les fonctions pour le mode opération dont les fonctions addition, soustraction, multiplication et division
les fonctions analyse_int et adapt servent pour la fonction opération ils se chargent de positionner les boules correctement en fonction du calcul effectué
fonction error_handler permet de mettre une limite au nombre de colonnes en mode simulation, il affiche une erreur si le nombre est ≤ à 0 ou si il est > à 20.

Utilisation du projet:

lorsque le programme s'allume et que la fênetre apparaît, appuyer sur le mode que l'on veut, donc simulation ou opération, en mode simulation on choisis le nombre de colonnes (valeur à entrer dans la console) que l'on veut puis on peux actionner les boules comme on le souhaite. Pour le mode opératoire il faut juste rentrer les 2 valeurs que l'ont veut calculer puis cliquer sur le bouton qui défini l'opération souhaité

bout de programme pris depuis un site :

num = 13579
x = [int(a) for a in str(num)]
print(x)

https://www.delftstack.com/fr/howto/python/split-integer-into-digits-python/#:~:text=%2C%207%2C%209%5D-,Utilisez%20les%20fonctions%20map()%20et%20str.,chaque%20élément%20d%27un%20itérable
