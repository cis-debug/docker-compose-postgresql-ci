# 🚀 Docker Compose + PostgreSQL + CI/CD






\

## 📌 Description

Projet DevOps combinant **Docker Compose**, **PostgreSQL**, **tests automatisés avec pytest** et **GitHub Actions**.

L'application contient une API Flask et une base PostgreSQL exécutées dans des conteneurs Docker.

À chaque `push` ou `pull request` sur `main`, GitHub Actions lance automatiquement les tests Python puis construit les images Docker si les tests réussissent.

---

## 🎯 Objectifs

Cette mission permet de pratiquer :

* Docker Compose
* Python / Flask
* PostgreSQL
* tests automatisés avec pytest
* GitHub Actions
* intégration continue (CI)
* dépendances entre jobs
* Docker Build automatisé

---

## 🏗️ Architecture

```text
                    👩‍💻 Developer
                         │
                         │ git push
                         ▼
                ┌─────────────────┐
                │ GitHub Actions  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Python Tests   │
                │     pytest      │
                └────────┬────────┘
                         │
                    Tests OK
                         │
                         ▼
                ┌─────────────────┐
                │   Docker Build  │
                └─────────────────┘


        Application locale
                 │
                 ▼
        ┌─────────────────┐
        │   Flask API     │
        │      :5000      │
        └────────┬────────┘
                 │
                 │ Docker Network
                 ▼
        ┌─────────────────┐
        │   PostgreSQL    │
        │      :5432      │
        └─────────────────┘
```

---

## 📁 Structure du projet

```text
docker-compose-postgresql-ci/
│
├── api/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

## 🌐 API Flask

L'API expose trois endpoints :

| Méthode | Endpoint  | Fonction                            |
| ------- | --------- | ----------------------------------- |
| `GET`   | `/`       | Vérifier que l'API fonctionne       |
| `GET`   | `/health` | Vérifier l'état de l'API            |
| `GET`   | `/users`  | Retourner la liste des utilisateurs |

### Tester l'API

```bash
curl http://localhost:5000/
```

```bash
curl http://localhost:5000/health
```

```bash
curl http://localhost:5000/users
```

Exemple de réponse :

```json
{
  "message": "Docker Compose PostgreSQL CI",
  "status": "running"
}
```

---

## 🐳 Docker Compose

Le fichier `docker-compose.yml` orchestre deux services :

```text
api
db
```

### API

* Python 3.12
* Flask
* port `5000`

### PostgreSQL

* PostgreSQL `16-alpine`
* base `devops`
* utilisateur `devops`
* port interne `5432`

Les deux services communiquent via le réseau Docker créé automatiquement par Compose.

---

## ❤️ Healthcheck PostgreSQL

PostgreSQL utilise `pg_isready` pour vérifier que la base est disponible.

```yaml
healthcheck:
  test:
    [
      "CMD-SHELL",
      "pg_isready -U devops -d devops"
    ]
```

Le service API attend que PostgreSQL soit prêt :

```yaml
depends_on:
  db:
    condition: service_healthy
```

Cela permet de gérer correctement le démarrage des services.

---

## 🧪 Tests automatisés

Les tests sont réalisés avec **pytest**.

Le fichier :

```text
tests/test_app.py
```

contient des tests pour :

* `/`
* `/health`
* `/users`

Lancer les tests localement :

```bash
pytest
```

Résultat attendu :

```text
3 passed
```

---

## ⚙️ GitHub Actions

Le workflow se trouve dans :

```text
.github/workflows/ci.yml
```

Il se déclenche lors :

* d'un `push` sur `main`
* d'une `pull request` vers `main`

### Pipeline

```text
Git Push / Pull Request
          │
          ▼
     Checkout code
          │
          ▼
     Setup Python 3.12
          │
          ▼
   Install dependencies
          │
          ▼
       Run pytest
          │
       ┌──┴──┐
       │     │
      ❌     ✅
       │     │
      STOP   ▼
         Docker Build
```

Le job Docker utilise :

```yaml
needs: test
```

Le build Docker ne démarre donc que si les tests Python réussissent.

---

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/cis-debug/docker-compose-postgresql-ci.git
cd docker-compose-postgresql-ci
```

### 2. Installer les dépendances

```bash
pip install -r api/requirements.txt
```

### 3. Lancer les tests

```bash
pytest
```

### 4. Construire les conteneurs

```bash
docker compose build
```

### 5. Démarrer l'application

```bash
docker compose up -d
```

### 6. Vérifier les services

```bash
docker compose ps
```

---

## 🔧 Commandes utiles

### Voir les conteneurs

```bash
docker ps
```

### Voir les logs de l'API

```bash
docker compose logs api
```

### Voir les logs PostgreSQL

```bash
docker compose logs db
```

### Arrêter les services

```bash
docker compose down
```

### Reconstruire les images

```bash
docker compose up -d --build
```

---

## 🛠️ Technologies utilisées

* 🐍 Python 3.12
* 🌐 Flask
* 🧪 Pytest
* 🐳 Docker
* 🧩 Docker Compose
* 🗄️ PostgreSQL 16
* ⚙️ GitHub Actions
* 🐧 Linux / WSL
* 🔧 Git / GitHub

---

## 🔐 Bonnes pratiques

Pour un environnement de production, il serait recommandé de :

* utiliser un fichier `.env` non versionné
* stocker les secrets dans GitHub Secrets
* utiliser des mots de passe robustes
* ajouter davantage de tests
* ajouter une authentification API
* scanner les images Docker pour détecter les vulnérabilités

---

## 🚀 Améliorations possibles

Ce projet peut évoluer vers :

* publication automatique de l'image sur Docker Hub
* tests d'intégration avec PostgreSQL
* linting Python
* analyse de sécurité avec Trivy
* reverse proxy Nginx
* monitoring avec Prometheus et Grafana
* déploiement automatique dans le cloud

---

## 👩‍💻 Auteur

**Cisse Ndeye**

GitHub :
https://github.com/cis-debug
