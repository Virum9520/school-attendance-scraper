import requests
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_attendance_html(base_url, atttype, dat, name, dis, timeout=20, delay=1):
    params = {
        'atttype': atttype,
        'dat': dat,
        'name': name,
        'dis': dis
    }
    try:
        response = requests.get(base_url, params=params, timeout=timeout)
        response.raise_for_status()
        
        # Add delay to avoid overwhelming the server
        time.sleep(delay)
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching attendance data: {str(e)}")
        return None

