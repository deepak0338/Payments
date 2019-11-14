#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:03:24 2019

@author: uxas
"""

import pandas as pd
import numpy as np

file_path = '/Users/uxas/Fees_details/fees.csv'
m_list = ['Name', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
file = pd.read_csv(file_path).copy(deep=True)
file.to_csv(file_path, index = False)
test = file.groupby(['Sep', 'Oct'])




