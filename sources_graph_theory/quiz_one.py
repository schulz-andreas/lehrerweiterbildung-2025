from jupyterquiz import display_quiz

quizz =[{
        "question": "Was ist ein Graph?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "Ein Graph zeigt zahlen oder Werte an und kann mehrere Dimensionen abbilden.",
                "correct": False
            },
            {
                "code": "Ein Graph ist ein mathematisches Konstrukt, welches Beziehungen abbilden kann.",
                "correct": True
            },
            {
                "code": " deine Mutter ",
                "correct": False
            }
        ]
    },
    {
        "question": "Wie viele Nachkommastellen hat Pi?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": " void",
                "correct": False,
                "feedback": "du bist so dumm"
            },
            {
                "code": "genau 3",
                "correct": False
            },
            {
                "code": "Genau 27",
                "correct": True
            },
            {
                "code": "ich glaube mehr als 4",
                "correct": False
            }
        ]
    },
    {
        "question": "Wozu braucht man Schleifen in der Programmierung?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "Für besseres Design ...",
                "correct": False,
                "feedback": "Haha du Opfer ..."
            },
            {
                "code": "Um Aufgaben zu wiederholen",
                "correct": True,
                "feedback": "Ich weiß du trägst Schuhe mit Klettverschluss."
            },
        ]
    }
]
display_quiz(quizz)