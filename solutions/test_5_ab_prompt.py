"""Exercice 5 — A/B testing d'un prompt (solution).

Objectif : comparer deux versions d'un chatbot (souvent : deux prompts
différents) sur le même jeu de questions. C'est le workflow le plus
fréquent dans la vraie vie : « est-ce que ce nouveau prompt améliore
vraiment quelque chose ? ».

Ici, on simule deux chatbots `v1` (réponses sèches) et `v2` (réponses
chaleureuses et orientées client) et on les évalue sur les mêmes deux
questions avec une métrique custom GEval qui mesure la convivialité.
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
    return [
        AnswerRelevancyMetric(threshold=0.7),
        GEval(
            name="Friendliness",
            criteria=(
                "Evaluate whether the actual output feels warm, empathetic "
                "and customer-friendly. Terse transactional answers should "
                "score lower than answers that acknowledge the customer."
            ),
            evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
            threshold=0.5,
        ),
    ]


@pytest.mark.parametrize("question", _QUESTIONS)
def test_chatbot_v1_terse(question):
    test_case = LLMTestCase(
        input=question,
        actual_output=_chatbot(question, "v1_terse"),
    )
    assert_test(test_case, _build_metrics())


@pytest.mark.parametrize("question", _QUESTIONS)
def test_chatbot_v2_friendly(question):
    test_case = LLMTestCase(
        input=question,
        actual_output=_chatbot(question, "v2_friendly"),
    )
    assert_test(test_case, _build_metrics())


@log_hyperparameters
def hyperparameters():
    return {
        "experiment": "ab_prompt_tone",
        "variants": "v1_terse vs v2_friendly",
    }
