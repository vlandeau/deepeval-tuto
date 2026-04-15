"""Exercice 4 — Génération synthétique de cas de test (solution).

Objectif : plutôt qu'écrire un jeu d'évaluation à la main, on laisse un LLM
le générer à partir d'une base de connaissances (quelques passages texte).
C'est la réponse au problème n°1 de l'évaluation LLM : « on n'a pas de
golden set ».
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
    synthesizer = Synthesizer()
    goldens = synthesizer.generate_goldens_from_contexts(
        contexts=_KNOWLEDGE_BASE,
        max_goldens_per_context=1,
        include_expected_output=True,
    )

    assert len(goldens) > 0

    # Dans la vraie vie, on appellerait ici son chatbot avec golden.input
    # pour obtenir un vrai actual_output. Pour la démo, on réutilise
    # l'expected_output comme stand-in — l'évaluation passe trivialement,
    # mais la boucle "génération → évaluation" est complète.
    test_cases = [
        LLMTestCase(
            input=golden.input,
            actual_output=golden.expected_output or "",
            retrieval_context=golden.context,
        )
        for golden in goldens
    ]

    evaluate(
        test_cases=test_cases,
        metrics=[AnswerRelevancyMetric(threshold=0.7)],
    )
