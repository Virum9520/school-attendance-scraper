# Configuration file for the project

# Base URL for attendance data
BASE_URL = "https://edudel.nic.in/mis/eis/Attendance/frmAttendanceSecondPageHome.aspx"
# Day of month to fetch (1-31)
DAT = '28'
# Schools list - Format: "school_code-School Name"
SCHOOLS = [
    '1001109-Kiran Vihar-SBV',
    '1002403-Govt. Coed Secondary School,Joshi colony,Mandawali',
    # Add more schools here
    # 'School_id-Another School Name',
]
# Attendance type parameters (Present, On duty, Half Casul Leave, etc)
ATTENDANCE_TYPES = ['Pre1','OD1','half1','CL1','EL1','abs1','sus1','OL1','vac1']
# Output data directory (where files will be named as schoolname_date.xlsx)
OUTPUT_DIR = 'data'
# Request timeout (seconds)
TIMEOUT = 10
# Delay between requests (seconds)
REQUEST_DELAY = 1
