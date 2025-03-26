import password_utils
import storage

def main():

    passwords = storage.load_passwords()

 
    while True:
        print("\nPassword Manager")
        print("1. Create a password")
        print("2. Check my password")
        print("3. Just show all saved")
        print("4. Exit")

        choice = input("Choose ure action: ").strip()
        
        if choice == "1":
            site = input("Enter a website name: ").strip()
            password = password_utils.generate_password()
            hashed_password = password_utils.hash_password(password)
            passwords[site] = hashed_password
            storage.save_passwords(passwords)
            print(f"GERETATION PASSWORD FOR: {site}: {password}")
        
        elif choice == "2":
            site = input("ENTER A WESYTE NAME: ").strip()

            if site in passwords:
                entered_password = input("ENTER  A PASSWORD: ")

                if password_utils.verify_password(entered_password, passwords[site]):
                    print("password is correct!")
                else:
                    print("WRONG PASSWORD!")
            else:
                print("HERES NO SAVED PASSWORD 4 THIS WEBSITE.")

        elif choice == "3":
            if passwords:
                print("HERES URE SAVED PASSWORD:")
                for site in passwords:
                    print(f"- {site}")
            else:
                print("HERES NO SAVED PASSWORDS.")

        elif choice == "4":
            print("Exit...")
            break

        else:
            print("wrong, Try again.")

if __name__ == "__main__":
    main()