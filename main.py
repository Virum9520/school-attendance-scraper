# pipeline: Fetch HTML ===> Parse Data ===> Save to Excel

import sys
import re
from pipeline.fetch_html import fetch_attendance_html
from pipeline.parse_attendance import parse_attendance_data
from pipeline.save_data import save_to_excel
import config

BASE_URL = "https://edudel.nic.in/mis/eis/Attendance/frmAttendanceSecondPageHome.aspx"
OUTPUT_DIR = 'data'
TIMEOUT = 10
REQUEST_DELAY = 1

ATTENDANCE_DISPLAY_NAMES = {
    'Pre1': 'Present',
    'OD1': 'On Duty',
    'half1': 'Half Casual Leave',
    'CL1': 'Casual Leave',
    'EL1': 'Earned Leave',
    'abs1': 'Absent',
    'sus1': 'Suspended',
    'OL1': 'Other Leave',
    'vac1': 'Vacation'
}

def main():
    print("School Attendance Scraper")
    print("=" * 80)
    
    total_files_saved = 0
    
    # Process each school
    for school in config.SCHOOLS:
        match = re.match(r'(\d+)-(.+)', school)
        if not match:
            print(f"✗ Invalid school format: {school}")
            continue
        
        school_code = match.group(1)
        school_name = match.group(2).strip()
        
        print(f"\nProcessing: {school_name} ({school_code})")
        print("-" * 80)
        
        school_records = []
        
        for att_type in ATTENDANCE_DISPLAY_NAMES.keys():
            display_name = ATTENDANCE_DISPLAY_NAMES.get(att_type, att_type)
            print(f"Fetching {display_name}...")
            
            # Step 1 Fetch HTML from link
            html = fetch_attendance_html(
                base_url=BASE_URL,
                atttype=att_type,
                dat=config.DATE,
                name=school,
                dis=school_code,
                timeout=TIMEOUT,
                delay=REQUEST_DELAY
            )            
            if not html:
                print(f"Failed to fetch {att_type}")
                continue
            
            # Step 2 Parsing HTML data
            records = parse_attendance_data(html, att_type)
            
            if records:
                print(f"  Found {len(records)} records")
                school_records.extend(records)
            else:
                print("0 records present")
        
        # Step 3 Saving to Excel
        if school_records:
            print(f"\nSaving {len(school_records)} records for this school...")
            save_to_excel(school_records, OUTPUT_DIR, school_name, config.DATE)
            
            print(f"Saved to {OUTPUT_DIR}/{school_name}_{config.DATE}.xlsx")
            total_files_saved += 1

    print(f"Successfully created {total_files_saved} Excel file")

if __name__ == "__main__":
    main()

