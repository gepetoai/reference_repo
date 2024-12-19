import requests

class Gepeto:
    def __init__(self):
        #return a list of agents
        #return org-specific api keys 
        #return database / resource variables
        #return globl variables
        pass

class Agent:
    def __init__(self, name):
        try:
            self.name = name
            headers = {"API-Key": "test-key"}  
            response = requests.get(f"http://0.0.0.0:8001/api/v1/agents/{self.name}", headers=headers)
            self.llm = response.json().get("llm")
            self.model = response.json().get("model")
            self.prompt = response.json().get("prompt")
            self.response_model = response.json().get("response_model")

        except Exception as e:
            print(e)


    def async_run(self):
        pass


    def run(self):
        info = self.get_info()
        print("got info: ", info)
        print(f"Agent {self.name} is running")

        if self.llm == "openai": 
            #impleent openai client 
            pass

        elif self.llm == "anthropic":
            #impleent anthropic client
            pass

        else:
            raise ValueError(f"Model {self.llm} not supported")
