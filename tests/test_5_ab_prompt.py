"""Exercice 5 — A/B testing d'un prompt.

Contexte : vous avez deux versions d'un chatbot e-commerce (souvent :
deux prompts différents) et vous voulez savoir laquelle est meilleure.
C'est *le* cas d'usage le plus fréquent de DeepEval en vrai.

Ici, un chatbot factice expose deux variantes :
  - v1_terse    : réponses sèches, efficaces
  - v2_friendly : réponses chaleureuses, orientées client

On les évalue sur les mêmes questions avec une métrique GEval
« Friendliness ». La v2 doit gagner.

Commande pour lancer ce fichier :
    uv run deepeval test run tests/test_5_ab_prompt.py

Lisez le rapport : les scores de Friendliness pour v1 doivent être plus
bas que pour v2. AnswerRelevancy reste élevée pour les deux — les deux
réponses sont pertinentes, mais pas également agréables.
"""

import pytest

from deepeval import assert_test, log_hyperparameters
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

_QUESTIONS = [
    "What if these shoes don't fit?",
    "How long does shipping take?",
]

_RESPONSES = {
    "v1_terse": {
        "What if these shoes don't fit?": "Refund within 30 days. Contact support.",
        "How long does shipping take?": "3-5 days.",
    },
    "v2_friendly": {
        "What if these shoes don't fit?": (
            "No worries! We offer a full refund within 30 days — just reach "
            "out and we'll take care of it."
        ),
        "How long does shipping take?": (
            "Our standard shipping takes 3 to 5 business days. Thanks for "
            "your patience!"
        ),
    },
}


def _chatbot(question: str, version: str) -> str:
    return _RESPONSES[version][question]


def _build_metrics() -> list:
    # TODO 1 : retourner une liste de deux métriques :
    #   - AnswerRelevancyMetric(threshold=0.7)
    #   - GEval nommé "Friendliness" avec :
    #       criteria="Evaluate whether the actual output feels warm, "
    #                "empathetic and customer-friendly. Terse transactional "
    #                "answers should score lower than answers that "
    #                "acknowledge the customer."
    #       evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT]
    #       threshold=0.5
    return ...


@pytest.mark.parametrize("question", _QUESTIONS)
def test_chatbot_v1_terse(question):
    # TODO 2 : créer un LLMTestCase avec input=question et
    #          actual_output=_chatbot(question, "v1_terse"),
    #          puis assert_test(test_case, _build_metrics()).
    ...


@pytest.mark.parametrize("question", _QUESTIONS)
def test_chatbot_v2_friendly(question):
    # TODO 3 : idem mais avec la version "v2_friendly".
    ...


@log_hyperparameters
def hyperparameters():
    return {
        "experiment": "ab_prompt_tone",
        "variants": "v1_terse vs v2_friendly",
    }
