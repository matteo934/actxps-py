"""Standard mortality and lapse tables.

Packaged tables for use as expected-decrement references:

Italian tables:
- SIM 1981, SIM 1992, SIM 2004 (male mortality)
- SIF (female mortality)
- IPS55 (annuitant mortality)

International tables:
- A2000 series
- Selected SOA standard mortality tables

Provides a unified ``Table`` abstraction supporting select-and-ultimate
structures, age conventions (nearest, last), and q ↔ μ conversions.
"""
