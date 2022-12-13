import json

class JSONDisplayer:
    def __init__(self, json_templates):
        with open(json_templates,"r") as file:
            self.template = json.load(file)
    
    def show(self):
        pass

