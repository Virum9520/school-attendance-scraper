import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_to_excel(data, output_dir, school_name, date):
    if not data:
        return False
    
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filename = f"{school_name}_{date}.xlsx"
        filepath = os.path.join(output_dir, filename)
        
        df = pd.DataFrame(data)
        
        column_order = ['school_id', 'school_name', 'employee_id', 
                       'employee_name', 'attendance_status']
        
        available_columns = [col for col in column_order if col in df.columns]
        df = df[available_columns]
        
        df.to_excel(filepath, index=False, engine='openpyxl')
        return True
        
    except Exception as e:
        logger.error(f"Error saving data to Excel: {str(e)}")
        return False

