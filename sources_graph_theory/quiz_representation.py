from jupyterquiz import display_quiz

quizz =[{
        "question": "Nenne eine Struktur zur Modellierung eines Graphen?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "eine Adjazenzliste",
                "correct": True
            },
            {
                "code": "eine Adjazenzmatrix",
                "correct": True
            },
            {
                "code": "eine Tabelle",
                "correct": False
            },
            {
                "code": "eine Inzidenzliste",
                "correct": False
            }
        ]
    },
    {
        "question": "Was beschreibt der Eintrag in einer Zelle innerhalb der im Beispiel genutzten Datenstruktur?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": " die Anzahl der \n Menschen auf einer \n Straße ",
                "correct": False,
                "feedback": "Leider Nein"
            },
            {
                "code": " die Entfernung \n zwischen den \n begrenzenden Knoten \n in Metern ",
                "correct": True,
                "feedback": "Richtig"
            },
            {
                "code": " die Geschwindigkeit ",
                "correct": False,
                "feedback": "Leider Nein"
            },
            {
                "code": " nichts ",
                "correct": False
            }
        ]
    },
    {
        "question": " Wäre es denkbar die das Werte andere Dinge repräsentieren wie ...",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "die durchschnitt- \n liche Dauer auf die- \n ser wenn man von \n A nach B will.",
                "correct": True,
                "feedback": ""
            },
            {
                "code": " den Fluss an Ver- \n kehrteilnehmern in- \n nerhalb einer \n Zeiteinheit ",
                "correct": True,
                "feedback": ""
            },
            {
                "code": " die Verzögerung in einem Datenübertragungsnetz von einem Netznoten zum anderen",
                "correct": True,
                "feedback": ""
            },
        ]
    }
]

display_quiz(quizz)