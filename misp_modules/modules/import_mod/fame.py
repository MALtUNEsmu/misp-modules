import base64
import json
import requests

from pymisp import MISPObject

misperrors = {"error": "Error"}

moduleinfo = {
    "version": "0.1",
    "author": "MALtUNEsmu",
    "description": "Module to import the JSON findings from the FAME analysis platform.",
    "module-type": ["import"],
    "name": "Fame Import",
    "logo": "",
    "requirements": ["PyMISP"],
    "features": (
        "TO BE FILLED"
    ),
    "references": ["https://fame.readthedocs.io/en/latest/"],
    "input": "Fame JSON result file",
    "output": "MISP objects with attributes",
}

moduleconfig = [
    "apikey",
    "fame_instance_url"
]

mispattributes = {
    "inputSource": ["file"],
    "output": ["MISP objects"],
    "format": "misp_standard",
}

userConfig = {
    "filter_by_tag": {
        "type": "String",
        "message": "Add tag based on...",
        "checked": "false",
    },
}

ANALYSIS_STATUS = ("Pending", "Finished", "")
headers = {
    'Accept': "application/json",
    'X-API-KEY': FAME_API_KEY
}
ENDPOINT = # have the url of the instance here

def handler(q=False):
##


with open(filepath, 'rb') as f:
    
       'file': id


    r = requests.get(ENDPOINT/file, data=params, files=files, headers=headers)
    return {"results": fame.results}


def introspection():
    modulesetup = {}
    try:
        userConfig
        modulesetup["userConfig"] = userConfig
    except NameError:
        pass
    try:
        inputSource
        modulesetup["inputSource"] = inputSource
    except NameError:
        pass
    modulesetup["format"] = "misp_standard"
    return modulesetup


def version():
    moduleinfo["config"] = moduleconfig
    return moduleinfo
