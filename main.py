import sys
from database import init_db
import volunteers
import donations
import campaigns

def main_menu():
    print("\n--- NayePankh Foundation Management System ---")
    print("1. Manage Volunteers")
    print("2. Track Donations")
    print("3. Log Campaigns/Events")
    print("4. Exit")
    return input("Select an option: ")

def volunteer_menu():
    while True:
        print("\n--- Volunteer Management ---")
        print("1. Add Volunteer")
        print("2. View All Volunteers")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            role = input("Enter Role: ")
            volunteers.add_volunteer(name, phone, role)
            print("Volunteer added successfully!")
        elif choice == '2':
            rows = volunteers.view_volunteers()
            print("\nID | Name | Phone | Role")
            print("-" * 30)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        elif choice == '3':
            break
        else:
            print("Invalid selection.")

def donation_menu():
    while True:
        print("\n--- Donation Tracking ---")
        print("1. Add Donation")
        print("2. View All Donations")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            donor = input("Enter Donor Name: ")
            item = input("Enter Amount or Item: ")
            donations.add_donation(donor, item)
            print("Donation logged successfully!")
        elif choice == '2':
            rows = donations.view_donations()
            print("\nID | Donor | Amount/Item | Date")
            print("-" * 40)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        elif choice == '3':
            break
        else:
            print("Invalid selection.")

def campaign_menu():
    while True:
        print("\n--- Campaign Logging ---")
        print("1. Log New Campaign")
        print("2. View Past Campaigns")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            event = input("Event Name: ")
            loc = input("Location: ")
            reached = input("Beneficiaries Reached: ")
            try:
                reached = int(reached)
            except ValueError:
                reached = 0
            campaigns.log_campaign(event, loc, reached)
            print("Campaign logged successfully!")
        elif choice == '2':
            rows = campaigns.view_campaigns()
            print("\nID | Event | Location | Date | Reached")
            print("-" * 50)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
        elif choice == '3':
            break
        else:
            print("Invalid selection.")

def run():
    init_db()
    while True:
        choice = main_menu()
        if choice == '1':
            volunteer_menu()
        elif choice == '2':
            donation_menu()
        elif choice == '3':
            campaign_menu()
        elif choice == '4':
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    run()
