# Tasks

## Part A — Baseline Python Diagnostic (45–60 min)

> Do not over-engineer. Clean, readable code with brief comments is ideal. Put answers in a single Jupyter notebook or a few `.py` scripts.

1) **Core Python (functions + types)**
   - Write `normalize_names(seq: list[str]) -> list[str]` that lowercases, trims, removes punctuation, and replaces spaces with underscores.
   - Write `rolling_std(values: list[float], window: int) -> list[float]` (population std). For the first `window-1` positions, return `NaN`.
   - Add 2–3 unit-style assertions or doctests for each.

2) **Files & CSV**
   - Load `data/nyc_311_sample.csv`.
   - Compute:
     - Top 5 `complaint_type` by count.
     - Median **resolution time in hours** (difference between `created_date` and `closed_date`, ignoring blank `closed_date`).
     - Percent of missing `descriptor` values (empty string counts as missing).

3) **pandas: groupby/rolling**
   - Load `data/nyc_pharmacy_utilization.csv`.
   - For each `facility_id`, compute monthly `spend_usd`, then a **3‑month rolling mean** of spend.
   - Find the **top 3 facilities by spend volatility** (standard deviation of monthly spend).

4) **Modeling (light)**
   - Using the pharmacy dataset, build a simple **linear regression** to predict `readmissions_rate` from `spend_usd` per patient and `generic_fill_rate`.
   - Split into train/test; report **RMSE** and **R²**; write 3–4 sentences interpreting coefficients and limitations.

5) **Visualization**
   - Produce one clean matplotlib line chart: monthly `spend_usd` vs. the 3‑month rolling mean for a chosen facility.

6) **Reproducibility**
   - Create/update `requirements.txt` or use the provided `environment.yml`.
   - Write a short **README** explaining: data, methods, results, and how to run your code.

---

## Part B — Study Subject 01 (Week 1–2)

**Learning goals**
- Python + pandas fluency for tabular data.
- SQL foundations (if you have time): joins, aggregations, window functions (document queries in a `.sql` file).
- Communicating insights succinctly.

**Suggested sequence**
1. Python refresh (functions, comprehensions, pathlib, datetime).  
2. pandas core (indexing, groupby, merge, pivot, rolling).  
3. Stats mini‑module (CI, p‑values, linear regression basics).  
4. Visualization & storytelling (matplotlib + a 1‑page stakeholder brief).

**Deliverables**
- One polished notebook that answers all diagnostic tasks (Part A).
- One extra mini‑analysis on a question you choose (2–3 figures + short narrative).
- Push to GitHub or zip your folder.

**Quality bar (self‑check)**
- No silent failures; handle missing values explicitly.
- Functions have type hints; code passes `flake8`/`ruff` or basic linting.
- README tells a non‑technical stakeholder what to do with your results.
