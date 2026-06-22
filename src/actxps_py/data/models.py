from datetime import date
from typing import Literal

from pydantic import BaseModel, computed_field


class Policy(BaseModel):
    """Represents a single life insurance policy record in an experience study."""

    policy_id: str
    """Unique identifier for the policy."""
    birth_date: date
    """Birth date of the policyholder"""
    issue_date: date
    """Date of the issue"""
    study_start: date
    """Starting date of the study"""
    study_end: date
    """Ending date of the study"""
    sex: Literal["M", "F"]
    """Sex of the policyholder"""
    status: Literal["Active", "Lapsed", "Death"]
    """Status of the policy"""

    @computed_field
    @property
    def age(self) -> int:
        if (date.today().month, date.today().day) < (self.birth_date.month, self.birth_date.day):
            return date.today().year - self.birth_date.year - 1
        else:
            return date.today().year - self.birth_date.year
