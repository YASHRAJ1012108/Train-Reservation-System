from abc import ABC, abstractmethod
import mysql.connector
from tabulate import tabulate
import random
from datetime import datetime
import re

# ----------- Abstract Base Classes -----------
class AbstractDatabase(ABC):
    @staticmethod
    @abstractmethod
    def create_database():
        pass

    @staticmethod
    @abstractmethod
    def create_tables():
        pass

class AbstractAccount(ABC):
    @staticmethod
    @abstractmethod
    def login():
        pass

class AbstractReservation(ABC):
    @abstractmethod
    def displayMenu(self):
        pass

    @abstractmethod
    def Main(self):
        pass

# ----------- Database Setup Class -----------
class DatabaseSetup(AbstractDatabase):
    @staticmethod
    def create_database():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database='train')
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS train")
        except Exception as e:
            print("Error creating database:", e)

    @staticmethod
    def create_tables():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("""CREATE TABLE IF NOT EXISTS accounts(
                Mobile VARCHAR(15),
                Email VARCHAR(100),
                Username VARCHAR(20),
                Password VARCHAR(20),
                Name VARCHAR(50),
                DOB VARCHAR(20),
                Gender VARCHAR(20),
                Nationality VARCHAR(50),
                Address VARCHAR(100),
                PIN VARCHAR(10)
            )""")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS trains(
                No VARCHAR(10),
                Name VARCHAR(100),
                Source VARCHAR(50),
                Destination VARCHAR(50),
                2S VARCHAR(10),
                SL VARCHAR(10),
                AC VARCHAR(10),
                Deparature VARCHAR(20),
                Arrival VARCHAR(20)
            )""")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS tickets(
                Name VARCHAR(100),
                Age VARCHAR(10),
                Gender VARCHAR(50),
                Nationality VARCHAR(50),
                Fare VARCHAR(20),
                TransId VARCHAR(50),
                PNR VARCHAR(50),
                Train VARCHAR(100),
                No VARCHAR(10),
                Date VARCHAR(20),
                Deparature VARCHAR(20),
                Arrival VARCHAR(20),
                Source VARCHAR(50),
                Destination VARCHAR(50),
                Passengers VARCHAR(10),
                Class VARCHAR(10),
                Berth VARCHAR(10),
                Mode VARCHAR(50),
                TransDate VARCHAR(100),
                TransTime VARCHAR(100)
            )""")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS cancels(
                Train VARCHAR(100),
                No VARCHAR(10),
                TransId VARCHAR(50),
                TransDate VARCHAR(100),
                Source VARCHAR(50),
                Destination VARCHAR(50),
                CancelDate VARCHAR(100),
                PNR VARCHAR(50),
                CancelId VARCHAR(50),
                Refund VARCHAR(20),
                Deducted VARCHAR(20)
            )""")
        except Exception as e:
            print("Error creating tables:", e)

# ----------- User Functions Class -----------
class User(AbstractAccount):
    @staticmethod
    def newUser():
        try:
            print("\n" + "*" * 17)
            print("USER REGISTRATION")
            print("*" * 17)

            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()

            # Mobile number validation (keep asking until valid)
            while True:
                mobile = input("\nMOBILE NUMBER (10 digits): ")
                if not mobile.isdigit() or len(mobile) != 10:
                    print("\nInvalid mobile number. Please enter exactly 10 digits.")
                else:
                    break

            # Email validation (keep asking until valid)
            while True:
                email = input("\nE-MAIL: ")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    print("\nInvalid email format:@gmail.com like this. Please try again.")
                else:
                    break

            # Check if username already exists
            while True:
                username = input("\nCREATE USERNAME: ").strip()
                mycursor.execute("SELECT Username FROM accounts")
                existing_usernames = [u[0] for u in mycursor.fetchall()]
                if not username:
                    print("\nUsername cannot be empty Please enter a valid username.")
                    continue 
                # as input again
                if username in existing_usernames:
                    print("\nUsername is already taken. Please choose a different one.")
                else:
                    break

            # Password validation (keep asking until valid)
            while True:
                password = input("\nCREATE PASSWORD: ")
                confirm_password = input("\nCONFIRM PASSWORD: ")
                if password != confirm_password:
                    print("\nPasswords do not match. Please try again.")
                elif len(password) < 6:
                    print("\nPassword must be at least 6 characters long.")
                else:
                    break

            # Name validation (keep asking until valid)
            while True:
                name = input("\nNAME: ")
                if not name.strip():
                    print("\nName cannot be empty.")
                else:
                    break

            # DOB validation (keep asking until valid)
            while True:
                print("\nD.O.B. (DD/MM/YYYY):")
                day = input("DD: ")
                month = input("MM: ")
                year = input("YYYY: ")
                if not (day.isdigit() and month.isdigit() and year.isdigit()) or len(day) != 2 or len(month) != 2 or len(year) != 4:
                    print("\nInvalid date format. Please enter the date in DD/MM/YYYY format.")
                else:
                    dob = f"{day}/{month}/{year}"
                    break

            # Gender validation (keep asking until valid)
            while True:
                gender = input("\nGENDER (M for Male/F for Female/T for Transgender): ").upper()
                if gender not in ['M', 'F', 'T']:
                    print("\nInvalid gender. Please enter M, F, or T.")
                else:
                    gender_map = {'M': 'MALE', 'F': 'FEMALE', 'T': 'TRANS'}
                    gender = gender_map[gender]
                    break

            # Nationality validation (keep asking until valid)
            while True:
                nationality = input("\nNATIONALITY: ")
                if not nationality.strip():
                    print("\nNationality cannot be empty.")
                else:
                    break

            # Address validation (keep asking until valid)
            while True:
                address = input("\nRESIDENCE ADDRESS: ")
                if not address.strip():
                    print("\nAddress cannot be empty.")
                else:
                    break

            # PIN validation (keep asking until valid)
            while True:
                print("\n" + "*" * 12)
                print("GENERATE PIN")
                print("*" * 12)

                pin = input("\nCREATE 4-DIGIT PIN: ")

                if not pin.isdigit() or len(pin) != 4:
                    print("\nPIN must be exactly 4 digits.")
                    continue  # Ask for input again

                # Check if PIN already exists
                mycursor.execute("SELECT PIN FROM accounts")
                existing_pins = [p[0] for p in mycursor.fetchall()]

                if pin in existing_pins:
                    print("\nThis PIN is already used by another user. Please enter a unique PIN.")
                    continue  # Ask for a new PIN

                confirm_pin = input("\nCONFIRM PIN: ")

                if pin != confirm_pin:
                    print("\nPIN does not match. Please try again.")
                else:
                    break  # Exit loop if PIN is unique and confirmed

            # Insert the new user into the database
            sql = """INSERT INTO accounts(Mobile, Email, Username, Password, Name, DOB, Gender, Nationality, Address, PIN) 
                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (mobile, email, username, password, name, dob, gender, nationality, address, pin)
            mycursor.execute(sql, values)
            mydb.commit()

            print("\nACCOUNT CREATED SUCCESSFULLY\n")
            User.oldUser()

        except Exception as e:
            print(f"Error in newUser: {e}")
            System.displayMenu()

    @staticmethod
    def oldUser():
        try:
            print("\n" + "*" * 7)
            print("SIGN IN")
            print("*" * 7)
            print("\nLOGIN VIA\n1. USERNAME\n2. 4-DIGIT PIN")
            s = int(input("\nSELECT OPTION: "))
            if s == 1:
                User.username()
            elif s == 2:
                User.pin()
            else:
                print("\nINCORRECT OPTION\n")
                User.oldUser()
        except Exception as e:
            print("Error in oldUser:", e)
            System.displayMenu()

    @staticmethod
    def username():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Username, Password, Name FROM accounts")
            accounts = mycursor.fetchall()
            login = input("\nUSERNAME: ")
            passwd = input("\nPASSWORD: ")
            for acc in accounts:
                if acc[0] == login and acc[1] == passwd:
                    captcha_str = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&+") for _ in range(6))
                    print('\n', captcha_str)
                    captcha = input("Enter Captcha: ")
                    if captcha == captcha_str:
                        print("\nWELCOME", acc[2])
                        System.Main()
                        return
                    else:
                        print("\nWrong Captcha\n")
                        User.oldUser()
                        return
            print("\nUser doesn't exist or Wrong password\n")
            User.oldUser()
        except Exception as e:
            print("Error in username:", e)
            System.displayMenu()

    @staticmethod
    def pin():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT PIN, Name FROM accounts")
            accounts = mycursor.fetchall()
            pin_val = input("\nEnter PIN: ")
            captcha_str = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&+") for _ in range(6))
            print('\n', captcha_str)
            captcha = input("Enter Captcha: ")
            for acc in accounts:
                if acc[0] == pin_val and captcha == captcha_str:
                    print("\nWELCOME", acc[1])
                    System.Main()
                    return
            print("\nIncorrect PIN or Captcha\n")
            User.oldUser()
        except Exception as e:
            print("Error in pin:", e)
            System.displayMenu()

    @staticmethod
    def login():
        User.oldUser()

# ----------- Admin Functions Class -----------
import re
import mysql.connector
from tabulate import tabulate

class Admin(AbstractAccount):
    @staticmethod
    def admin_login():
        try:
            print("\n" + "*" * 9)
            print("ADMIN LOGIN")
            print("*" * 9)
            username_input = input("\nADMIN USERNAME: ").strip()
            password_input = input("ADMIN PASSWORD: ").strip()
            if username_input == "admin" and password_input == "adminpass":
                print("\nADMIN LOGIN SUCCESSFUL")
                Admin.admin_menu()
            else:
                print("\nINVALID ADMIN CREDENTIALS\n")
                System.displayMenu()
        except Exception as e:
            print("Error in admin_login:", e)
            System.displayMenu()

    @staticmethod
    def admin_menu():
        try:
            print("\n" + "*" * 28)
            print("ADMIN CONTROL PANEL")
            print("*" * 28)
            print("\n1. ADD TRAIN DETAILS\n2. DELETE TRAIN DETAILS\n3. UPDATE TRAIN DETAILS\n4. SHOW REVENUE OF TRAINS\n5. LOG OUT")
            choice = int(input("\nSELECT OPTION: "))
            if choice == 1:
                Admin.admin_add_train()
            elif choice == 2:
                Admin.admin_delete_train()
            elif choice == 3:
                Admin.admin_update_train()
            elif choice == 4:
                Admin.admin_show_revenue()
            elif choice == 5:
                System.displayMenu()
            else:
                print("\nINVALID SELECTION\n")
                Admin.admin_menu()
        except Exception as e:
            print("Error in admin_menu:", e)
            Admin.admin_menu()

    @staticmethod
    def admin_add_train():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            print("\n** ADD TRAIN DETAILS **")

            while True:
                no = input("Train No: ").strip()
                if not no.isdigit() or len(no) != 5:
                    print("Train number must be exactly 5 digits.")
                else:
                    break

            while True:
                name = input("Train Name: ").strip()
                if not name:
                    print("Train Name cannot be empty.")
                else:
                    break

            while True:
                source = input("Source: ").strip()
                if not source:
                    print("Source cannot be empty.")
                else:
                    break

            while True:
                destination = input("Destination: ").strip()
                if not destination:
                    print("Destination cannot be empty.")
                else:
                    break

            while True:
                fare_2s = input("Fare for 2S: ").strip()
                if not fare_2s.isdigit():
                    print("Fare must be a number.")
                else:
                    break

            while True:
                fare_sl = input("Fare for SL: ").strip()
                if not fare_sl.isdigit():
                    print("Fare must be a number.")
                else:
                    break

            while True:
                fare_ac = input("Fare for AC: ").strip()
                if not fare_ac.isdigit():
                    print("Fare must be a number.")
                else:
                    break

            while True:
                departure = input("Departure Time (HH:MM): ").strip()
                if not Admin.validate_time_format(departure):
                    print("Invalid time format. Please enter in HH:MM.")
                else:
                    break

            while True:
                arrival = input("Arrival Time (HH:MM): ").strip()
                if not Admin.validate_time_format(arrival):
                    print("Invalid time format. Please enter in HH:MM.")
                else:
                    break

            sql = """INSERT INTO trains(No, Name, Source, Destination, 2S, SL, AC, Deparature, Arrival)
                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (no, name, source, destination, fare_2s, fare_sl, fare_ac, departure, arrival)
            mycursor.execute(sql, val)
            mydb.commit()

            print("\nTRAIN ADDED SUCCESSFULLY")
            Admin.admin_menu()
        except Exception as e:
            print("Error in admin_add_train:", e)
            Admin.admin_menu()

    @staticmethod
    def validate_time_format(time_str):
        try:
            if ":" not in time_str:
                return False
            hours, minutes = map(int, time_str.split(":"))
            return 0 <= hours < 24 and 0 <= minutes < 60
        except ValueError:
            return False


    @staticmethod
    def admin_delete_train():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            print("\n** DELETE TRAIN DETAILS **")
            no = input("Enter Train No to delete: ").strip()
            if not no.isdigit() or len(no) != 5:
                print("Train number must be exactly 5 digits.")
                Admin.admin_menu()
                return
            mycursor.execute("SELECT No FROM trains WHERE No=%s", (no,))
            result = mycursor.fetchone()
            if not result:
                print("Your train number is not available in the database.")
            else:
                mycursor.execute("DELETE FROM trains WHERE No=%s", (no,))
                mydb.commit()
                print("\nTRAIN DELETED SUCCESSFULLY")
            Admin.admin_menu()
        except Exception as e:
            print("Error in admin_delete_train:", e)
            Admin.admin_menu()

    @staticmethod
    def admin_update_train():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            print("\n** UPDATE TRAIN DETAILS **")
            no = input("Enter Train No to update: ").strip()
            if not no.isdigit() or len(no) != 5:
                print("Train number must be exactly 5 digits.")
                Admin.admin_menu()
                return

            mycursor.execute("SELECT * FROM trains WHERE No=%s", (no,))
            result = mycursor.fetchone()
            if not result:
                print("Your train number is not available in the database.")
                Admin.admin_menu()
                return

            print("Enter new details (leave blank to keep current value):")

            def validate_time(time_input):
                if time_input:
                    parts = time_input.split(":")
                    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                        hours, minutes = int(parts[0]), int(parts[1])
                        if 0 <= hours < 24 and 0 <= minutes < 60:
                            return time_input
                    print("Invalid time format. Use HH:MM (24-hour format).")
                    return None
                return None

            name = input("Train Name: ").strip()
            source = input("Source: ").strip()
            destination = input("Destination: ").strip()

            fare_2s = input("Fare for 2S: ").strip()
            if fare_2s and not fare_2s.isdigit():
                print("Fare for 2S must be a valid number.")
                Admin.admin_menu()
                return

            fare_sl = input("Fare for SL: ").strip()
            if fare_sl and not fare_sl.isdigit():
                print("Fare for SL must be a valid number.")
                Admin.admin_menu()
                return

            fare_ac = input("Fare for AC: ").strip()
            if fare_ac and not fare_ac.isdigit():
                print("Fare for AC must be a valid number.")
                Admin.admin_menu()
                return

            deparature = input("Deparature Time (HH:MM): ").strip()
            if deparature:
                deparature = validate_time(deparature)
                if not deparature:
                    Admin.admin_menu()
                    return

            arrival = input("Arrival Time (HH:MM): ").strip()
            if arrival:
                arrival = validate_time(arrival)
                if not arrival:
                    Admin.admin_menu()
                    return

            updates = []
            values = []

            if name:
                updates.append("Name=%s")
                values.append(name)
            if source:
                updates.append("Source=%s")
                values.append(source)
            if destination:
                updates.append("Destination=%s")
                values.append(destination)
            if fare_2s:
                updates.append("2S=%s")
                values.append(fare_2s)
            if fare_sl:
                updates.append("SL=%s")
                values.append(fare_sl)
            if fare_ac:
                updates.append("AC=%s")
                values.append(fare_ac)
            if deparature:
                updates.append("Deparature=%s")
                values.append(deparature)
            if arrival:
                updates.append("Arrival=%s")
                values.append(arrival)

            if updates:
                sql = f"UPDATE trains SET {', '.join(updates)} WHERE No=%s"
                values.append(no)
                mycursor.execute(sql, values)
                mydb.commit()
                print("\nTRAIN DETAILS UPDATED SUCCESSFULLY")
            else:
                print("No changes made.")

            Admin.admin_menu()
        except Exception as e:
            print("Error in admin_update_train:", e)
            Admin.admin_menu()




    @staticmethod
    def admin_show_revenue():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            sql = "SELECT No, Train, SUM(CAST(Fare AS DECIMAL(10,2))) AS Revenue FROM tickets GROUP BY No, Train"
            mycursor.execute(sql)
            results = mycursor.fetchall()
            if results:
                print("\n** TRAIN REVENUE DETAILS **")
                print(tabulate(results, headers=['Train No', 'Train Name', 'Revenue'], tablefmt='psql'))
            else:
                print("No revenue data available.")
            Admin.admin_menu()
        except Exception as e:
            print("Error in admin_show_revenue:", e)
            Admin.admin_menu()

    @staticmethod
    def login():
        Admin.admin_login()
    


# ----------- System (Main Menu & Booking) Class -----------
class System(AbstractReservation):
    @staticmethod
    def displayMenu():
        try:
            print("\n" + "*" * 13)
            print("SYSTEM LOGIN")
            print("*" * 13)
            print("\n1. REGISTER USER\n2. SIGN IN\n3. ADMIN LOGIN\n4. EXIT")
            st = int(input("\nSELECT: "))
            if st == 1:
                User.newUser()
            elif st == 2:
                User.oldUser()
            elif st == 3:
                Admin.admin_login()
            elif st == 4:
                print("\n*** THANK YOU FOR VISITING OUR TRAIN RESERVATION SYSTEM! ***")
                exit() 
            else:
                print("\nINVALID SELECTION\n")
                System.displayMenu()
        except Exception as e:
            print("Error in displayMenu:", e)
            System.displayMenu()

    @staticmethod
    def Main():
        try:
            print("\n" + "*" * 28)
            print("TRAIN TICKET BOOKING SYSTEM")
            print("*" * 28)
            print("\n1. BOOK TICKET\n2. MY BOOKINGS\n3. PNR ENQUIRY\n4. LAST TRANSACTIONS\n5. CANCEL TICKET\n6. REFUND HISTORY\n7. TRAIN SCHEDULE\n8. LOG OUT")
            s = int(input("\nSELECT OPTION: "))
            if s == 1:
                System.book_ticket()
            elif s == 2:
                System.my_bookings()
            elif s == 3:
                System.pnr_enquiry()
            elif s == 4:
                System.last_transactions()
            elif s == 5:
                System.cancel_ticket()
            elif s == 6:
                System.refund_history()
            elif s == 7:
                System.train_schedule()
            elif s == 8:
                System.log_out()
            else:
                print("\nINCORRECT OPTION\n")
                System.Main()
        except Exception as e:
            print("Error in Main:", e)
            System.Main()

    @staticmethod
    def book_ticket():
        try:
            print("\n" + "*" * 11)
            print("BOOK TICKET")
            print("*" * 11)
    
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
    
            # FROM
            while True:
                fr = input("\nFROM: ").strip()
                if fr:
                    break
                print("FROM field cannot be empty.")
    
            # TO
            while True:
                to = input("\nTO: ").strip()
                if to:
                    break
                print("TO field cannot be empty.")
    
    # DATE OF JOURNEY
            print("\nEnter Date of jorney according to you:")
            while True:
                date_input = input("DD/MM/YYYY: ").strip()
                try:
                    journey_date = datetime.strptime(date_input, "%d/%m/%Y")
                    dt = journey_date.strftime("%d %b, %Y")
                    break
                except ValueError:
                    print("Invalid date format. Please enter in DD/MM/YYYY format.")
    
            tup = (fr, to)
            sql = "SELECT * FROM trains WHERE Source=%s and Destination=%s"
            mycursor.execute(sql, tup)
            myresult = mycursor.fetchall()
    
            if not myresult:
                print("No trains found for the given route.")
                return System.Main()
    
            print(tabulate(myresult, headers=['Train No.', 'Train Name', 'From', 'To', '2S', 'SL', 'AC', 'Departure', 'Arrival'], tablefmt='psql'))
    
            # TRAIN NUMBER
            while True:
                trno = input("\nENTER TRAIN NO: ").strip()
                if trno.isdigit() and len(trno) == 5:
                    break
                print("Train number must be exactly 5 digits.")
    
            mycursor.execute("SELECT Name FROM trains WHERE No=%s", (trno,))
            tr = mycursor.fetchall()
            if not tr:
                print("Train not found.")
                return System.Main()
            train_name = tr[0][0]
            print("\nTRAIN NAME:", train_name)
    
            # NAME
            while True:
                nam = input("\nNAME: ").strip()
                if nam:
                    break
                print("Name cannot be empty.")
    
            # AGE
            while True:
                age = input("\nAGE: ").strip()
                if age.isdigit():
                    break
                print("Invalid Age. Please enter a valid number.")
    
            # GENDER
            print("\nGENDER: M for MALE | F for FEMALE | T for TRANSGENDER")
            while True:
                gender = input("\nGENDER: ").upper().strip()
                if gender in ['M', 'F', 'T']:
                    break
                print("Invalid Gender. Enter M, F, or T.")
            gen_dict = {'M': 'MALE', 'F': 'FEMALE', 'T': 'TRANS'}
            v = gen_dict[gender]
    
            # NATIONALITY
            while True:
                nat = input("\nNATIONALITY: ").strip()
                if nat:
                    break
                print("Nationality cannot be empty.")
    
            # BERTH
            print("\nBERTH PREFERENCE: LB for LOWER | MB for MIDDLE | UB for UPPER | SL for SIDE LOWER | SU for SIDE UPPER")
            while True:
                ber = input("\nSELECT: ").strip().upper()
                if ber in ['LB', 'MB', 'UB', 'SL', 'SU']:
                    break
                print("Invalid Berth Preference.")
    
            # CLASS
            print("\nCLASS: 1 for 2S | 2 for SL | 3 for AC")
            while True:
                try:
                    cl_choice = int(input("\nSELECT: ").strip())
                    if cl_choice in [1, 2, 3]:
                        break
                    else:
                        print("Invalid Class Selection.")
                except ValueError:
                    print("Invalid input. Please enter a number (1, 2, or 3).")
    
            # NUMBER OF TICKETS
            while True:
                try:
                    tc = int(input("\nNO. OF TICKETS: ").strip())
                    if tc > 0:
                        break
                    else:
                        print("Number of tickets must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    
            # FETCH CLASS FARE
            if cl_choice == 1:
                mycursor.execute("SELECT 2S FROM trains WHERE No=%s", (trno,))
                am = int(mycursor.fetchone()[0]) * tc
                cl = "2S"
            elif cl_choice == 2:
                mycursor.execute("SELECT SL FROM trains WHERE No=%s", (trno,))
                am = int(mycursor.fetchone()[0]) * tc
                cl = "SL"
            elif cl_choice == 3:
                mycursor.execute("SELECT AC FROM trains WHERE No=%s", (trno,))
                am = int(mycursor.fetchone()[0]) * tc
                cl = "AC"
    
            # MEAL OPTION
            fd = input("\nDo you want meal (₹ 500 each)? (yes/no): ").strip().lower()
            base_fare = am + (500 * tc if fd == 'yes' else 0)
            total_fare = base_fare + 11.80  # Convenience fee
    
            print("\nPAYMENT DETAILS")
            print("BASE FARE: ₹", base_fare)
            print("CONVENIENCE FEE: ₹ 11.80")
            print("TOTAL FARE: ₹", total_fare)
    
            # PAYMENT MODE
            print("\nPAYMENT MODE:\n1. CARDS/NET BANKING\n2. BHIM/UPI")
            while True:
                ch = input("\nSELECT: ").strip()
                if ch in ['1', '2']:
                    break
                print("Invalid payment mode. Choose 1 or 2.")
            mode_dict = {'1': 'CARDS/NET BANKING', '2': 'BHIM/UPI'}
            payment_mode = mode_dict[ch]
    
            # CAPTCHA
            captcha_str = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&+") for _ in range(6))
            print('\n', captcha_str)
            captcha = input("Enter Captcha: ").strip()
            if captcha != captcha_str:
                print("\nWrong Captcha")
                return System.Main()
    
            # TRANSACTION & TICKET DETAILS
            ti = str(random.randint(1000000000, 9999999999)) + str(random.randint(10000, 99999))
            pnr = random.randint(1000000000, 9999999999)
            now = datetime.today()
            dt_now = now.strftime("%d %b, %Y")
            tm = now.strftime("%H:%M")
    
            mycursor.execute("SELECT Deparature, Arrival, Source, Destination FROM trains WHERE No=%s", (trno,))
            lt = mycursor.fetchone()
    
            sql_insert = """INSERT INTO tickets(Name, Age, Gender, Nationality, Fare, TransId, PNR, Train, No, Date, Deparature, Arrival,
                             Source, Destination, Passengers, Class, Berth, Mode, TransDate, TransTime)
                             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (nam, age, v, nat, total_fare, ti, pnr, train_name, trno, dt, lt[0], lt[1], lt[2], lt[3], tc, cl, ber, payment_mode, dt_now, tm)
    
            mycursor.execute(sql_insert, val)
            mydb.commit()
    
            print("\nTICKET BOOKED SUCCESSFULLY!")
            System.Main()
    
        except Exception as e:
            print("Error in book_ticket:", e)
            System.Main()
    

    @staticmethod
    def my_bookings():
        try:
            print("\n" + "*" * 11)
            print("MY BOOKINGS")
            print("*" * 11)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            sql = "SELECT No, Train, Source, Destination, Passengers, Date, Deparature, Arrival, PNR FROM tickets"
            mycursor.execute(sql)
            bookings = mycursor.fetchall()
            if not bookings:
                print("\nNO BOOKINGS")
            else:
                print(tabulate(bookings, headers=['Train No.', 'Train Name', 'From', 'To', 'Passengers', 'Date', 'Deparature', 'Arrival', 'PNR'], tablefmt='psql'))
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont == "yes":
                System.Main()
            else:
                System.log_out()
        except Exception as e:
            print("Error in my_bookings:", e)
            System.Main()

    @staticmethod
    def pnr_enquiry():
        try:
            print("\n" + "*" * 11)
            print("PNR ENQUIRY")
            print("*" * 11)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            pnr = input("\nSEARCH PNR: ").strip()
            mycursor.execute("SELECT No, Train, PNR, Date, Source, Destination, Passengers, Class, Fare, Berth FROM tickets WHERE PNR=%s", (pnr,))
            rs = mycursor.fetchone()
            if not rs:
                print("PNR not found")
                return System.Main()
            print(rs[1], '(', rs[0], ')', "PNR:", rs[2])
            print("Date:", rs[3])
            print("Source:", rs[4], "Destination:", rs[5])
            print(rs[6], "Adult 0 Child|", rs[7], "|GENERAL|", rs[4], "|", rs[3])
            print("BOOKING STATUS: CONFIRMED")
            print("TICKET FARE: ₹", rs[8])
            print("Charting Status: Chart Prepared")
            print("Coach: B3    Berth: 7    Berth Type:", rs[9], "\n")
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont == "yes":
                System.Main()
            else:
                System.log_out()
        except Exception as e:
            print("Error in pnr_enquiry:", e)
            System.Main()

    @staticmethod
    def last_transactions():
        try:
            print("\n" + "*" * 16)
            print("LAST TRANSACTION")
            print("*" * 16)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Train, No, TransId, TransDate, Source, Destination, Date, Fare FROM tickets")
            rs = mycursor.fetchall()
            if not rs:
                print("\nNO BOOKINGS")
                cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
                if cont == "yes":
                    System.Main()
                else:
                    System.log_out()
            else:
                lt = rs[-1]
                print(lt[0], "Transaction Id:", lt[2])
                print('(', lt[1], ')', "Transaction Date:", lt[3])
                print(lt[4], "→", lt[5])
                print(lt[6], "STATUS: BOOKED")
                print("Payment Status:")
                print("Amount deducted: ₹", lt[7])
                print("Bank Name: Credit & Debit cards/UPI(Powered by RazorPay)")
                cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
                if cont == "yes":
                    System.Main()
                else:
                    System.log_out()
        except Exception as e:
            print("Error in last_transactions:", e)
            System.Main()

    @staticmethod
    def cancel_ticket():
        try:
            print("\n" + "*" * 13)
            print("CANCEL TICKET")
            print("*" * 13)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT No, Train, Source, Destination, Name, Fare, Date, Deparature, Arrival, PNR FROM tickets")
            bookings = mycursor.fetchall()
            if not bookings:
                print("\nNO BOOKINGS")
                cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
                if cont == "yes":
                    System.Main()
                else:
                    System.log_out()
            else:
                print(tabulate(bookings, headers=['Train No.', 'Train Name', 'From', 'To', 'Name', 'Fare', 'Date', 'Deparature', 'Arrival', 'PNR'], tablefmt='psql'))
                pnr = input("\nSEARCH PNR: ").strip()
                mycursor.execute("SELECT No, Train, PNR, Date, Source, Destination, Passengers, Class, Fare, Berth, TransId, TransDate FROM tickets WHERE PNR=%s", (pnr,))
                rs = mycursor.fetchone()
                if not rs:
                    print("PNR not found")
                    return System.Main()
                print(rs[1], '(', rs[0], ')', "PNR:", rs[2])
                print("Date:", rs[3])
                print("Source:", rs[4], "Destination:", rs[5])
                print(rs[6], "Adult 0 Child|", rs[7], "|GENERAL|", rs[4], "|", rs[3])
                print("BOOKING STATUS: CONFIRMED")
                print("TICKET FARE: ₹", rs[8])
                print("Charting Status: Chart Prepared")
                print("Coach: B3    Berth: 7    Berth Type:", rs[9], "\n")
                c = input("CANCEL? (yes/no): ").strip().lower()
                if c == "yes":
                    print("Cancelling Ticket.....")
                    deducted = (2 * float(rs[8])) // 100
                    refund = float(rs[8]) - deducted
                    print("Refund Amount: ₹", refund)
                    ci = str(random.randint(1000000000, 9999999999)) + str(random.randint(10000, 99999))
                    now = datetime.today()
                    dt_now = now.strftime("%d %b, %Y")
                    sql_cancel = """INSERT INTO cancels(Train, No, TransId, TransDate, Source, Destination, CancelDate, PNR, CancelId, Refund, Deducted)
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    val = (rs[1], rs[0], rs[10], rs[11], rs[4], rs[5], dt_now, rs[2], ci, refund, deducted)
                    mycursor.execute(sql_cancel, val)
                    mydb.commit()
                    mycursor.execute("DELETE FROM tickets WHERE PNR=%s", (pnr,))
                    mydb.commit()
                    cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
                    if cont == "yes":
                        System.Main()
                    else:
                        System.log_out()
                else:
                    cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
                    if cont == "yes":
                        System.Main()
                    else:
                        System.log_out()
        except Exception as e:
            print("Error in cancel_ticket:", e)
            System.Main()

    @staticmethod
    def refund_history():
        try:
            print("\n" + "*" * 14)
            print("REFUND HISTORY")
            print("*" * 14)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT Train, No, TransId, TransDate, Source, Destination, CancelDate FROM cancels")
            results = mycursor.fetchall()
            if not results:
                print("\nNO BOOKINGS")
            else:
                print(tabulate(results, headers=['Train Name', 'Train No.', 'Transaction Id', 'Transaction Date', 'From', 'To', 'Cancel Date'], tablefmt='psql'))
                no = input("\nTRAIN NO.: ").strip()
                mycursor.execute("SELECT Train, No, TransId, TransDate, Source, Destination, CancelDate, PNR, CancelId, Deducted, Refund FROM cancels WHERE No=%s", (no,))
                rs = mycursor.fetchone()
                if rs:
                    print(rs[0], "Transaction Id:", rs[2])
                    print('(', rs[1], ')', "Transaction Date:", rs[3])
                    print(rs[4], "→", rs[5])
                    print(rs[6], "STATUS: CANCELLED")
                    print("PNR:", rs[7], "CANCELLATION/REFUND ID:", rs[8])
                    print("Refund Status: REFUNDED")
                    print("Refund Detail: Amount Credited To Bank With Reference No. rfnd_F2sP73q81TGHUT")
                    print("Amount deducted: ₹", rs[9], "Refunded Amount: ₹", rs[10])
                    print("Bank Name: Credit & Debit cards/Net Banking/UPI(Powered by Paytm)")
                else:
                    print("No refund details for this train")
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont == "yes":
                System.Main()
            else:
                System.log_out()
        except Exception as e:
            print("Error in refund_history:", e)
            System.Main()

    @staticmethod
    def train_schedule():
        try:
            print("\n" + "*" * 14)
            print("TRAIN SCHEDULE")
            print("*" * 14)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Yash1012108@", database="train")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT No, Name, Source, Destination, Deparature, Arrival FROM trains")
            results = mycursor.fetchall()
            print(tabulate(results, headers=['Train No.', 'Train Name', 'From', 'To', 'Deparature', 'Arrival'], tablefmt='psql'))
            cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if cont == "yes":
                System.Main()
            else:
                System.log_out()
        except Exception as e:
            print("Error in train_schedule:", e)
            System.Main()

    @staticmethod
    def log_out():
        try:
            print("\n**THANK YOU:::::VISIT AGAIN**\n")
            System.displayMenu()
        except Exception as e:
            print("Error in log_out:", e)
            System.displayMenu()


# ----------- Program Start -----------
DatabaseSetup.create_database()
DatabaseSetup.create_tables()
status = " "  # Dummy variable for loop control
while status != 0:
    System.displayMenu()
