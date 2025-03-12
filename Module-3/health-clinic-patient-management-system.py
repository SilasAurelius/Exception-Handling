def add_patients(patients, patient_id, name, age):
    if patient_id not in patients:
        patients[patient_id] = {"name": name, "age": age, "visits": []}
        print(f"Patient 'name' added with ID: {patient_id}.")
    else:
        print(f"Patient with ID {patient_id} already exists.")



clinic_patients = {}

