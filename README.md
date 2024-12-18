# Task Scheduling Simulation

## 📋 Description

Ce projet est une application web développée avec **Django** , **Flask** et **StreamLit**. Qui permet de simuler plusieurs algorithmes d'ordonnancement de tâches (scheduling algorithms). L'utilisateur peut entrer des tâches avec leurs propriétés (ID, temps d'arrivée, temps d'exécution, deadline, période), choisir un algorithme et visualiser les résultats, y compris un **diagramme de Gantt**.

---

## 🚀 Fonctionnalités

- **Ajout et Suppression de Tâches Dynamiquement** : 
  - L'utilisateur peut ajouter plusieurs tâches via le formulaire.
  - Chaque tâche peut être supprimée individuellement avec un bouton "Remove".

- **Algorithmes Disponibles** :
  - **FCFS (First-Come, First-Served)**
  - **SJF (Shortest Job First)**
  - **RM (Rate Monotonic)**
  - **DM (Deadline Monotonic)**
  - **LLF (Least Laxity First)**
  - **EDF (Earliest Deadline First)**

- **Visualisation des Résultats** :
  - Affichage des étapes de l'algorithme sélectionné.
  - Génération et affichage d'un **diagramme de Gantt** pour visualiser l'ordonnancement.
 

## 🛠️ Prérequis

1. **Python 3.8+**
2. **Django 5.1.4**
3. **Matplotlib** pour la génération des diagrammes de Gantt.
4. **Flask (Optional)** 
5. **StreamLit (Optional)** 


## 🔧 Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/nom_utilisateur/task-scheduling-simulation.git
   cd task-scheduling-simulation


