"""Exercice 3 — Évaluation en masse via EvaluationDataset (solution).

Objectif : passer du test unitaire à une évaluation sur plusieurs cas à la
fois, workflow typique lorsqu'on benchmark un modèle ou une version d'un
pipeline RAG.
"""

import json
from pathlib import Path

from deepeval import evaluate
from deepeval.dataset import EvaluationDataset
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase


_DATASET_PATH = Path(__file__).resolve().parent.parent / "data" / "qa_dataset.jsonl"


def test_bulk_evaluation_on_qa_dataset():
    dataset = EvaluationDataset()
    dataset.test_cases = _load_test_cases(_DATASET_PATH)

    evaluate(
        test_cases=dataset.test_cases,
        metrics=[
            AnswerRelevancyMetric(threshold=0.7),
            FaithfulnessMetric(threshold=0.7),
        ],
    )


def _load_test_cases(path: Path) -> list[LLMTestCase]:
    if not path.exists():
        raise FileNotFoundError(f"Dataset introuvable : {path}")

    with path.open(encoding="utf-8") as file:
        lines = [line for line in file if line.strip()]

    return [
        LLMTestCase(
            input=row["input"],
            actual_output=row["actual_output"],
            retrieval_context=row.get("retrieval_context"),
        )
        for row in (json.loads(line) for line in lines)
    ]
