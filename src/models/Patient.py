from datetime import date
from typing import Optional
from pydantic import BaseModel

class Patient(BaseModel):
    patientId: int
    firstName: str
    lastName: str
    phoneNumber: Optional[str] = None
    email: Optional[str] = None
    mailingAddress: Optional[str] = None
    dateOfBirth: date

    def get_age(self) -> int:
        """Calculates the patient's current age."""
        today = date.today()
        age = today.year - self.dateOfBirth.year
        # Adjust age if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.dateOfBirth.month, self.dateOfBirth.day):
            age -= 1
        return age