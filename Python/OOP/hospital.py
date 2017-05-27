"""
You're going to build a hospital with patients in it! Create a hospital class.

Before looking at the requirements below, think about the potential characteristics
of each patient and hospital. How would you design each?

> Patient
Attributes:
* Id: an id number
* Name
* Allergies
* Bed number: should be none by default

> Hospital
Attributes:
* Patients: an empty array
* Name: hospital name
* Capacity: an integer indicating the maximum number of patients the hospital can hold.

Methods:
* Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
* Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
"""

class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_num = 0

    # display patient info
    def patient_info(self):
        print "PATIENT INFORMATION:"
        print "\tPatient ID: {}".format(self.id)
        print "\tPatient name: {}".format(self.name)
        print "\tPatient allergies: {}".format(self.allergies)
        print "\tPatient bed number: {}".format(self.bed_num)

patient1 = Patient(1, "Lea Salonga", "peanut allergy")
patient2 = Patient(2, "Missy Morrison", "chocolate allergy")
patient3 = Patient(3, "James Wall", "pollen")
print patient2.patient_info()

class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.bed_num = 0

    # add a patient to the list of patients
    def admit(self, *new_patients):
        for new_patient in new_patients:
            self.patients.append(new_patient)
            # assign a bed number to new patient
            self.bed_num += 1
            new_patient.bed_num += self.bed_num
        return self

    # look up and remove a patient from the list of patients
    def discharge(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                self.patients.remove(patient)
                # Change bed number for this patient back to none.
                patient.bed_num = 0
        return self

    # display hospital and patient information
    def hospital_info(self):
        print "HOSPITAL INFORMATION:"
        print "\tHospital name: {}\n\tCapacity: {}".format(self.hospital_name, self.capacity)
        print "PATIENTS AT THIS HOSPITAL:"
        for patient in self.patients:
            print "\tPatient name: {}\n\tBed number: {}".format(patient.name, patient.bed_num)
        return self

hospital1 = Hospital("Angel Hospital", 50)
hospital1.admit(patient1, patient2, patient3).discharge("Missy Morrison").hospital_info()
