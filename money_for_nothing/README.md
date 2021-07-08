## Money_for_nothing

On crée un object dont la fonction `main` sera appellée
On envoie a l'object l'argument numéro 1, ce dernier est "load" durant l'initialisation

On defini une premiere boucle qui va se repeter tant que nous n'avons pas parcouru le tableau
a l'interieur de celle ci nous creons une seconde boucle qui va parcourir pour avoir le prix d'achat le plus bas une premiere fois
une fois ce prix d'achat atteint nous le rentrons dans notre tableau et passons a la seconde boucle qui va definir le prix de vente
ces deux boucle fonctionne de la meme facon en verifiant que nous ne somme pas a la fin du tableau et que e nombre actuel est superieur (en cas de recherche de vente) ou inferieur (en cas de recherche d'achat) au nombre precedant, une fois la boucle arretée, si nous ne somme pas a la fin du tableau ce nombre est ajouté a notre tableau

finalement verifions que tous les actifs sont vendu avant de rendre le resultat en verifiant qu'il y a autant d'achat que de vente (%2) si ce n'est pas le cas nous retirons le dernier achat 
