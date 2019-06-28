from flask import Flask
import re
app = Flask(__name__)

def isAlphanumeric(str):
    match = re.findall("^[a-zA-Z0-9]+$", str)
    if match:
        return True
    else:
        return False

def isAlpha(str):
    match = re.findall("^[a-zA-Z]+$", str)
    if match:
        return True
    else:
        return False

def isDigit(str):
    match = re.findall("^[0-9]+$", str)
    if match:
        return True
    else:
        return False

def isBool(str):
    match = re.findall("^(True|False)+$", str)
    if match:
        return True
    else:
        return False

def inputValidation(input, type):
    if type == 'alphanumeric':
        return isAlphanumeric(input)
    elif type == 'alpha':
        return isAlpha(input)
    elif type == 'digit':
        return isDigit(input)
    elif type == 'bool':
        return isBool(input)
    else:
        return False
