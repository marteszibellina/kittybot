"""
Created on: 24.12.2024
@author: marteszibellina
"""

import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
print(token)
