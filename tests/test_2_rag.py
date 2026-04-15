"""Exercice 2 — Évaluation d'un pipeline RAG.

Contexte : votre RAG récupère des passages de la base de connaissances puis
un LLM génère une réponse. Vous voulez vérifier que cette réponse est bien
*fidèle* au contexte (pas d'hallucination) et que le contexte est bien
*pertinent* par rapport à la question.

Métriques à utiliser :
  - FaithfulnessMetric         : l'output invente-t-il des faits absents
                                 du retrieval_context ?
  - ContextualRelevancyMetric  : les passages récupérés sont-ils pertinents
                                 vis-à-vis de l'input ?

Commande pour lancer ce fichier :
    uv run deepeval test run tests/test_2_rag.py

Attention : le second test (hallucination) DOIT échouer. C'est ce qui
démontre que la métrique fait bien son travail.
"""

from deepeval import assert_test
from deepeval.metrics import ContextualRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

# Contexte récupéré par le RAG — partagé entre les deux tests.
_RETRIEVAL_CONTEXT = [
    "All customers are eligible for a 30 day full refund at no extra cost.",
    "Refunds are processed within 5 business days.",
]


def test_rag_faithful_answer():
    # TODO 1 : créer un LLMTestCase fidèle au contexte :
    #   - input             : "What if these shoes don't fit?"
    #   - actual_output     : une reformulation fidèle du contexte ci-dessus
    #   - retrieval_context : _RETRIEVAL_CONTEXT
    test_case = ...

    # TODO 2 : instancier FaithfulnessMetric(threshold=0.7, include_reason=True)
    faithfulness = ...

    # TODO 3 : instancier ContextualRelevancyMetric(threshold=0.7, include_reason=True)
    contextual_relevancy = ...

    # TODO 4 : assert_test(test_case, [faithfulness, contextual_relevancy])
    ...


def test_rag_hallucinated_answer():
    # TODO 5 : créer un LLMTestCase qui invente volontairement un détail
    #          absent du contexte (par exemple : « free return shipping
    #          via DHL Express »).
    test_case = ...

    # TODO 6 : assert_test avec uniquement FaithfulnessMetric.
    #          Ce test DOIT échouer — c'est attendu.
    ...
