from typing import List
from schemas import SetEntry, PlanWeek, PlanItem


def one_rm(load_kg: float, reps: int, method: str = "epley") -> float:
    reps = max(1, reps)
    if method == "brzycki":
        # Brzycki: 1RM = w * (36 / (37 - r))
        return load_kg * (36 / (37 - reps))
    # Epley (default): 1RM = w * (1 + r/30)
    return load_kg * (1 + reps / 30)


def recommend_progression(entries: List[SetEntry]) -> List[PlanWeek]:
    """
    Progressão simples:
    - Semanas 1..3: +2% na carga a cada semana (mantém sets e reps alvo 8-12)
    - Semana 4: deload (reduz volume ~30%)
    """
    weeks: List[PlanWeek] = []
    inc = 0.02  # 2% por semana

    for w in range(1, 4):
        target = []
        for e in entries:
            load = round(e.load_kg * (1 + inc * (w - 1)), 1)
            target.append(PlanItem(exercise_id=e.exercise_id, sets=e.sets, reps="8-12", load_kg=load))
        weeks.append(PlanWeek(week=w, target=target))

    weeks.append(PlanWeek(week=4, deload=True, note="reduzir volume em ~30%"))
    return weeks


def session_volume(entries: List[SetEntry]) -> float:
    return float(sum(e.sets * e.reps * e.load_kg for e in entries))
