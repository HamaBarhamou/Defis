Très excité par toutes les possibilités offertes par son ordinateur, Gérard a téléchargé de nombreux logiciels sur internet... ce qui devait arriver est arrivé et son ordinateur a été infecté par un virus. Evidemment, c'est à vous que Gérard fait appel pour réparer les dégâts. Vous vous empressez d'installer un antivirus et de nettoyer son PC. Malheureusement des données ont été corrompues et il va falloir les reconstruire.
Le virus a modifié certains caractères dans les fichiers de la base de données de produits de Gérard : un peu partout, des caractères ont été remplacés par des '?'. Il est facile de deviner ce qui manque quand il s'agit de noms de produits, mais c'est beaucoup plus difficile lorsque ce sont les codes des produits qui ont été corrompus.

Vous avez établi la liste des produits dont le code a été partiellement effacé, il ne reste plus qu'à les compléter. Pour cela, il n'y a pas d'autre solution que de rechercher ces objets dans le stock pour retrouver leur code. Heureusement, vous n'avez perdu aucune information concernant la manière dont sont rangés les produits d'un code donné et n'aurez pas à vider toute la réserve.

Vous devez écrire un programme qui recherche tous les codes de produits pouvant correspondre au code partiel qui vous est fourni. Pour augmenter vos chances de retrouver très rapidement le bon produit dans la réserve, vous devez énumérer les codes possibles dans l'ordre du nombre d'étapes nécessaires pour les retrouver. Les codes d'objets nécessitant un même nombre d'étapes peuvent être donnés dans n'importe quel ordre.

Limites de temps et de mémoire (Python)
Temps : 2 s sur une machine à 1 GHz.
Mémoire : 4 000 ko.
Contraintes
1 <= N <= 20000, où N est le nombre de codes d'identification différents utilisés pour les produits et récipients de la réserve.
1 <= K <= N, où K est le code-barre d'un produit, ou d'un récipient de la réserve.
Entrée
La première ligne de l'entrée contient un entier N : le nombre de produits et récipients de la réserve, identifiés par un code.
La deuxième ligne contient N entiers séparés par des espaces, qui décrivent les positions des produits ou récipients, dans l'ordre de leur code d'identification. Le Kème entier de la ligne représente le code du récipient dans lequel se trouve l'objet de code K. La valeur 0 indique que l'objet se trouve directement dans la réserve.

La troisième ligne contient une chaîne composée de chiffres et de caractères '?' et représentant le code incomplet. Il s'agit du "masque".

Sortie
Vous devez afficher une ligne sur la sortie, contenant des nombres séparés par des espaces : l'ensemble des codes qui peuvent correspondre au code incomplet fourni, triés par nombre d'étapes nécessaires pour retrouver les produits correspondants.
Exemples
Exemple 1
entrée :

8
3 3 7 3 6 7 0 0
?
sortie :

7 8 6 3 1 2 4 5
Exemple 2
entrée :

12
0 0 1 1 2 2 2 3 3 3 4 4
1?
sortie :

12 11 10
Commentaires
Dans le premier exemple, tous les objets peuvent correspondre au code partiel '?'
Les objets 7 et 8 s'obtiennent en une étape.
Les objets 6 et 3 s'obtiennent en deux étapes.
Les objets 1, 2, 4 et 5 s'obtiennent en trois étapes.
Dans le deuxième exemple, seuls les objets à deux chiffres, et commençant par 1, peuvent correspondre au code partiel '1?'.

Attention : si le code partiel commence par un '?', ce '?' ne peut pas correspondre à un zéro. On représente en effet les nombres sans zéros en tête.