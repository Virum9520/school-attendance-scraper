from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mapping attendance type codes to abbreviations
ATTENDANCE_STATUS_MAP = {
    'Pre1': 'Present',
    'OD1': 'On Duty',
    'half1': 'Half Day',
    'CL1': 'Casual Leave',
    'EL1': 'Earned Leave',
    'abs1': 'Absent',
    'sus1': 'Suspended',
    'OL1': 'On Leave',
    'vac1': 'Vacation'
}


def parse_attendance_data(html, attendance_type):
    if not html:
        logger.error("No HTML content provided")
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    attendance_records = []
    
    # Find the table class="mistable" and id="Table1"
    table = soup.find('table', {'class': 'mistable', 'id': 'Table1'})
    
    if not table:
        return []
    
    if table:
        rows = table.find_all('tr')
        
        if len(rows) <= 1: 
            return []
        
        
        for row in rows[1:]:
            cells = row.find_all('td')          
            
            if cells[0].get('class') and 'MISFieldCaptionTD' in cells[0].get('class'):
                continue   
                    
            # Extract text from each cell
            cell_data = [cell.get_text(strip=True) for cell in cells]
            
            school_id = cell_data[1] if len(cell_data) > 1 else ''
            school_name = cell_data[2] if len(cell_data) > 2 else ''
            employee_id = cell_data[3] if len(cell_data) > 3 else ''
            employee_name = cell_data[4] if len(cell_data) > 4 else ''
            status_full_name = ATTENDANCE_STATUS_MAP.get(attendance_type, attendance_type)
            
            record = {
                'school_id': school_id,
                'school_name': school_name,
                'employee_id': employee_id,
                'employee_name': employee_name,
                'attendance_status': status_full_name
            }
            attendance_records.append(record)
    
    return attendance_records

