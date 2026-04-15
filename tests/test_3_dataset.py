"""Exercice 3 — Évaluation en masse via EvaluationDataset.

Contexte : vous voulez benchmarker une version de votre chatbot sur un jeu
de 5 cas préparés à l'avance (data/qa_dataset.jsonl). Plutôt qu'un test
unitaire par cas, on construit un EvaluationDataset et on appelle
`evaluate()` une seule fois.

Commande pour lancer ce fichier :
    uv run deepeval test run tests/test_3_dataset.py

Bonus : le dataset contient un cas volontairement faux (cherchez-le !) qui
doit faire chuter le score de FaithfulnessMetric.
"""

import json
from pathlib import Path

from deepeval import evaluate
from deepeval.dataset import EvaluationDataset
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

_DATASET_PATH = Path(__file__).resolve().parent.parent / "data" / "qa_dataset.jsonl"


def _load_test_cases(path: Path) -> list[LLMTestCase]:
    """Helper fourni : lit le .jsonl et renvoie une liste de LLMTestCase."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset introuvable : {path}")

    with path.open(encoding="utf-8") as file:
        lines = [line for line in file if line.strip()]

    return [
        LLMTestCase(
            input=row["input"],
            actual_output=row["actual_output"],
            expected_output=row.get("expected_output"),
            retrieval_context=row.get("retrieval_context"),
        )
        for row in (json.loads(line) for line in lines)
    ]


def test_bulk_evaluation_on_qa_dataset():
    # TODO 1 : construire un EvaluationDataset() vide
    dataset = ...

    # TODO 2 : assigner dataset.test_cases = _load_test_cases(_DATASET_PATH)
    #          (en DeepEval 3.x, la liste se passe via le setter, pas dans __init__)
    ...

    # TODO 3 : appeler evaluate() avec :
    #            - test_cases=dataset.test_cases
    #            - metrics=[AnswerRelevancyMetric(threshold=0.7),
    #                       FaithfulnessMetric(threshold=0.7)]
    ...
