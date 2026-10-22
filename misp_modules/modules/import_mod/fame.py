import base64
import json

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

moduleconfig = []

mispattributes = {
    "inputSource": ["file"],
    "output": ["MISP objects"],
    "format": "misp_standard",
}

userConfig = {
    "include_unconfirmed": {
        "type": "Boolean",
        "message": "Include findings whose exploitation could not be confirmed",
        "checked": "true",
    },
}

ANALYSIS_STATUS = ("Pending", "Finished", "")

def handler(q=False):
##
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
