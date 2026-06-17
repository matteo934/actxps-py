"""Exposure computation — central and initial exposure approaches.

Implements the exposure calculation engine that converts a portfolio of
policies with effective dates and decrement events into person-years of
exposure to risk, segmented by relevant dimensions (age, duration, calendar
year, etc.).

Supported approaches:
- Central exposure (Hoem)
- Initial exposure (with deaths weighted to year-end)
"""
