# Roadmap

Target for v0.1 public release: **Q4 2026 / Q1 2027**.

This roadmap is a living document. Milestones may shift; the structure is the commitment.

## Phase 0 — Setup ✅

- [x] Repository initialized
- [x] Python packaging (`pyproject.toml`, hatchling backend)
- [x] Dev tooling: ruff, mypy, pytest, pre-commit
- [x] CI pipeline (GitHub Actions): lint, type check, tests
- [x] Module skeleton (data, exposure, tables, study, credibility, viz, reports)
- [x] License (MIT), README, gitignore

## Phase 1 — Data layer 🚧

- [ ] Pydantic schemas: `Policy`, `DecrementEvent`, `Portfolio`
- [ ] CSV / Excel / Parquet ingestion
- [ ] Synthetic portfolio generator (configurable: size, product mix, age/sex distribution, decrement rates)
- [ ] Exposure calculation engine — central exposure (Hoem) and initial exposure approaches
- [ ] Decrement classification and competing-risks handling
- [ ] Unit tests with synthetic fixtures
- [ ] Example notebook: generate synthetic portfolio + compute exposure

## Phase 2 — Tables and expected ⏳

- [ ] Table abstraction (select-and-ultimate support)
- [ ] Packaged Italian tables: SIM 1981 / 1992 / 2004, SIF, IPS55
- [ ] Packaged international tables: A2000, selected SOA mortality tables
- [ ] q ↔ μ conversions and age-nearest / age-last conventions
- [ ] Expected decrement computation
- [ ] Tests against published benchmarks

## Phase 3 — A/E engine ⏳

- [ ] Core A/E computation by cohort
- [ ] Segmentation API — group by any column or computed dimension (age band, duration band, etc.)
- [ ] Binomial confidence intervals on A/E
- [ ] Credibility weighting: limited fluctuation
- [ ] Credibility weighting: Bühlmann (empirical Bayes)
- [ ] Multi-decrement studies (mortality + lapse combined)
- [ ] Tests with known analytical cases

## Phase 4 — Visualization & reporting ⏳

- [ ] Plotly charts: A/E by segment (bar), heatmap (age × duration), time series (study year)
- [ ] HTML report template (Jinja2) with executive summary + drilldowns
- [ ] CLI entry point: `actxps run --config study.yaml`
- [ ] Optional Streamlit dashboard for interactive exploration

## Phase 5 — Polish & launch ⏳

- [ ] Documentation site (mkdocs-material) with API reference + tutorials
- [ ] End-to-end tutorial notebook on synthetic data
- [ ] PyPI release (`pip install actxps-py`)
- [ ] CHANGELOG entry, release notes
- [ ] LinkedIn announcement post, blog post on methodology

## Out of scope for v0.1

- Stochastic mortality projection (Lee-Carter, CBD)
- IFRS 17 / Solvency II reserving calculations
- Pricing and product design
- Real-time portfolio monitoring
- Predictive modeling (ML-based mortality / lapse models)

These may appear in v0.2+ depending on adoption and feedback.
