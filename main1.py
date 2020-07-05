# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:51:19 2020

@author: benfa
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/benfa/Desktop/ds_salary_proj/chromedriver"
df = gs.get_jobs('data scientist', 15, False, path, 10)