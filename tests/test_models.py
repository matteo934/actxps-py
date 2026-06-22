import pytest
from pydantic import ValidationError

from actxps_py.data.models import Policy


def test_valid_policy_creates_without_errors() -> None:
    """A valid policy record is created without raising exceptions."""
    p = Policy(
        policy_id="A123",
        birth_date="1990-01-15",
        issue_date="2020-06-01",
        study_start="2023-01-01",
        study_end="2023-12-31",
        sex="M",
        status="Active",
    )
    assert p.policy_id == "A123"
    assert p.sex == "M"
    assert p.status == "Active"


def test_invalid_status_raises_error() -> None:
    """A policy with an invalid status raises a ValidationError."""
    with pytest.raises(ValidationError):
        Policy(
            policy_id="B456",
            birth_date="1990-01-15",
            issue_date="2020-06-01",
            study_start="2023-01-01",
            study_end="2023-12-31",
            sex="M",
            status="Invalid",
        )


def test_age_computed_correctly_before_birthday() -> None:
    """Age is correctly reduced by 1 when birthday has not yet occurred this year."""
    p = Policy(
        policy_id="C789",
        birth_date="1990-12-15",
        issue_date="2020-06-01",
        study_start="2023-01-01",
        study_end="2023-12-31",
        sex="M",
        status="Active",
    )
    assert p.age == 35
