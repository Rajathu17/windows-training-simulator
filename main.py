# Main entry point for Windows Training Simulator
# File: main.py

import os
import json
from modules import file_operations, network_troubleshooting, system_management
from utils import logger, validator, feedback

# Load user preferences from configuration
def load_config():
    try:
        with open("config/config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
        return {"theme": "default", "prompt": "> "}

# Language support
def load_language(language):
    try:
        with open(f"config/language/{language}.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Language file for '{language}' not found. Falling back to English.")
        return load_language("en")

# Main menu
def main_menu(config, lang):
    print(lang["welcome"])
    modules = {
        "1": file_operations,
        "2": network_troubleshooting,
        "3": system_management
    }

    print(lang["choose_module"])
    for key, module in modules.items():
        print(f"[{key}] {module.__name__.split('.')[-1].replace('_', ' ').capitalize()}")

    choice = input(config["prompt"])
    if choice in modules:
        module = modules[choice]
        module.run_module(config, lang)
    else:
        print(lang["invalid_option"])

# Entry point
def main():
    config = load_config()
    lang = load_language(config.get("language", "en"))
    
    logger.log("Starting Windows Training Simulator")

    while True:
        main_menu(config, lang)
        cont = input(lang["continue_prompt"])
        if cont.lower() not in ["yes", "y"]:
            break

if __name__ == "__main__":
    main()
