from health_centre import HealthCentre, Doctor, Pharmacist, Cashier


def main():
    health_centre = HealthCentre()
    pharmacist = Pharmacist()
    cashier = Cashier()

    while True:
        print("""===============Welcome to the Health Centre===============
                Choose an option below
                1. See the Doctor
                2. Get Doctor's prescribed drugs from Pharmacist
                3. Buy drugs from Pharmacist
                4. Get my bill from Cashier
                5. ADMIN: Check drug store
                """)

        choice = input("Enter your option >> ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an integer! ")
            continue
        else:
            if choice == 1:
                doctor = Doctor()
                doctor.diagnose_patient()

            elif choice == 2:
                pharmacist.attend_to_patient(doctor.diagnose_patient())

            elif choice == 3:
                pharmacist.sell_drugs()

            elif choice == 4:
                cashier.bill_patient()

            elif choice == 5:
                admin_pass = input("Enter ADMIN password here >> ")
                if admin_pass == health_centre.password:
                    health_centre.check_store()
                else:
                    print("Incorrect Password")
                    continue

            else:
                print("Invalid input. Please enter a number between 1-5")


if __name__ == "__main__":
    main()






