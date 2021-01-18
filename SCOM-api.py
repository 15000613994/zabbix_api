# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 17:45
# @Author  : Gao, Jiezhang (Vic)
# @File    : export_alert_data.py

import csv
import json
import os

from modules import object
from modules import authentication
from modules import base_lib


CSV_HEADERS = ['displayName', 'id', 'className', 'path', 'fullName']


#####################################
#       Logging Configuration       #
#####################################
this_module_name = str(os.path.basename(__file__)).replace('.py', '')
logger = base_lib.configure_logger(this_module_name)

if __name__ == "__main__":
    # Get output CSV filename - interactive.
    csv_filename = base_lib.get_csv_filename()
    # Get SCOM URL
    scom_url = base_lib.get_url()
    # Log in
    (scom_auth, scom_cookies) = authentication.login(scom_url)
    # Define payload
    object_payload = 'ClassName LIKE \'%Computer%\''
    # Call API to get alerts
    response_content = object.get_object_data(scom_url, scom_auth, scom_cookies, json.dumps(object_payload))
    # Log out
    authentication.logout(scom_url, scom_auth, scom_cookies)
    if response_content is None:
        raise Exception('Failed to get columns from SCOM. Refer to logs for details.')
    else:
        # Write CSV
        with open(csv_filename, 'a', newline='', encoding="utf-8") as csv_file:
            logger.info('Opened the CSV file %s' % csv_filename)
            inst_csv = csv.DictWriter(csv_file, CSV_HEADERS)
            inst_csv.writeheader()
            inst_csv.writerows(response_content['scopeDatas'])