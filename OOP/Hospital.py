class Patient(object):
    def __init__(self,id,name,allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = "None"

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Unfortuantely, the hospital is full right now. Patient", patient.name, "not admitted."
        else:
            self.patients.append(patient)
            patient.bed = len(self.patients)
        return self

    def discharge(self, pid):
        new_list = []
        for patient in self.patients:
            if patient.id != pid:
                new_list.append(patient)
            else:
                patient.bed = "None"
        self.patients = new_list

    def display(self):
        for patient in self.patients:
            print "Patient:", patient.name, ". Allergies:", patient.allergies, ". Bed:", patient.bed

p1 = Patient(123, "Joe", "None")
p2 = Patient(124, "Fred", "All of them")
p3 = Patient(125, "Greg", "Penicillin")
p4 = Patient(126, "Fran", "Non")

hosp = Hospital("Saint Seattle's", 3)

hosp.admit(p1).admit(p2).admit(p3).admit(p4)
hosp.display()
hosp.discharge(123)
hosp.display()
