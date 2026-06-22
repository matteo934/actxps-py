from pydantic import BaseModel, computed_field
from datetime import date
from typing import Literal

class Policy(BaseModel):
    policy_id: str
    birth_date: date
    issue_date: date
    sex: Literal["M","F"]
    status: Literal["Active","Lapsed","Death"]

    @computed_field
    @property
    def age(self) -> int: 
        if (date.today().month, date.today().day)<(self.birth_date.month, self.birth_date.day): 
            return date.today().year-self.birth_date.year-1
        else: 
            return date.today().year-self.birth_date.year



p = Policy(policy_id="A123", birth_date="1996-12-12", issue_date="2026-06-19", sex='M', status="Active")
print(p)

