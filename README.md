# actxps-py

> Actuarial experience studies in Python — A/E analysis, credibility, segmentation, and reporting for life insurance portfolios.

[![CI](https://github.com/YOUR_USERNAME/actxps-py/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/actxps-py/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## What is this

`actxps-py` is a Python toolkit for running **actuarial experience studies** on life insurance portfolios — comparing actual mortality, lapse, and surrender experience against expected (table-based or pricing-based) decrements, with credibility weighting, segmentation, and report generation.

Methodologically inspired by the excellent [`actxps`](https://github.com/mattheaphy/actxps) R package by Matt Heaphy, with extended support for European and Italian standard tables (SIM, SIF, IPS) and life insurance product structures common in continental Europe.

## Status

🚧 **Pre-alpha — under active development.** First public release (v0.1) targeted for Q4 2026 / Q1 2027. See [ROADMAP.md](ROADMAP.md) for milestones.

## What v0.1 will do

- Load policy-level portfolio data with exposure periods and decrement events
- Compute central and initial exposure
- Look up expected decrements from packaged standard tables (SIM92, SIF, IPS55, plus selected SOA tables)
- Calculate A/E ratios with binomial confidence intervals
- Segment results by age, sex, duration, product, distribution channel, or any custom dimension
- Apply credibility weighting (Bühlmann, limited fluctuation)
- Generate interactive Plotly visualizations
- Produce standalone HTML reports

## Why

Actuaries running experience studies across Europe largely still rely on Excel pipelines or expensive proprietary platforms. Python has the data tooling but lacks a focused, idiomatic experience-study package. `actxps-py` aims to fill that gap.

## Installation

> Not yet on PyPI. For now, clone and install in development mode:

```bash
git clone https://github.com/YOUR_USERNAME/actxps-py.git
cd actxps-py
uv venv
uv pip install -e ".[dev]"
```

## Quickstart

> ⚠️ API design in progress — the example below is a *sketch* of the intended interface, not yet implemented.

```python
import actxps_py as axp

# Load policies and decrements
portfolio = axp.data.load_portfolio(
    policies="policies.csv",
    decrements="decrements.csv",
)

# Define the study
study = axp.MortalityStudy(
    portfolio=portfolio,
    expected_table=axp.tables.SIM92,
    study_period=("2020-01-01", "2024-12-31"),
)

# Run it
results = study.run(segment_by=["age_band", "sex", "duration_band"])

# Visualize and report
results.plot_ae_by_segment().show()
results.generate_html_report("report.html")
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the full plan. High-level phases:

| Phase | Scope | Status |
|---|---|---|
| 0 | Repo + tooling setup | ✅ Done |
| 1 | Data layer + synthetic generator + exposure | 🚧 |
| 2 | Standard tables + expected decrements | ⏳ |
| 3 | A/E engine + segmentation + credibility | ⏳ |
| 4 | Visualization + HTML reporting | ⏳ |
| 5 | Docs + PyPI release | ⏳ |

## Contributing

This is a personal project but contributions, issues, and discussion are welcome. Open an issue before submitting a PR for anything non-trivial.

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgments

- [`actxps`](https://github.com/mattheaphy/actxps) (R) by Matt Heaphy — methodological inspiration
- [`lifelib`](https://github.com/lifelib-dev/lifelib) — companion ecosystem for actuarial cashflow modeling in Python
- [`lifelines`](https://github.com/CamDavidsonPilon/lifelines) — adjacent survival-analysis tooling
