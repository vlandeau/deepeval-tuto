# Hands-on DeepEval — 15-20 minutes

Un atelier pratique pour découvrir [DeepEval](https://deepeval.com), un framework
open-source d'évaluation de LLMs inspiré de `pytest`. Vous allez écrire vos
premiers tests d'évaluation, détecter une hallucination dans un pipeline RAG,
puis lancer une évaluation en masse sur un petit dataset.

L'ensemble tourne **en local avec Ollama** — aucune clé API nécessaire.

---

## Prérequis (à installer AVANT la session)

1. **[uv](https://docs.astral.sh/uv/)** installé :
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   (uv gère Python et les dépendances — pas besoin d'installer Python
   séparément).
2. **Ollama** installé — https://ollama.com/download
3. **Le modèle `gemma3:4b`** téléchargé :
   ```bash
   ollama pull gemma3:4b
   ```
   (~3,3 Go ; à faire à l'avance, pas le jour J).
4. Ollama doit tourner en arrière-plan. Vérifier avec :
   ```bash
   ollama list
   ```

> **Note** : les scores peuvent varier d'une exécution à l'autre — c'est
> normal avec un petit juge local. En production, on préfère un modèle
> plus puissant (GPT-4.1, Claude Opus 4, etc.).

---

## Setup (3 minutes)

```bash
# 1. Se placer dans le repo
cd deepeval-tuto

# 2. Installer les dépendances (uv crée le .venv automatiquement)
uv sync

# 3. Créer le fichier .env.local qui pointe DeepEval vers Ollama
cat > .env.local <<'EOF'
USE_LOCAL_MODEL=1
LOCAL_MODEL_NAME=gemma3:4b
LOCAL_MODEL_BASE_URL=http://localhost:11434/v1/
LOCAL_MODEL_API_KEY=ollama
EOF
```

Pour vérifier que tout est prêt :

```bash
uv run deepeval test run solutions/test_1_basics.py
```

Le test doit passer en ~10 secondes (scores possiblement variables selon
le modèle local — c'est attendu avec un petit juge).

---

## Structure du projet

```
deepeval-tuto/
├── data/
│   └── qa_dataset.jsonl       # 5 cas pour l'exercice 3
├── tests/
│   ├── test_1_basics.py       # Exercice 1 — à compléter
│   ├── test_2_rag.py          # Exercice 2 — à compléter
│   └── test_3_dataset.py      # Exercice 3 — à compléter
└── solutions/                  # Corrigés — à consulter en cas de blocage
```

---

## Exercice 1 — Premiers tests (5 min)

**Fichier** : `tests/test_1_basics.py`

Vous allez évaluer la réponse d'un chatbot e-commerce avec deux métriques :

- `AnswerRelevancyMetric` — métrique intégrée, mesure si la réponse est
  pertinente par rapport à la question.
- `GEval` — métrique 100% custom, pilotée par un critère en langage naturel
  (ici : évaluer la politesse de la réponse).

**Objectif** : compléter les 4 `TODO` du fichier et lancer :

```bash
uv run deepeval test run tests/test_1_basics.py
```

**Ce que vous apprenez** : la différence entre une métrique paramétrée et une
métrique GEval où *vous* définissez le critère d'évaluation.

---

## Exercice 2 — Évaluation d'un pipeline RAG (5 min)

**Fichier** : `tests/test_2_rag.py`

Vous simulez un pipeline RAG : un contexte (`retrieval_context`) a été récupéré
et un LLM a généré une réponse. Vous devez écrire :

- un test avec une réponse **fidèle** au contexte ;
- un test avec une réponse qui **hallucine** un détail (par ex. « free return
  shipping via DHL Express »).

**Objectif** : compléter les `TODO` puis lancer :

```bash
uv run deepeval test run tests/test_2_rag.py
```

> ⚠ Le second test **doit échouer**. C'est le comportement attendu — c'est
> précisément ce qui démontre que `FaithfulnessMetric` détecte l'hallucination.

**Ce que vous apprenez** : comment plugger DeepEval sur la sortie d'un RAG et
détecter automatiquement qu'un LLM invente des faits.

---

## Exercice 3 — Évaluation en masse (5 min)

**Fichier** : `tests/test_3_dataset.py`

Vous allez charger `data/qa_dataset.jsonl` (5 cas) dans un `EvaluationDataset`
et lancer une évaluation en bulk avec `evaluate()`.

**Objectif** : compléter les 3 `TODO` et lancer :

```bash
uv run deepeval test run tests/test_3_dataset.py
```

DeepEval va produire un rapport consolidé sur les 5 cas. Un des cas du
dataset contient volontairement une hallucination — cherchez-la dans le
rapport !

**Ce que vous apprenez** : le passage du test unitaire à l'**évaluation en
masse**, workflow typique quand on benchmark un modèle ou qu'on veut suivre
l'évolution de la qualité au fil des versions.

---

## En cas de blocage

Consultez le dossier `solutions/` qui contient les trois exercices corrigés.
N'hésitez pas à copier/coller — l'important est de comprendre le workflow,
pas d'avoir tout écrit vous-même.

---

## Pour aller plus loin

- **Confident AI** : la plateforme cloud des créateurs de DeepEval, pour
  logger les résultats, versionner les datasets et suivre les régressions.
- **Synthetic data generation** : DeepEval peut générer automatiquement des
  cas de test à partir de vos documents sources.
- **LLM juge custom** : au lieu d'Ollama, brancher un modèle Anthropic, OpenAI,
  ou un modèle fine-tuné comme juge.
- **Red teaming** : DeepEval inclut des métriques de sécurité (Bias, Toxicity,
  PII leakage...).

### Ressources

- Docs officielles : https://deepeval.com/docs/getting-started
- Intégration Ollama : https://deepeval.com/integrations/models/ollama
- Faithfulness : https://deepeval.com/docs/metrics-faithfulness
- Answer Relevancy : https://deepeval.com/docs/metrics-answer-relevancy
