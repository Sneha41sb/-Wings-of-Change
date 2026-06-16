import os
from database import init_db
import volunteers
import donations
import campaigns

def verify():
    print("Starting system verification...")
    
    # Initialize DB
    init_db()
    print("[1/4] Database initialized.")
    
    # Test Volunteers
    volunteers.add_volunteer("Test Volunteer", "1234567890", "Coordinator")
    vols = volunteers.view_volunteers()
    assert any(v[1] == "Test Volunteer" for v in vols), "Volunteer test failed"
    print("[2/4] Volunteer management verified.")
    
    # Test Donations
    donations.add_donation("Test Donor", "5000 INR")
    dons = donations.view_donations()
    assert any(d[1] == "Test Donor" for d in dons), "Donation test failed"
    print("[3/4] Donation tracking verified.")
    
    # Test Campaigns
    campaigns.log_campaign("Food Drive", "Slum Area A", 150)
    camps = campaigns.view_campaigns()
    assert any(c[1] == "Food Drive" for c in camps), "Campaign test failed"
    print("[4/4] Campaign logging verified.")
    
    print("\nVerification Complete! All core modules are functional.")

if __name__ == "__main__":
    verify()
