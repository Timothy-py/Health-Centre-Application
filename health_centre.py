import re, json
#
#
# class HealthCentre:
#     """
#     this class contain the attributes and the functionality of the health centre to store drugs
#     with their corresponding quantity and prices.
#     """
#
#     password = 'timothy'
#     quantity = [1, 4, 7, 3]
#     drugAndprice = {
#         "paracetamol": 600,
#         "aspirin": 250,
#         "kekozonazo": 300,
#         "vitamin_C": 100
#     }
#
#     def __init__(self):
#         """
#         this two instance variables store the quantity do drugs in a list and
#         store the drug and price pair in a dictionary.
#         """
#         pass
#
#     def check_store(self):
#         """
#          this method access the data in the class instance variables, does the necessary filtration to separate
#          the qty, drug and price, and print them out in a user-friendly format.
#         """
#
#         self.list_drugAndprice = list(self.drugAndprice.items())
#         print('Qty\t\t\t\tDrug Name\t\t\t\tPrice(#)')
#
#         for num in self.quantity:
#             for drug in self.list_drugAndprice:
#                 if self.quantity.index(num) == self.list_drugAndprice.index(drug):
#                     print('{}\t\t\t\t{}\t\t\t\t{}'.format(num, drug[0], drug[1]))
#
#
class Doctor:
    """
    this class does two main things - i. to ask the patient for his feelings
    ii. to diagnose the patient base on those feelings.
    """

    # load the ailment_symptoms.json file as a json object
    with open("ailment_symptoms.json") as fileObj:
        data = json.load(fileObj)

    # this class variable stores symptoms and their most probable ailment in a dictionary
    doctor_brain = data["ailment_symptoms"]

    def __init__(self):
        """
        the constructor ask the patient for his feelings as a user-input and stores it in
        patient_response instance variable.
        """
        self.patient_symptoms = []
        self.process_patient_response = ()
        self.patient_possible_ailment = []
        self.patient_ailment_count = []

        print('DOCTOR >> ')
        print("""
                Hello! How are you doing today? Could you please tell me in specific words
                how you've been feeling and the symptoms you've been experiencing.
                """)

        print('YOU >> ')
        self.patient_response = input('Your response here : ')
        print('\n')

    def diagnose_patient(self):
        """
         this method contain logic to determine the most probable ailment of patient from
         the response provided.
        """

        try:
            # check for words patient_response variable which correspond to symptom in the doctor_brain variable and
            # append such word(symptom) to patient_symptoms variable. Done through the use of regular expression.
            # symptomsRegex = re.compile(r'cold|fever|cough|headache|stool|temperature|'
            #                            r'catarrh|vomiting|stomach-ache|diarrhoea', re.I)

            symptomsFileObj = open("symptomsFile.txt", "w+")
            for symptom in self.doctor_brain:
                symptomsFileObj.write(symptom + "|")
            symptomsFileObj.close()

            symptomsFileObj = open("symptomsFile.txt", 'r')
            symptoms_string = symptomsFileObj.read()
            # symptoms_strings = print(f'r"{symptoms_string}"')
            # print(symptoms_strings)
            symptomsRegex = re.compile(f'r"{symptoms_string}"', re.I)

            self.patient_symptoms = symptomsRegex.findall(self.patient_response)

            # Store the values(ailments) of keys(symptoms) in the doctor_brain to
            # patient_possible_ailment variable. Done through the use of list comprehension
            self.patient_possible_ailment = [self.doctor_brain[symptom] for symptom in self.patient_symptoms]

            # This code suit does two things simultaneously:
            # At first it is a filtered list of patient_possible_ailment list to make sure an ailment appears just once.
            # It then count the original appearance of each ailment in the patient_possible_ailment list
            # and append the number of appearance of each ailment to patient_ailment_count list.
            self.patient_ailment_count = [self.patient_possible_ailment.count(ailment)
                                          for ailment in self.patient_possible_ailment
                                          if ailment not in self.patient_ailment_count]

            # This code suit determines the most probable ailment of the patient by checking
            # for the max value in patient_ailment_count list, determining the index of such value,
            # and then, list indexing the index returned from patient_ailment_count list into
            # patient_possible_ailment to determine the actual patient ailment.
            self.patient_ailment = self.patient_possible_ailment[
                self.patient_ailment_count.index
                (max(self.patient_ailment_count))]

        except ValueError:
            print('DOCTOR >> ')
            print("Sorry! I can't get any symptom from your response. Be detailed!")

        else:
            print('DOCTOR >> ')
            print("""Oh Sorry! You\'re probably suffering from {} infection.
            Go to the pharmacist go get some drugs.
            Make sure you use up the drugs that will be prescribed and use them accordingly.""".format(
                self.patient_ailment))
            return self.patient_ailment

        finally:
            print('Take care.')
#
#
# class Pharmacist(Doctor):
#     """
#     this class provide functionality of the pharmacist to prescribe drugs to patients.
#     """
#
#     # this class variable is a dictionary of ailments and drugs that can be used to cure them.
#     pharmacist_brain = {
#         'malaria': {'paracetamol': 1, 'vitamin_C': 4},
#         'diarrhoea': {'salt': 4, 'aspirin': 5},
#         'pimples': {'Funbact A': 1, 'kekozonazo': 1},
#         }
#
#     patient_qty = []
#     patient_drug = []
#
#     def __init__(self):
#         pass
#
#     def attend_to_patient(self, patient_ailment):
#         """
#         this method accept the diagnoses of doctor(i.e return value of diagnose_patient method), check for
#         the drugs to be used in the pharmacist_brain and print them out for the user.
#         this method also save the drugs and the quantity in the class instance variables to make
#         it available for the cashier for billing.
#         """
#
#         print('PHARMACIST >> ')
#         self.patient_ailment = patient_ailment
#         for drug in self.pharmacist_brain[self.patient_ailment]:
#             self.patient_qty.append(self.pharmacist_brain[self.patient_ailment][drug])
#             self.patient_drug.append(drug)
#             print('Take {} of {}'.format(self.pharmacist_brain[self.patient_ailment][drug], drug))
#
#         print('\nKindly go to the Cashier to get your bills')
#
#     def sell_drugs(self):
#         """
#         this method allow the pharmacist to sell drugs to patients who just want to buy drugs by
#         inputing the qty and name of drugs they wanna purchase.
#         this method also save the drugs and the quantity in the class instance variables to make
#         it available for the cashier for billing.
#         """
#
#         print('PHARMACIST >> ')
#         print("""Hi, You're welcome.
#         Kindly provide ONLY the name and the quantity(in figure pls) of drugs you wanna purchase""")
#
#         self.patient_response = input('Your response here : ')
#
#         self.drug_listRegex = re.compile(r'[0-9]|paracetamol|aspirin|salt|vitamin_C|'
#                                          r'kekozonazo|funbact A', re.I)
#
#         self.match_obj = self.drug_listRegex.findall(self.patient_response)
#
#         for string in self.match_obj:
#                 if string.isdigit():
#                     self.patient_qty.append(string)
#                 else:
#                     self.patient_drug.append(string.lower())
#
#         print("""\n=================DRUG LIST=================
#         Drug\t\t\t\tQty""")
#
#         for drug in self.patient_drug:
#             for qty in self.patient_qty:
#                 if self.patient_drug.index(drug) == self.patient_qty.index(qty):
#                     print('{}\t\t\t{}\t\t\t\t\t'.format(drug, qty))
#         print('\n======================================')
#
#         print('\nKindly go to the Cashier to get your bills')
#
#
# class Cashier(HealthCentre, Pharmacist):
#     """
#     this class provides the functionality of the cashier to bill drugs prescribed by the pharmacist.
#     """
#
#     price = []
#
#     def __init__(self):
#         HealthCentre.__init__(self)
#         Pharmacist.__init__(self)
#
#     def bill_patient(self):
#         """
#         this method access the instance variables (i.e qty and drug) in the pharmacist class and check
#         for the prices of the drugs in the healthcentre class and then bill the patient.
#         """
#
#         print('CASHIER >> ')
#         print("""=================BILL=================
#         Drug\t\t\tQty\t\t\tPrice""")
#         for drug in Pharmacist.patient_drug:
#             for qty in Pharmacist.patient_qty:
#                 if Pharmacist.patient_drug.index(drug) == Pharmacist.patient_qty.index(qty):
#                     self.price.append(HealthCentre.drugAndprice[drug] * int(qty))
#                     print('{}\t\t\t{}\t\t\t{}\t\t\t\t'.format(drug, qty, HealthCentre.drugAndprice[drug]))
#         print('=====================================')
#         print('TOTAL => #{}'.format(sum(self.price)))
#
if __name__ == "__main__":
    Doctor().diagnose_patient()