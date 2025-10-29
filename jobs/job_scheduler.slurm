#!/bin/bash
#SBATCH --job-name=attendance_scraper
#SBATCH --output=output/scraper_%j.out
#SBATCH --partition=standard
# module load python
# pip install -r requirements.txt

# python /path/main.py

# crontab -e
# 0 2 * * * sbatch /home/youruniqname/myjob.sh (job at 2am everyday)