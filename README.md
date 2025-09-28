
---

# 📄 `coach-svc/README.md`
```markdown
# coach-svc

API secundária do MVP **GymHub**, responsável pelas regras de negócio:  
- Cálculo de **1RM**  
- Cálculo de **volume de treino**  
- Geração de **plano semanal**  
- CRUD de **templates de treino** (para cobrir os verbos REST)

---

## ⚙️ Requisitos
- Python 3.11+
- FastAPI + Uvicorn
- Docker

---

## 🔧 Instalação local
```bash
python -m venv .venv

# ativar (Windows)
.\.venv\Scripts\activate

# ativar (Linux/Mac)
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

▶️ Execução local

```bash
uvicorn main:app --reload --port 8000
```
Abra: http://localhost:8000/

▶️ Execução via Docker

```bash
docker build -t coach-svc .
docker run --rm -p 8000:8000 coach-svc
```

Integração com GymHub

A API principal consome o endpoint:

`POST /plan` → exposto em `/recommendations` no GymHub.

No `.env` do GymHub:

COACH_SVC_URL=http://coach-svc:8000

