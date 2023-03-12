# Code made by https://github.com/EduContin
# This script restarts bot.py every X amount of time to verify if memberships expired, and if so, user gets bannd/kicked.
# More often restarts = more often bot verifies expired memberships
# Recommended amount = 4-12 hours

import subprocess
import time

while True:
    # Open the bot.py file using the subprocess module
    bot_process = subprocess.Popen(['python', 'bot.py'])
    
    # Wait for given amount of seconds
    time.sleep(43200) # That's 12 hours
    
    # Terminate the bot.py process
    bot_process.terminate()