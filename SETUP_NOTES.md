# Note di setup — leggimi prima di pushare

Questo file è solo per te, Matteo. Cancellalo prima del primo commit pubblico (o quando ti senti sicuro che hai capito tutto).

## Cosa devi fare nei prossimi 15 giorni (Fase 0)

### Step 1 — Personalizza i placeholder (5 minuti)

Cerca e sostituisci ovunque (è facile con un find/replace in VS Code):

- `YOUR_NAME` → il tuo nome completo (es. `Matteo Rossi`)
- `YOUR_USERNAME` → il tuo username GitHub
- `your.email@example.com` → la tua email pubblica (puoi usare un alias se preferisci)

File da pulire/personalizzare:
- `pyproject.toml`
- `README.md`
- `LICENSE`
- `src/actxps_py/__init__.py`

### Step 2 — Crea il repo su GitHub (2 minuti)

- Nuovo repo: `actxps-py`
- Pubblico
- Descrizione: "Actuarial experience studies in Python — A/E analysis, credibility, segmentation, and reporting for life insurance portfolios."
- Topics da aggiungere: `actuarial`, `python`, `insurance`, `experience-study`, `mortality`, `life-insurance`
- NON aggiungere README/license/gitignore — li abbiamo già

### Step 3 — Push iniziale (5 minuti)

```bash
cd actxps-py
git init
git add .
git commit -m "chore: initial scaffold (Phase 0)"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/actxps-py.git
git push -u origin main
```

### Step 4 — Installa uv (se non l'hai già) (2 minuti)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# o con homebrew
brew install uv
```

Riferimento: https://docs.astral.sh/uv/

### Step 5 — Setup ambiente locale (5 minuti)

```bash
cd actxps-py
uv venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
uv pip install -e ".[dev]"
```

### Step 6 — Verifica che tutto giri (3 minuti)

```bash
# Test
pytest

# Lint
ruff check .

# Format check
ruff format --check .

# Type check
mypy src/
```

Tutti devono passare. Se qualcosa è rosso, è qualcosa da sistemare *prima* di iniziare Fase 1 — questa è proprio la disciplina che il progetto ti deve insegnare.

### Step 7 — Setup pre-commit (5 minuti)

```bash
uv pip install pre-commit
pre-commit install
```

Da ora ogni commit gira ruff + ruff-format + alcuni controlli base prima di committare. Se qualcosa è da sistemare, te lo dice e blocca il commit. Questo è quello che ti fa apprendere Python "alla giusta", costringendoti a scrivere codice pulito dal primo giorno.

### Step 8 — Verifica CI verde su GitHub (5 minuti)

Dopo il primo push, vai su `https://github.com/YOUR_USERNAME/actxps-py/actions` e verifica che il workflow CI giri e passi. Se è rosso, debugga prima di iniziare Fase 1.

### Step 9 — Apri il primo issue (3 minuti)

Vai sui Issues del repo e apri:

**Titolo**: `Phase 1: implement Policy and DecrementEvent Pydantic schemas`

**Body**:
```
First task of Phase 1 (data layer).

Define Pydantic models for:
- `Policy`: policy_id, product_code, sex, date_of_birth, effective_date, premium, sum_assured, ...
- `DecrementEvent`: policy_id, event_date, event_type (death/lapse/surrender/maturity), cause_code

Acceptance criteria:
- [ ] Models defined in `src/actxps_py/data/schemas.py`
- [ ] Tests covering valid and invalid inputs in `tests/test_schemas.py`
- [ ] mypy strict passes
- [ ] ruff passes
```

Questo issue è il tuo *primo lavoro vero* dopo Fase 0. Ti aspetta lì quando sei pronto.

---

## Quanto tempo è realistico per Fase 0?

**~3-4 ore concentrate** se hai dimestichezza minima con Git/Python. **~6-8 ore** se è la prima volta che fai un setup serio. Una serata o due, non di più.

## Cosa NON fare in Fase 0

- Non iniziare a scrivere logica attuariale
- Non scegliere già le tavole esatte da packagare
- Non perdere tempo a "imparare Python prima di partire" — impari facendo, dentro il progetto
- Non strafare con il README — quello che c'è va bene per ora, lo arricchirai man mano

## Quando puoi considerare Fase 0 chiusa

Tutti i criteri devono essere veri:

- [ ] Repo pubblico su GitHub con il commit iniziale
- [ ] CI verde sul main
- [ ] `pytest` passa localmente
- [ ] `ruff`, `ruff format --check`, `mypy` passano localmente
- [ ] pre-commit installato e funzionante
- [ ] Primo issue di Phase 1 aperto
- [ ] Hai cancellato questo file (`SETUP_NOTES.md`) dal repo

A quel punto, Vietnam o non Vietnam, sei oltre l'attivation energy. Il progetto è vivo.
