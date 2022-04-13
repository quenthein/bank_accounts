# bank_accounts_programm

## Objectif: 
Ecrire un programme qui implémente en POO un fonctionnement bancaire basique par l'interméfiaire du langage Python v.3.9

## Résumé
Le projet propose une interface en ligne de commande, de gestion de deux comptes bancaires :
- un compte courant (Current Account)
- un compte épargne (Savings Account)

Il sera possible à travers l'interface de :
1. Regarder le solde de ses comptes
2. Faire un retrait (withdrawal)
3. Déposer de l'argent (deposit)

Le programme permet également de :
- gérer un taux d'agios sur le compte courant, lorsque ce dernier passe en négatif.
- gérer un taux d'intéret lorsqu'un dépôt sur le compte épargne est réalisé.

### Focus sur le fonctionnement des objets créés :
Le fichier comptes.py intègre la classe mère "Bank Account" dont hérite les deux classes "Current account" & "Savings account", elles-même habritant les méthodes de calcul d'agios lors d'un retrait ou d'intérets lors d'un deposit.

### Focus sur l'interface 
Le fichier main.py habrite le fonctionnement de l'interface en ligne de commande et l'import des classes (comptes.py) permettant aux users de rentrer leur données.

---

*Réalisation dans le cadre de la POEC Cybersécurité de l'école EPSI*

*lien de l'exercice original :*
[Comptes Bancaires - Exercice](https://gitlab.com/docusland/compte-bancaires-exercice)
