"""Exercice 1 — Premiers tests avec DeepEval (solution).

Objectif : évaluer la réponse d'un chatbot e-commerce avec deux métriques
complémentaires : une métrique paramétrée (AnswerRelevancy) et une métrique
GEval custom pilotée par un critère en langage naturel.
"""

from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


def test_chatbot_refund_answer():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="We offer a 30-day full refund at no extra cost.",
        expected_output="You can return shoes within 30 days for a full refund.",
    )

    answer_relevancy = AnswerRelevancyMetric(threshold=0.7, include_reason=True)

    politeness = GEval(
        name="Politeness",
        criteria=(
            "Determine whether the actual output is polite, helpful "
            "and customer-friendly in tone."
        ),
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.5,
    )

    assert_test(test_case, [answer_relevancy, politeness])
