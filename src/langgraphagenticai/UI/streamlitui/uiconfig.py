# here we read .ini files and set up the configuration for the UI   

from configparser import ConfigParser

class Config:
    def __init__(self,config_file="src\langgraphagenticai\UI\streamlitui\uiconfigfile.ini"):
        self.config= ConfigParser()  # it read .ini file i.e config file
        self.config.read(config_file)

    def get_llm_option(self):
        return self.config['DEFAULT'].get("LLM_OPTIONS").split(", ")        
    



        