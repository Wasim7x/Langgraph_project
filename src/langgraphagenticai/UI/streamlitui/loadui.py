import streamlit as st
import os 
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage
from src.langgraphagenticai.UI.streamlitui.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()  # config
        self.uset_controls = {}
