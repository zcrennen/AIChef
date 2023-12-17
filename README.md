# 🍽️ AI Chef

[![Demo Video](https://img.shields.io/badge/Demo%20Video-Watch-brightgreen?style=flat-square)](https://youtu.be/rPdr8t9-qcw?si=_GmN-G7fLr46vmQo)

Ever had some ingredients on hand, but not know what to make? Introducing AI Chef! AI Chef generates recipes for you based on whatever ingredients you have on hand. It generates a recipe from the following parameters:

- 🍛 Type (genre) of food
- 🥘 Available ingredients
- 🔌 Available appliances
- 🥗 Dietary restrictions
- 🍽️ Number of servings
- 💰 Price range

## Setup

### OpenAI API Key

1. Create an API key through OpenAI. First, create an OpenAI account, and go to this [link](https://platform.openai.com/api-keys).

2. Click "Create new secret key," then name it, and click "Create secret key." Copy this key and save it.

3. Create a file in your local folder named ".env". Write the line `OPENAI_API_KEY = ...` where "..." represents your API key.

### Dependencies

- (Recommended) Create a virtual environment (venv) to run this file.
- Inside your terminal, run the command:

    `pip install -r requirements.txt`


## How to Run

1. Inside your terminal, run the command:

    `streamlit run \main.py`

2. This will pull up a window with the website. Enjoy!

## Additional Resources

- [📊 Slideshow](https://docs.google.com/presentation/d/1eQs398lMs0YmgFpgqNXAdV-xA62oHYszKW8NsJz5aao/edit?usp=sharing)

### Notes

- Previous commits may show an API key. This key has since been deactivated. Nice try! 🙅‍♂️

- Each run of this costs ~$0.04. This can be lowered by using DALLE-2 instead of DALLE-3 (main.py line 40) 💰

- This project was voted best LLM project in our section. Thanks to Dr. [Zibo Wang](https://www.linkedin.com/in/zibo-wang-a6169655/) for the guidance with this project!
