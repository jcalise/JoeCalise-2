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

'''
class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed_num = None
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.cap:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"
    '''
    
