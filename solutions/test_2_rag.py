"""Exercice 2 — Évaluation d'un pipeline RAG (solution).

Objectif : comparer deux réponses à une même question. La première est fidèle
au contexte retrouvé, la seconde invente un détail absent du contexte
(« free shipping »). FaithfulnessMetric doit faire échouer ce second cas.
"""

from deepeval import assert_test
from deepeval.metrics import ContextualRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

_RETRIEVAL_CONTEXT = [
    "All customers are eligible for a 30 day full refund at no extra cost.",
    "Refunds are processed within 5 business days.",
]

_FAITHFULNESS = FaithfulnessMetric(threshold=0.7, include_reason=True)
_CONTEXTUAL_RELEVANCY = ContextualRelevancyMetric(threshold=0.7, include_reason=True)


def test_rag_faithful_answer():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="We offer a 30-day full refund at no extra cost.",
        retrieval_context=_RETRIEVAL_CONTEXT,
    )
    assert_test(test_case, [_FAITHFULNESS, _CONTEXTUAL_RELEVANCY])


def test_rag_hallucinated_answer():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output=(
            "We offer a 30-day full refund and free return shipping "
            "via DHL Express."
        ),
        retrieval_context=_RETRIEVAL_CONTEXT,
    )
    # Ce test DOIT échouer : « free return shipping via DHL Express » n'est
    # pas présent dans le retrieval_context. C'est le comportement attendu
    # pour démontrer la détection d'hallucination.
    assert_test(test_case, [_FAITHFULNESS])
