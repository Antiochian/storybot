# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:30:34 2020

@author: Hal
"""


from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



def read_responses():
    """Get results from spreadsheet
    """
    SPREADSHEET_ID = 'CENSORED'
    RANGE_NAME = "Form responses 1!A2:ZZZ"
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    res = []
    for row in values:
        if (not row) or (row[1] == ""):
            pass
        else:
            res.append(row)
    return res

def delete_responses(finalidx=20):
    if finalidx == 1:
        print("Nothing to delete, exited early")
        return
    """
    Deletes all current responses
    """
    SPREADSHEET_ID = 'CENSORED'
    #SHEET_ID = "Form responses 1"
    SHEET_ID = 604944233
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    body = {"requests": [
                    {
                      "deleteDimension": {
                        "range": {
                          "sheetId": SHEET_ID,
                          "dimension": "ROWS",
                          "startIndex": 1,
                          "endIndex": finalidx
                        }
                      }
                    }
                  ]
                }
    response = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
    return response
