class Doctor:
    def __init__(self, m, n, windows):
        self.windows_total = m
        self.patients_total = n
        patients = []
        for i, window in enumerate(windows):
            patients.append(Patient(number=i, window=window))
        self.patients = patients

class Patient:
    def __init__(self, number, window):
        self.number = number
        self.window = window

t = int(input())
doctors = []
for _ in range(t):
    n, m = [int(item) for item in input().split(" ")]
    windows = [int(item) for item in input().split(" ")]
    doctors.append(Doctor(n, m, windows))

for doctor in doctors:
    doctor : Doctor = doctor
    print(doctor.patients)
    sorted_by_windows_patients = sorted(doctor.patients, key=lambda patient: patient.window)
    # print(sorted_by_windows_patients)

    print([patient.window for patient in sorted_by_windows_patients])
    


