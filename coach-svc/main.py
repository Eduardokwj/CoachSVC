from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="coach-svc",
    description="Serviço de coaching: 1RM, volume e plano semanal.",
    version="1.0.0",
)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/one_rm")
def one_rm(
    load_kg: float = Form(..., description="Carga (kg)"),
    reps: int = Form(..., description="Repetições"),
    method: str = Form("epley", description="epley | brzycki"),
):
    if method.lower() == "brzycki":
        one_rm_val = load_kg * (36 / (37 - reps))
    else:
        one_rm_val = load_kg * (1 + reps / 30)
    return {"one_rm": round(one_rm_val, 2)}

@app.post("/volume")
def volume(
    exercise_id: int = Form(..., description="ID do exercício"),
    sets: int = Form(..., description="Séries"),
    reps: int = Form(..., description="Repetições"),
    load_kg: float = Form(..., description="Carga (kg)"),
):
    vol = sets * reps * load_kg
    return {"exercise_id": exercise_id, "volume": vol}

@app.post("/plan")
def plan(
    exercise_id: int = Form(..., description="ID do exercício"),
    sets: int = Form(..., description="Séries"),
    reps: int = Form(..., description="Repetições"),
    load_kg: float = Form(..., description="Carga (kg)"),
    rir: Optional[int] = Form(None, description="Reps in Reserve (opcional)"),
    experience: str = Form("intermediate", description="beginner | intermediate | advanced"),
    goal: str = Form("hypertrophy", description="hypertrophy | strength | endurance"),
):
    base = {
        "exercise_id": exercise_id,
        "sets": sets,
        "reps": "8-12" if goal == "hypertrophy" else reps,
        "load_kg": float(load_kg),
        "rir": rir,
    }
    week_plan = [
        {"week": 1, "target": [base]},
        {"week": 2, "target": [{**base, "load_kg": round(load_kg * 1.02, 2)}]},
        {"week": 3, "target": [{**base, "load_kg": round(load_kg * 1.04, 2)}]},
        {"week": 4, "deload": True, "note": "reduzir volume em ~30%"},
    ]
    return {"week_plan": week_plan, "athlete": {"experience": experience, "goal": goal}}
