from imageRecognitionAPI.schema import Symptom


def get_risk_level(symptom: Symptom):
    if not (symptom.fever or symptom.dry_cough or symptom.tiredness or symptom.breathing_problem):
        return 'Level of Covid Risk: Low'

    if not (symptom.breathing_problem or symptom.dry_cough):
        if symptom.fever:
            return 'Level of Covid Risk: Moderate'

    if symptom.breathing_problem:
        return 'Level of Covid Risk: High'

    return 'THIS IS A DEMO COVID-19 APP'
