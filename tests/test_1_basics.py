"""Exercice 1 — Premiers tests avec DeepEval.

Contexte : un chatbot e-commerce répond à la question d'un client sur un
remboursement. On veut évaluer la qualité de sa réponse avec deux métriques :

  1. AnswerRelevancyMetric  — métrique intégrée, paramétrée par un threshold.
  2. GEval                  — métrique 100% custom, pilotée par un critère
                              rédigé en langage naturel.

Commande pour lancer ce fichier :
    uv run deepeval test run tests/test_1_basics.py

Objectif : que le test passe avec un score ≥ 0.7 sur les deux métriques.
"""

from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams


def test_chatbot_refund_answer():
    # TODO 1 : créer un LLMTestCase avec :
    #   - input          : "What if these shoes don't fit?"
    #   - actual_output  : "We offer a 30-day full refund at no extra cost."
    #   - expected_output: une reformulation équivalente de votre choix
    test_case = ...

    # TODO 2 : instancier AnswerRelevancyMetric avec threshold=0.7
    #          et include_reason=True (pour voir le raisonnement dans le rapport).
    answer_relevancy = ...

    # TODO 3 : instancier un GEval nommé "Politeness" qui évalue si la
    #          réponse est polie et orientée client.
    #          Indices :
    #            - name="Politeness"
    #            - criteria="..." (à rédiger en anglais, une phrase suffit)
    #            - evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT]
    #            - threshold=0.5
    politeness = ...

    # TODO 4 : appeler assert_test(test_case, [answer_relevancy, politeness])
    ...
