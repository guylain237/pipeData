# Projet ETL AIA

## Description

Ce projet consiste à développer un outil ETL (Extract-Transform-Load) modulaire en Python, capable d'extraire des données de diverses sources, de les transformer selon des règles déclaratives définies dans un fichier YAML, et de les charger vers plusieurs cibles (bases de données, fichiers JSON/XML, etc.). L'objectif est de fournir une preuve de concept et un support de méthodologie de travail en équipe.

## Fonctionnalités

* **Extraction** depuis :

  * Fichiers plats (texte, CSV)
  * Fichiers semi-structurés (JSON, XML, HTML)
  * Bases de données relationnelles
  * APIs HTTP
* **Transformation** :

  * Filtrage de données selon des critères
  * Détection et correction des valeurs manquantes ou aberrantes
  * Calcul et ajout d'attributs dérivés
  * Normalisation de formats (dates, catégories, types)
  * Combinaison de plusieurs transformations en pipeline
* **Chargement** vers :

  * Bases de données relationnelles
  * Fichiers JSON ou XML
* **Configuration** déclarative du pipeline via un fichier `config.yaml`
* **Interface** en ligne de commande pour piloter l'ETL
* **Extensible** : ajout de connecteurs ou de transformations via un catalogue de modules

## Architecture

L’architecture modulaire du projet **pipeData** suit le schéma ci-dessous, facilitant l’extensibilité, la maintenabilité et la réutilisation :

```text
[ config.yaml ]
        │
        ▼
┌───────────────────────────────────────────┐
│               CLI (main.py)              │
│ ┌───────────────────────────────────────┐ │
│ │ 1) Loader Configuration YAML         │ │
│ │   • Lecture et validation (pydantic) │ │
│ └───────────────────────────────────────┘ │
│ ┌───────────────────────────────────────┐ │
│ │ 2) Orchestrateur de pipeline ETL     │ │
│ │   • Construction du flux             │ │
│ │   • Exécution séquentielle           │ │
│ └───────────────────────────────────────┘ │
└───────────────────────────────────────────┘
           │                 │              
           ▼                 ▼              
   ┌──────────────┐   ┌───────────────┐     
   │ Extracteurs  │   │ Transformeurs │     
   │ (etl/extract)│   │ (etl/transform)│    
   └──────────────┘   └───────────────┘     
           │                 │              
           ▼                 ▼              
        ┌─────────────────────────┐         
        │         Chargeurs       │         
        │      (etl/load)         │         
        └─────────────────────────┘         
                   │                       
                   ▼                       
      Cibles de sortie (DB, JSON, XML, DataLake, CSV, logs)
```

### Points clés

* **Configuration YAML** : centralise les sources, transformations et cibles.
* **Modules `etl/`**

  * **extract/** : extraction depuis CSV, JSON, XML, HTML, API, SQL...
  * **transform/** : filtres, normalisation, enrichissement, calculs dérivés.
  * **load/**      : envoi vers SQLite, Postgres, fichiers, DataLake...
* **Dossier `extract/`** : scripts d’exemple et utilitaires pour prototypage rapide.
* **CLI** : interface unique (`main.py`) avec options `--config`, `--verbose`, `--dry-run`.
* **Validation** : `pydantic` ou `cerberus` pour le fichier `config.yaml`.
* **Logs et monitoring** : `loguru`, niveaux de log configurables, écriture dans un fichier.
* **Tests & CI** : tests `pytest` dans `tests/`, CI via GitHub Actions pour lint, tests et packaging.
* **Containerisation** : `Dockerfile` et `docker-compose.yml` pour isoler l’application et ses dépendances.

## Prérequis

* Python 3.8+
* Pip
* (Optionnel) Environnement virtuel (`venv` ou `virtualenv`)

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/guylain237/pipeData.git
   cd pipeData
   ```
2. Créer et activer un environnement virtuel :

   ```bash
   python -m venv env
   source env/bin/activate  # macOS/Linux
   env\\Scripts\\activate   # Windows
   ```
3. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Le pipeline est défini dans `config.yaml`. Exemple de structure :

```yaml
sources:
  - name: users_csv
    type: csv
    path: data/users.csv
  - name: api_posts
    type: api
    url: https://jsonplaceholder.typicode.com/posts
transformations:
  - name: filter_active
    type: filter
    params:
      column: status
      value: active
  - name: normalize_dates
    type: normalize_date
    params:
      column: created_at
      format: "%Y-%m-%d"
load:
  - name: sqlite_db
    type: sqlite
    path: database/output.db
  - name: export_json
    type: json
    path: output/results.json
```

## Utilisation

Exécuter le script principal :

```bash
python main.py --config config.yaml
```

Options disponibles :

* `--config` : chemin vers le fichier de configuration YAML (par défaut `config.yaml`)
* `--verbose` : activer le mode verbeux pour le logging

## Structure du projet

```text
pipeData/
├── env/                # Environnement virtuel Python
├── etl/                # Paquet principal ETL
│   ├── extract/        # Connecteurs d'extraction (CSV, API, SQL, ...)
│   ├── transform/      # Modules de transformations déclaratives
│   └── load/           # Connecteurs de chargement vers cibles diverses
├── extract/            # Scripts d'exemple et utilitaires d'extraction
├── config.yaml         # Définition déclarative du pipeline
├── main.py             # Point d'entrée CLI
└── requirements.txt    # Dépendances Python
```

Les dossiers et fichiers suivants peuvent être ajoutés selon l’évolution :

* `tests/`             : tests unitaires et d’intégration (pytest)
* `Dockerfile`         : configuration de build pour Docker
* `docker-compose.yml` : orchestration de services (BD, ETL)
* `data/`              : exemples ou données de test

## Contribution

1. Fork du dépôt
2. Création d'une branche de fonctionnalité (`feature/ma-fonctionnalite`)
3. Commit et push
4. Création d'une Pull Request

