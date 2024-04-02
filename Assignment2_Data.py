import random  # To assign random values
import time  # to calculate the efficiency of each algorithm
from collections import defaultdict
from enum import Enum

class RandomNames(Enum):
    AHMED = "Ahmed"
    RASHED = "Rashed"
    SALEM = "Salem"
    MUHSEN = "Muhsen"
    KHALED = "Khaled"
    JASEM = "Jasem"
    MUNTHER = "Munther"
    SAMI = "Sami"
    JABER = "Jaber"
    OTHMAN = "Othman"

class RandomMedicalHistory(Enum):
    ENTRY_1 = "Patient has a history of hypertension."
    ENTRY_2 = "Patient underwent surgery for appendicitis last year."
    ENTRY_3 = "Patient is allergic to penicillin."
    ENTRY_4 = "Patient experienced a mild heart attack five years ago."
    ENTRY_5 = "Patient has a family history of diabetes."
    ENTRY_6 = "Patient suffered a concussion from a car accident."
    ENTRY_7 = "Patient has chronic back pain due to a previous injury."
    ENTRY_8 = "Patient was diagnosed with asthma in childhood."
    ENTRY_9 = "Patient has a history of depression and anxiety."
    ENTRY_10 = "Patient underwent knee replacement surgery recently."


class Patient:
    """Class that represent the patients"""
    patient_count = 0

    # Constructor
    def __init__(self, name, date_of_birth, medical_history, phone, admission_date):
        Patient.patient_count += 1
        self._patient_id = f"HP{Patient.patient_count}"  # Generate patient ID automatically
        self._name = name  # patient's name
        self._date_of_birth = date_of_birth  # patient's date of birth
        self._medical_history = medical_history  # patient's medical history
        self._phone = phone
        self._admission_date = admission_date
        self._appointments = []  # list to store appointments
        self._prescriptions = Stack()
        self._record = None

    # Setters and Getters
    def get_patient_id(self):
        return self._patient_id

    def get_name(self):
        return self._name

    def get_date_of_birth(self):
        return self._date_of_birth

    def set_medical_history(self, value):
        self._medical_history = value

    def get_medical_history(self):
        return self._medical_history

    def set_phone(self, value):
        self._phone = value

    def get_phone(self):
        return self._phone

    def set_admission_date(self, value):
        self._admission_date = value

    def get_admission_date(self):
        return self._admission_date

    def get_appointments(self):
        return self._appointments

    def get_prescriptions(self):
        return self._prescriptions

    def remove_appointment(self, appointment):
        self._appointments.remove(appointment)

    def add_prescription(self, prescription):
        self._prescriptions.push(prescription)

    def fulfill_prescription(self):
        if not self._prescriptions.is_empty():
            return self._prescriptions.pop()
        else:
            print("No prescriptions to fulfill.")
            return None

    def add_record(self, record):
        self._record = record  # Assume 'record' is an instance of the 'Record' class

    @staticmethod
    def quicksort_records(records, low, high, sort_key):
        """Sorts the patient records using the quicksort algorithm based on the given sort_key."""
        if low < high:
            # Partition the list
            pi = Patient.partition(records, low, high, sort_key)
            # Sort the partitions
            Patient.quicksort_records(records, low, pi - 1, sort_key)
            Patient.quicksort_records(records, pi + 1, high, sort_key)

    @staticmethod
    def partition(records, low, high, sort_key):
        """Helper function for quicksort_records to partition the sublist."""
        # Pivot (Element to be placed at the right position)
        pivot = getattr(records[high], f'get{sort_key}')()  # Use the getter method
        i = low - 1
        for j in range(low, high):
            if getattr(records[j], f'get{sort_key}')() <= pivot:  # Use the getter method
                # Increment index of smaller element
                i = i + 1
                records[i], records[j] = records[j], records[i]
        records[i + 1], records[high] = records[high], records[i + 1]
        return i + 1

    @staticmethod
    def search_patient(patient_records, patient_id):
        return patient_records.get(patient_id)

    def update_details(self, name=None, date_of_birth=None, medical_history=None):
        if name is not None:
            self._name = name  # update name if provided
        if date_of_birth is not None:
            self._date_of_birth = date_of_birth  # update date of birth if provided
        if medical_history is not None:
            self._medical_history = medical_history  # update medical history if provided

    def add_appointment(self, appointment):
        # Ensure that the appointment is for this patient
        if appointment._patient == self:
            self._appointments.append(appointment)
        else:
            print("This appointment is not for this patient.")

    def print_patient_summary(self):
        """
        Print a summary of the patient's details, appointments, prescriptions, and records.
        """
        print(f"Patient ID: {self._patient_id}")
        print(f"Name: {self._name}")
        print(f"Date of Birth: {self._date_of_birth}")
        print(f"Medical History: {self._medical_history}")
        print(f"Phone: {self._phone}")
        print(f"Admission Date: {self._admission_date}")

        # Print appointments
        if self._appointments:
            print("Appointments:")
            for appointment in self._appointments:
                print(
                    f"- {appointment.get_date()} at {appointment.get_time()} with {appointment.get_doctor().get_name()}")

        # Print prescriptions
        if not self._prescriptions.is_empty():
            print("Prescriptions:")
            for prescription in self._prescriptions.get_items():
                print(
                    f"- Medication: {prescription.get_medication()}, Dosage: {prescription.get_dosage()}, Duration: {prescription.get_duration()}")

        # Print record
        if self._record:
            print("Medical Record:")
            print(f"- Diagnosis: {self._record.get_diagnosis()}")
            print(f"- Treatment Plan: {self._record.get_treatment_plan()}")


class Doctor:
    """Class that represents doctors"""
    doctor_count = 0

    # Constructor
    def __init__(self, name, specialty):
        Doctor.doctor_count += 1
        self._doctor_id = f"HD{Patient.patient_count}"  # Generate patient ID automatically
        self._name = name
        self._specialty = specialty
        self._appointments = []  # List of Appointment objects
        self._patients = []      # List of Patient objects



    # Setters and Getters
    def get_doctor_id(self):
        return self._doctor_id

    def get_name(self):
        return self._name

    def set_specialty(self, value):
        self._specialty = value

    def get_specialty(self):
        return self._specialty

    def set_appointments(self, value):
        self._appointments = value

    def get_appointments(self):
        return self._appointments

    def remove_appointment(self, appointment):
        self._appointments.remove(appointment)


    def add_patient(self, patient):
        # Adds a new patient to the doctor's list, if not already present
        if patient not in self._patients:
            self._patients.append(patient)

    def remove_patient(self, patient):
        # Removes a patient from the doctor's list, if present
        if patient in self._patients:
            self._patients.remove(patient)

    def schedule_appointment(self, appointment):
        # Schedules a new appointment, ensuring the patient is assigned to the doctor
        if appointment._patient not in self._patients:
            self.add_patient(appointment._patient)
        self._appointments.append(appointment)

    def get_patient_appointments(self, patient_id):
        # Returns appointments for a specific patient
        return [appointment for appointment in self._appointments if appointment._patient.get_patient_id() == patient_id]



    # Class variable for holding doctors
    doctors = {}

    # Class method to add a doctor to the doctors dictionary
    @classmethod
    def add_doctor(cls, doctor_id, name, specialty):
        if doctor_id not in cls.doctors:
            cls.doctors[doctor_id] = Doctor(doctor_id, name, specialty)
        else:
            print(f"Doctor with ID {doctor_id} already exists.")

    # Function to schedule an appointment - it will check in the doctors dictionary
    def schedule_appointment(self, new_appointment):
        # Assuming new_appointment is an Appointment object
        self._appointments.append(new_appointment)


class PatientRecordSystem:
    """Class to manage the patient records"""

    # Constructor
    def __init__(self, max_patients):
        self.max_patients = max_patients
        self.records = [None] * max_patients
        self.next_index = 0
        self.patient_index_map = {}  # This will map patient_id to index in the records list

    def sort_patient_records(self, sort_key):
        """ Sorts the patient records based on the sort_key using quicksort. """
        if self.records:
            # Ensure we're not trying to sort where records might be None
            filled_records = [record for record in self.records if record is not None]
            # Call the quicksort_records method
            Patient.quicksort_records(filled_records, 0, len(filled_records) - 1, sort_key)
            # Reassign sorted records back to self.records
            self.records = filled_records + [None] * (self.max_patients - len(filled_records))
            # Update the index map after sorting
            self.patient_index_map = {
                patient.get_patient_id(): index for index, patient in enumerate(filled_records)
            }

    def add_patient(self, patient):
        if self.next_index < self.max_patients:
            self.records[self.next_index] = patient
            self.patient_index_map[patient.get_patient_id()] = self.next_index
            self.next_index += 1
            self.sort_patient_records('Patient_id')  # Sort after adding
        else:
            print("Patient record system is full, cannot add more patients.")

    def search_patient(self, patient_id):
        index = self.patient_index_map.get(patient_id)
        if index is not None:
            return self.records[index]
        return None

    def update_patient(self, patient_id, name=None, date_of_birth=None, medical_history=None, phone=None,
                       admission_date=None):
        patient = self.search_patient(patient_id)
        if patient:
            if name:
                patient.set_name(name)
            if date_of_birth:
                patient.set_date_of_birth(date_of_birth)
            if medical_history:
                patient.set_medical_history(medical_history)
            if phone:
                patient.set_phone(phone)
            if admission_date:
                patient.set_admission_date(admission_date)
            self.sort_patient_records('Patient_id')  # Sort after update
        else:
            print(f"No record found for patient_id {patient_id}")

    def delete_patient(self, patient_id):
        index = self.patient_index_map.get(patient_id)
        if index is not None:
            # Set the record to None, indicating deletion
            self.records[index] = None

            # Remove the patient from the map
            del self.patient_index_map[patient_id]
            print(f"Patient record for patient_id {patient_id} deleted.")

        else:
            print(f"No record found for patient_id {patient_id}")

        # Re-sort the records after deletion to fill the gap and maintain order
        self.sort_patient_records('Patient_id')

    def binary_search_patient(self, patient_id):
        """
        Perform a binary search on the sorted list of patient records.
        """
        left, right = 0, self.next_index - 1  # Adjusted to next_index since records are populated sequentially

        while left <= right:
            mid = (left + right) // 2
            if self.records[mid] is None:  # Skip empty record slots
                right = mid - 1
                continue

            mid_id = self.records[mid].get_patient_id()
            if mid_id == patient_id:
                return self.records[mid]
            elif mid_id < patient_id:
                left = mid + 1
            else:
                right = mid - 1

        return None  # Patient not found

    def print_patient_summary(self, patient_id):
        """
        Search for a patient using binary search and display their details,
        including personal details, doctor, appointment, and medications.
        """
        patient = self.binary_search_patient(patient_id)
        if patient is not None:
            print(f"Patient ID: {patient.get_patient_id()}")
            print(f"Name: {patient.get_name()}")
            print(f"Date of Birth: {patient.get_date_of_birth()}")
            print(f"Medical History: {patient.get_medical_history()}")
            print(f"Phone: {patient.get_phone()}")
            print(f"Admission Date: {patient.get_admission_date()}")

            # Assuming a patient can have only one appointment and one doctor at a time
            appointment = patient.get_appointments()[0] if patient.get_appointments() else None
            if appointment:
                doctor_id = appointment.get_doctor_id()
                doctor = Doctor.doctors[doctor_id]
                print(
                    f"Appointment with Dr. {doctor.get_name()} on {appointment.get_date()} at {appointment.get_time()}. Reason: {appointment.get_reason()}")

            # Assuming the prescription stack stores all prescriptions for the patient
            if not patient.get_prescriptions().is_empty():
                current_prescription = patient.get_prescriptions().peek()
                print(
                    f"Current Prescription: {current_prescription.get_medication()} for {current_prescription.get_duration()}")
            else:
                print("No current prescriptions.")
        else:
            print("Patient not found.")


class Appointment:
    """Class that represents the appointments"""
    appointment_count = 0

    # Constructor
    def __init__(self, patient, doctor, date, time, reason):
        Appointment.appointment_count +=1
        self._appointment_id = f"HAp{Appointment.appointment_count}"  # Generate appointment ID automatically
        self._patient = patient  # Reference to Patient object
        self._doctor = doctor    # Reference to Doctor object
        self._date = date
        self._time = time
        self._reason = reason


    # Setters and Getters
    def get_appointment_id(self):
        return self._appointment_id

    def set_patient_id(self, value):
        self._patient_id = value

    def get_patient_id(self):
        return self._patient_id

    def set_doctor_id(self, value):
        self._doctor_id = value

    def get_doctor_id(self):
        return self._doctor_id

    def set_date(self, value):
        self._date = value

    def get_date(self):
        return self._date

    def set_time(self, value):
        self._time = value

    def get_time(self):
        return self._time

    def set_reason(self, value):
        self._reason = value

    def get_reason(self):
        return self._reason


class Prescription:
    """Class that represents the prescriptions"""
    prescription_count = 0

    # Constructor
    def __init__(self, patient_id, doctor_id, medication, dosage, duration):
        Prescription.prescription_count +=1
        self._prescription_id = f"HPr{Prescription.prescription_count}"  # Generate prescription ID automatically
        self._patient_id = patient_id  # ID of the patient to whom the prescription is issued
        self._doctor_id = doctor_id  # ID of the doctor who issued the prescription
        self._medication = medication  # Name of the prescription
        self._dosage = dosage  # Dosage of the medication
        self._duration = duration  # Duration for which the medication is prescribed

    # Setters and Getters
    def get_prescription_id(self):
        return self._prescription_id

    def set_patient_id(self, value):
        self._patient_id = value

    def get_patient_id(self):
        return self._patient_id

    def set_doctor_id(self, value):
        self._doctor_id = value

    def get_doctor_id(self):
        return self._doctor_id

    def set_medication(self, value):
        self._medication = value

    def get_medication(self):
        return self._medication

    def set_dosage(self, value):
        self._dosage = value

    def get_dosage(self):
        return self._dosage

    def set_duration(self, value):
        self._duration = value

    def get_duration(self):
        return self._duration


class Record:
    """Class that represents the records"""
    record_count = 0

    # Constructor
    def __init__(self, patient_id, diagnosis, treatment_plan):
        Record.record_count += 1
        self._patient_id = patient_id  # ID of the patient to whom the record belongs
        self._record_id = f"HR{Record.record_count}"  # identifier for the record
        self._diagnosis = diagnosis  # Diagnosis information
        self._treatment_plan = treatment_plan  # Proposed treatment plan

    # Setters and Getters
    def get_patient_id(self):
        return self._patient_id

    def set_record_id(self, value):
        self._record_id = value

    def get_record_id(self):
        return self._record_id

    def set_diagnosis(self, value):
        self._diagnosis = value

    def get_diagnosis(self):
        return self._diagnosis

    def set_treatment_plan(self, value):
        self._treatment_plan = value

    def get_treatment_plan(self):
        return self._treatment_plan


class Node:
    """Class that represent nodes for singly linked lists"""

    # Constructor
    def __init__(self, patient):
        self._patient = patient  # The patient object stored in this node
        self._next = None  # reference to the next node in the list, initialized as None

    # Setters and Getters
    def set_patient(self, patient):
        self._patient = patient

    def get_patient(self):
        return self._patient

    def set_next(self, next_node):
        self._next = next_node

    def get_next(self):
        return self._next


class SinglyLinkedList:
    """Singly linked list class for managing a queue of patients"""

    # Constructor
    def __init__(self):
        self._head = None  # the head of the list, starting as None
        self._tail = None  # the tail of the list, also starting as None

    # Setters and Getters
    def set_head(self, node):
        self._head = node

    def get_head(self):
        return self._head

    def set_tail(self, node):
        self._tail = node

    def get_tail(self):
        return self._tail

    # a method to add a patient to the end of the list
    def enqueue(self, patient):
        new_node = Node(patient)  # create a new node with the patient
        if not self._head:  # If the list is empty (head is None)
            self._head = self._tail = new_node  # here we are taking into account if the new node is both head and tail
        else:
            self._tail.set_next(new_node)  # Link the current tail to the new node
            self._tail = new_node  # Update the tail to be the new node

    # a method to remove and return a patient from the front of the list
    def dequeue(self):
        if self._head:  # If the list is not empty
            removed_patient = self._head.get_patient()  # storing the patient to return
            self._head = self._head.get_next()  # moving the head to the next node
            if self._head is None:  # If removing the node made the list empty
                self._tail = None  # tail to None since the list is empty
            return removed_patient  # Returning the removed patient
        return None  # here, we are taking into account If the list was empty, it will return None


class DNode:
    """Class that represents nodes for a doubly linked list"""

    # Constructor
    def __init__(self, patient):
        self.patient = patient  # the patient object stored in this node
        self._prev = None  # reference to the previous node, initialized as None
        self._next = None  # Reference to the next node, also initialized as None

    # Setters and Getters
    def set_patient(self, patient):
        self.patient = patient

    def get_patient(self):
        return self.patient

    def set_prev(self, prev_node):
        self._prev = prev_node

    def get_prev(self):
        return self._prev

    def set_next(self, next_node):
        self._next = next_node

    def get_next(self):
        return self._next


class DoublyLinkedList:
    """Doubly linked list class for more flexible patient queue management"""

    # Constructor
    def __init__(self):
        self._head = None  # the head of the list, starting as None
        self._tail = None  # the tail of the list, also starting as None

    # Setters and Getters
    def set_head(self, node):
        self._head = node

    def get_head(self):
        return self._head

    def set_tail(self, node):
        self._tail = node

    def get_tail(self):
        return self._tail

    # Method to add a patient to the end of the list
    def append(self, patient):
        new_node = DNode(patient)  # create a new doubly linked node with the patient
        if not self._tail:  # if the list is empty (tail is None)
            self._head = self._tail = new_node  # The new node is both head and tail
        else:
            self._tail.set_next(new_node)  # Link the current tail to the new node
            new_node.set_prev(self._tail)  # Link the new node back to the current tail
            self._tail = new_node  # Update the tail to be the new node

    # Method to remove and return a patient from the front of the list
    def pop(self):
        if self._head:  # If the list is not empty
            removed_patient = self._head.get_patient()  # Store the patient to return
            self._head = self._head.get_next()  # Move the head to the next node
            if self._head is None:  # If removing the node made the list empty
                self._tail = None  # Set tail to None since the list is empty
            else:
                self._head.set_prev(None)  # Clear the previous reference of the new head
            return removed_patient  # Return the removed patient
        return None  # If the list was empty, return None

class Stack:
    """Stack class for managing prescriptions in a LIFO (Last-In-First-Out)"""

    # Constructor
    def __init__(self):
        self._items = []  # internal list to store stack items, in this case, prescriptions

    # Setters and Getters
    def set_items(self, items):
        self._items = items

    def get_items(self):
        return self._items

    # Method to check if the stack is empty
    def is_empty(self):
        """Check if the stack is empty."""
        # Return True if the stack is empty (length is 0), otherwise returns False
        return len(self._items) == 0

    # Method to add a new prescription to the top of the stack
    def push(self, prescription):
        """Add a new prescription to the top of the stack."""
        # Adding the given prescription to the end of the list, which serves as the top of the stack
        self._items.append(prescription)

    # Method to remove and return the top prescription from the stack
    def pop(self):
        """Remove and return the top prescription from the stack."""
        # Checking if the stack is not empty to avoid errors
        if not self.is_empty():
            # Removing the last item from the list (top of the stack) and returns it
            return self._items.pop()
        # If the stack is empty, return None to indicate no items can be popped
        return None

    # Method to get the top prescription from the stack without removing it
    def peek(self):
        """Get the top prescription from the stack without removing it."""
        # Checking if the stack is not empty to avoid errors
        if not self.is_empty():
            # Returns the last item from the list (top of the stack) without removing it
            return self._items[-1]
        # If the stack is empty, return None to indicate there's no item to peek at
        return None


class Queue:
    """Queue class specifically designed for managing the scheduling of appointments in a FIFO manner"""

    # Constructor
    def __init__(self):
        self._appointments = []  # Internal list that acts as the queue for storing appointments

    # Setters and Getters
    def set_appointments(self, appointments):
        """Set the appointments list."""
        self._appointments = appointments

    def get_appointments(self):
        """Get the appointments list."""
        return self._appointments

    # Method to check if the queue is empty
    def is_empty(self):
        """Check if the queue is empty."""
        # Returns True if the queue is empty, indicating no appointments are queued
        # This is determined by checking if the length of the appointments list is 0
        return len(self._appointments) == 0

    # Method to add an appointment to the end (rear) of the queue
    def enqueue(self, appointment):
        """Add an appointment to the end (rear) of the queue."""
        # Appending the given appointment object to the end of the appointments list
        # This represents adding an appointment to the rear of the queue
        self._appointments.append(appointment)

    # Method to remove and return the first (front) appointment from the queue
    def dequeue(self):
        """Remove and return the first (front) appointment from the queue."""
        # Check if the queue is not empty to ensure an appointment can be dequeued
        if not self.is_empty():
            # Removing and returning the first appointment in the list
            # This represents removing the appointment from the front of the queue
            return self._appointments.pop(0)
        # If the queue is empty, return None to indicate there are no appointments to dequeue
        return None

    # Method to view the first (front) appointment in the queue without removing it
    def peek(self):
        """View the first (front) appointment in the queue without removing it."""
        # Check if the queue is not empty to ensure there is an appointment to peek at
        if not self.is_empty():
            # Return the first appointment in the list without removing it
            # This allows viewing the front appointment in the queue
            return self._appointments[0]
        # If the queue is empty, return None to indicate there's no appointment to peek at
        return None


consultation_queue = Queue()


def add_patient_to_consultation_queue(patient_id, patient_records):
    """
    This function adds a patient to the consultation queue.
    """

    # Ensure the patient exists in the patient_records before enqueuing
    if patient_id in patient_records:
        consultation_queue.enqueue(patient_records[patient_id])
        print(f"Patient {patient_id} added to the consultation queue.")
    else:
        print("Patient record not found.")

def consult_next_patient():
    """
    This function dequeues the next patient from the consultation queue for consultation.
    """
    if not consultation_queue.is_empty():
        next_patient = consultation_queue.dequeue()
        print(f"Now consulting patient {next_patient.get_patient_id()}.")
        # Here, you can call other functions to handle the consultation details
    else:
        print("No more patients in the queue.")

def patient_generator(n):
    patients = []
    for i in range(n):
        name = random.choice(list(RandomNames)).value  # Randomly select a name from the enum
        date_of_birth = f"{random.randint(1950, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}"  # Generate a random date of birth
        medical_history = random.choice(list(RandomMedicalHistory)).value  # Randomly select medical history from the enum
        phone = f"+{random.randint(1, 999)}-{random.randint(100, 999)}-{random.randint(1000000, 9999999)}"  # Generate a random phone number
        admission_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}"  # Generate a random admission date

        # Create a Patient object with the generated data
        patient = Patient(name, date_of_birth, medical_history, phone, admission_date)
        consultation_queue.enqueue(patient)  # Enqueue the patient into the consultation queue
        patients.append(patient)  # Add the patient to the list of patients

    return patients

# Initialize patient records system and consultation queue
patient_records_system = PatientRecordSystem(max_patients=100)
consultation_queue = Queue()

# Dictionary to store doctors
doctors = {}

# Dictionary to store prescriptions stack for each patient
prescriptions = defaultdict(Stack)

# Dictionary to store appointments queue for each patient
appointments = defaultdict(Queue)

# Some instances to test the code:
# Creating patient objects
patient1 = Patient("Hamad Alnuaimi", "2004-02-12", "No significant medical history", "0509997667", "2024-04-01")
patient2 = Patient("Rashed Alghafri", "1985-10-20", "Allergic to penicillin", "0509999999", "2024-04-02")

# Creating doctor objects
doctor1 = Doctor("Dr. Smith", "Cardiologist")
doctor2 = Doctor("Dr. Johnson", "Orthopedic Surgeon")

# Creating appointment objects
appointment1 = Appointment(patient1, doctor1, "2024-04-05", "10:00", "Regular checkup")
appointment2 = Appointment(patient2, doctor2, "2024-04-06", "11:00", "Knee pain evaluation")

# Creating prescription objects
prescription1 = Prescription(patient1.get_patient_id(), doctor1.get_doctor_id(), "Aspirin", "100mg", "2 weeks")
prescription2 = Prescription(patient2.get_patient_id(), doctor2.get_doctor_id(), "Ibuprofen", "200mg", "1 week")

# Creating record objects
record1 = Record(patient1.get_patient_id(), "High blood pressure", "Prescribed medication and lifestyle changes")
record2 = Record(patient2.get_patient_id(), "Knee inflammation", "Recommended rest and physical therapy")

# Some functions to test the code:
# Add patients to consultation queue
consultation_queue.enqueue(patient1)
consultation_queue.enqueue(patient2)

# Consult next patient
consult_next_patient()

# Schedule appointments for patients
doctor1.schedule_appointment(appointment1)
doctor2.schedule_appointment(appointment2)

# Add prescriptions to patients
patient1.add_prescription(prescription1)
patient2.add_prescription(prescription2)

# Add records to patients
patient1.add_record(record1)
patient2.add_record(record2)

# Print patient summary
patient1.print_patient_summary()
patient2.print_patient_summary()


choice = 'o'
# Main menu loop
while choice != '0':
    print("\nWelcome to the Hospital's System...")
    print("1.   Add a patient")
    print("2.   Generate random patients")
    print("3.   Add a doctor")
    print("4.   Create an appointment for a patient")
    print("5.   Create a prescription for a patient")
    print("6.   Record the patient's status")
    print("7.   Add a patient into the queue")
    print("8.   Add the prescription into the stack")
    print("9.   Add the patient's appointment into the queue")
    print("10.  Consult next patient")
    print("0.   Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Add a patient
        name = input("Enter patient name: ")
        date_of_birth = input("Enter patient's date of birth (YYYY-MM-DD): ")
        medical_history = input("Enter patient's medical history: ")
        phone = input("Enter patient's phone number: ")
        admission_date = input("Enter admission date (YYYY-MM-DD): ")
        patient = Patient(name, date_of_birth, medical_history, phone, admission_date)
        patient_records_system.add_patient(patient)
        print(f"A patient has been successfully created in the system, the patient id is: {patient.get_patient_id()}")


    elif choice == '2':
        num_patients = int(input("How many patients do you want to generate? "))
        patient_generator(num_patients)
        print(f"{num_patients} patients are waiting in the queue.")



    elif choice == '3':
        # Add a doctor
        name = input("Enter doctor name: ")
        specialty = input("Enter doctor's specialty: ")
        doctor = Doctor( name, specialty)
        print(f"A doctor has been successfully created in the system, the doctor id is: {doctor.get_doctor_id()}")


    elif choice == '4':
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time: ")
        reason = input("Enter appointment reason: ")
        appointment = Appointment(patient_id, doctor_id, date, time, reason)
        appointments[patient_id].enqueue(appointment)
        print(f"An appointment is successfully created with the ID: {appointment.get_appointment_id()}.")

    elif choice == '5':
        # Create a prescription for a patient
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        medication = input("Enter medication: ")
        dosage = input("Enter dosage: ")
        duration = input("Enter duration: ")
        prescription = Prescription(patient_id, doctor_id, medication, dosage, duration)
        prescriptions[patient_id].push(prescription)

    elif choice == '6':
        # Record the patient's status
        patient_id = input("Enter patient ID: ")
        diagnosis = input("Enter diagnosis: ")
        treatment_plan = input("Enter treatment plan: ")
        record = Record(patient_id, diagnosis, treatment_plan)
        patient_records_system.search_patient(patient_id).add_record(record)
        print(f"The patient status had been successfully recorded, recording ID: {record.get_record_id()}")

    elif choice == '7':
        # Add a patient into the queue
        patient_id = input("Enter patient ID: ")
        add_patient_to_consultation_queue(patient_id, patient_records_system.patient_index_map)

    elif choice == '8':
        # Add the prescription into the stack
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        medication = input("Enter medication: ")
        dosage = input("Enter dosage: ")
        duration = input("Enter duration: ")
        prescription = Prescription(patient_id, doctor_id, medication, dosage, duration)
        prescriptions[patient_id].push(prescription)

    elif choice == '9':
        # Add the patient's appointment into the queue
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time: ")
        reason = input("Enter appointment reason: ")
        appointment = Appointment(patient_id, doctor_id, date, time, reason)
        appointments[patient_id].enqueue(appointment)

    elif choice == '10':
        # Consult next patient
        consult_next_patient()

    elif choice == '0':
        # Exit the program
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")