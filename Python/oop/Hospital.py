class Patient(object):
    def __init__(self, patid, name, allergies):
        self.patid = patid
        self.name = name
        self.allergies = allergies
        self.bed = "0"

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            return "Sorry, the hospital is at maximum occupancy"
        else:
            patient.bed = len(self.patients)
            self.patients.append(patient)
            return "Admitance is complete"

    def discharge(self, patientid):
        patient = 0
        for i in range(0, len(self.patients)-1):
            patient = self.patients[i]
            if patientid == patient.patid:
                print "Patient: " + patient.name + " removed!"
                patient.bed = "0"
                return self.patients.pop(i)

patient1 = Patient(0, "Will", "Fish")
patient2 = Patient(1, "James", "Tree Nuts")
patient3 = Patient(2, "Stu", "Shellfish, Pork")
patient4 = Patient(3, "Jane", "Tomato, Beer")
patient5 = Patient(4, "Pete",  "Dairy")

hospital1 = Hospital("First Paient Care First", 2)

print hospital1.admit(patient1)
print hospital1.admit(patient2)
print hospital1.admit(patient3)
print hospital1.admit(patient4)
print hospital1.admit(patient5)

hospital1.discharge(0)