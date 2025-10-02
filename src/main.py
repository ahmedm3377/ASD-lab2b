import json
from datetime import date
from typing import List
from models.Patient import Patient

def get_patient_data() -> List[Patient]:
    """Creates and returns a list of Patient objects."""
    return [
        Patient(patientId=1, firstName="Daniel", lastName="Agar", phoneNumber="(641) 123-0009", email="dagar@m.as", mailingAddress="1 N Street", dateOfBirth=date(1987, 1, 19)),
        Patient(patientId=2, firstName="Ana", lastName="Smith", phoneNumber=None, email="amsith@te.edu", mailingAddress=None, dateOfBirth=date(1948, 12, 5)),
        Patient(patientId=3, firstName="Marcus", lastName="Garvey", phoneNumber="(123) 292-0018", email=None, mailingAddress="4 East Ave", dateOfBirth=date(2001, 9, 18)),
        Patient(patientId=4, firstName="Jeff", lastName="Goldbloom", phoneNumber="(999) 165-1192", email="jgold@es.co.za", mailingAddress=None, dateOfBirth=date(1995, 2, 28)),
        Patient(patientId=5, firstName="Mary", lastName="Washington", phoneNumber=None, email=None, mailingAddress="30 W Burlington", dateOfBirth=date(1932, 5, 31)),
    ]

def create_and_write_report():
    """Generates a patient report, sorts it, and writes it to a JSON file."""
    patients = get_patient_data()

    # Create a list of dictionaries with age included
    patient_data_with_age = [
        {"age": patient.get_age(), **patient.dict()} for patient in patients
    ]

    # Sort the list by age in descending order
    sorted_patients = sorted(
        patient_data_with_age, key=lambda p: p["age"], reverse=True
    )

    # Convert the sorted list to a JSON string
    json_output = json.dumps(sorted_patients, indent=2)

    # Write the JSON data to a file
    output_file_path = "patients_report.json"
    with open(output_file_path, "w") as f:
        f.write(json_output)

    print(f"Patient data successfully written to {output_file_path}")

if __name__ == "__main__":
    create_and_write_report()