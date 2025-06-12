from jupyterquiz import display_quiz

quizz =[{
        "question": "Was ist ein gerichteter Graph?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "Ein Graph bei dem man nur entlang der Pfeilrichtung darf.",
                "correct": True
            },
            {
                "code": "Ein Graph bei dem man überall entlang darf.",
                "correct": False
            },
            {
                "code": "Ein Graf ist eine ge- adelte Person.",
                "correct": False
            }
        ]
    },
    {
        "question": "Welche Menge beschreibt ALLE Kanten von Abbildung 1?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": " {(1;2),(1;3),(2;1),(2;4),(3;1),(4:1)} ",
                "correct": True,
                "feedback": "Genau hier sind wirklich alle Kanten und Richtungen beschrieben."
            },
            {
                "code": "{(1;2),(1;3),(2;4),(3;3)}",
                "correct": False,
                "feedback": "Sind das wirklich alle Kanten?"
            },
            {
                "code": "42, die Antwort \n auf fast alles",
                "correct": True,
                "feedback": "Die Antwort auf fast alles."
            },
            {
                "code": "{}",
                "correct": False
            }
        ]
    },
    {
        "question": "Woraus darf die Bezeichnung der Kanten bestehen?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "Nur aus Zahlen",
                "correct": False,
                "feedback": "Wirklich?"
            },
            {
                "code": "Nur aus Unicode \n Zeichen",
                "correct": False,
                "feedback": "Wirklich?"
            },
            {
                "code": "aus einem beliebigen \n Bezeichner",
                "correct": True,
                "feedback": "Genau."
            },
        ]
    }
]

display_quiz(quizz)