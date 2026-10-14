# Outil de diagnostic réseau pour le support informatique

Projet personnel développé en Python pour pratiquer le diagnostic réseau, la gestion des erreurs et la génération de rapports techniques, dans le contexte du support informatique.

## Présentation du projet

Cet outil permet d'effectuer des vérifications réseau de base afin d'aider à identifier des problèmes de connectivité. Il vérifie la résolution DNS d'un nom d'hôte et tente d'établir une connexion TCP vers un port spécifié.

Les résultats sont affichés dans le terminal et enregistrés dans des rapports JSON horodatés contenant les observations et des recommandations pour poursuivre le diagnostic.

**Remarque :** il s'agit d'un projet personnel à vocation pédagogique, inspiré des méthodes de diagnostic utilisées en support informatique. Ce projet n'est pas un produit officiel de Hewlett Packard Enterprise (HPE) et n'est pas affilié à l'entreprise.

## Fonctionnalités

- **Vérification DNS :** résolution d'un nom d'hôte en adresse IPv4.
- **Test de connectivité TCP :** vérification de la possibilité d'établir une connexion vers un hôte et un port spécifiques.
- **Gestion des erreurs :** prise en charge des erreurs courantes de résolution DNS et de connexion.
- **Mesure du temps de réponse :** mesure de la durée des opérations de diagnostic réussies.
- **Recommandations de dépannage :** suggestions d'investigation adaptées aux résultats obtenus.
- **Génération de rapports JSON :** sauvegarde des résultats et des recommandations dans des fichiers horodatés.
- **Validation des entrées :** vérification du nom d'hôte et de la plage de ports autorisée.

## Technologies utilisées

- Python 3.11 ou version ultérieure
- Bibliothèques standard Python : `socket`, `time`, `json`, `datetime` et `pathlib`
- Git et GitHub pour la gestion de versions

Aucune bibliothèque Python externe n'est nécessaire pour les fonctionnalités de diagnostic réseau.

## Structure du projet

```text
hpe-it-diagnostic-toolkit/
├── main.py
├── network_diagnostics.py
├── README.md
├── .gitignore
└── reports/
    └── Rapports JSON générés automatiquement
```

- `main.py` : gestion des entrées utilisateur, exécution des tests, affichage des résultats, recommandations et génération des rapports.
- `network_diagnostics.py` : implémentation des fonctions de résolution DNS et de vérification de la connectivité TCP.
- `reports/` : dossier de destination des rapports générés lors de l'exécution.

## Installation et utilisation

### Prérequis

- Python 3.11 ou version ultérieure
- Une connexion Internet pour tester des hôtes externes

### Lancer le programme

1. Cloner le dépôt GitHub :

   ```bash
   git clone https://github.com/VOTRE_NOM_UTILISATEUR/hpe-it-diagnostic-toolkit.git
   ```

2. Accéder au répertoire du projet :

   ```bash
   cd hpe-it-diagnostic-toolkit
   ```

3. Exécuter le programme :

   ```bash
   python main.py
   ```

4. Saisir le nom d'hôte et le port TCP à tester lorsque le programme le demande.

Remplacer `VOTRE_NOM_UTILISATEUR` par le nom d'utilisateur GitHub correspondant au dépôt.

## Exemple d'utilisation

Pour effectuer un test de connectivité de base, saisir :

```text
Nom d'hôte : example.com
Port TCP : 443
```

Le programme affiche séparément le résultat de la résolution DNS et celui du test de connectivité TCP.

Une connexion TCP réussie signifie qu'une connexion a pu être établie vers le port spécifié. Cela ne garantit pas que le site web ou l'application fonctionne correctement.

## Rapports de diagnostic

À la fin des vérifications, le programme génère un rapport JSON horodaté dans le dossier `reports/`.

Chaque résultat peut contenir les informations suivantes :

- Type de vérification
- Nom d'hôte ou adresse de destination et port
- Statut du test (`PASS` ou `FAIL`)
- Détails du résultat
- Temps de réponse lorsqu'il est disponible
- Recommandations pour poursuivre le dépannage

Les rapports JSON générés sont exclus du suivi Git grâce au fichier `.gitignore`. Le dépôt reste ainsi centré sur le code source et la documentation plutôt que sur les résultats locaux des tests.

## Limites connues

- La résolution DNS repose sur les mécanismes du système d'exploitation et peut utiliser des résultats mis en cache.
- Le test TCP vérifie un seul port à la fois.
- Un échec de connexion ne permet pas, à lui seul, d'identifier la cause racine du problème.
- Les recommandations sont basées sur des règles simples et orientent les investigations sans garantir un diagnostic définitif.
- L'outil ne vérifie pas encore les réponses HTTP, ne réalise pas de supervision complète des serveurs et n'effectue pas d'analyse automatique de la cause racine.

## Améliorations envisagées

- Ajouter la vérification de plusieurs ports configurables.
- Améliorer la gestion des délais d'attente et la description des échecs.
- Développer des tests unitaires automatisés pour les fonctions de diagnostic et de génération de rapports.
- Ajouter un module distinct de surveillance des ressources système sous Linux.
- Améliorer la synthèse des échecs et des actions de dépannage recommandées.

## Objectifs pédagogiques

Ce projet permet de mettre en pratique la programmation Python, la décomposition en fonctions, la gestion des exceptions, la manipulation de dictionnaires, les opérations sur les fichiers, le diagnostic réseau, la validation des entrées et le contrôle de versions avec Git.

Il vise à renforcer les compétences en résolution de problèmes techniques et en documentation, utiles dans les fonctions de support informatique et de support aux infrastructures.

## Auteur

**Issra Lassoued**  
Élève ingénieure en Informatique Industrielle et Automatique à l'INSAT, Tunisie.