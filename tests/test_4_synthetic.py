"""Exercice 4 — Génération synthétique de cas de test.

Contexte : le problème le plus fréquent en évaluation LLM est « on n'a pas
de golden set ». DeepEval fournit un `Synthesizer` qui génère des paires
(question, réponse attendue) à partir de morceaux de votre base de
connaissances.

Vous allez :
  1. fournir une petite base de connaissances en dur (2 contextes),
  2. laisser le Synthesizer générer 1 golden par contexte,
  3. convertir les goldens en LLMTestCase et les évaluer avec
     AnswerRelevancyMetric.

Commande pour lancer ce fichier :
    uv run deepeval test run tests/test_4_synthetic.py
"""

from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.synthesizer import Synthesizer
from deepeval.test_case import LLMTestCase

_KNOWLEDGE_BASE = [
    [
        "All customers are eligible for a 30 day full refund at no extra cost.",
        "Refunds are processed within 5 business days.",
    ],
    [
        "Standard shipping takes 3 to 5 business days across the country.",
        "Express shipping is available for next-day delivery at $15.",
    ],
]


def test_generate_and_evaluate_synthetic_cases():
    # TODO 1 : instancier un Synthesizer()
    synthesizer = ...

    # TODO 2 : appeler synthesizer.generate_goldens_from_contexts avec :
    #            - contexts=_KNOWLEDGE_BASE
    #            - max_goldens_per_context=1
    #            - include_expected_output=True
    goldens = ...

    assert len(goldens) > 0

    # TODO 3 : transformer la liste de goldens en une liste de LLMTestCase.
    #          Pour chaque golden, créer un LLMTestCase avec :
    #            - input             : golden.input
    #            - actual_output     : golden.expected_output (stand-in pour
    #                                  la démo — en vrai, ce serait la
    #                                  réponse de votre chatbot sur golden.input)
    #            - retrieval_context : golden.context
    test_cases = ...

    # TODO 4 : appeler evaluate() avec ces test_cases et la métrique
    #          AnswerRelevancyMetric(threshold=0.7)
    ...
