##################
# Run this file in the terminal with the following line
# streamlit run .\main.py
##################
import streamlit as st
import openai
from openai import OpenAI
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.llms import OpenAI

###################Init###################
#Load in API Key
api_key = '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'
#Initialize langchain chat client
chat = ChatOpenAI(temperature=0.7, openai_api_key=api_key)
#Initialize openai client
client = OpenAI(openai_api_key=api_key)
##########################################

def generateDish(genre, ingredients, appliances, diet, servings, price):
    prompt_template = f'Name a {genre} dish that uses {ingredients}. I can only cook with {appliances}. It must follow a {diet} diet. I want {servings} servings, and to spend ${price}.'
    response = chat(
        [
            SystemMessage(content='You are an AI Chef. List only the name of the dish with detail, and nothing else.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content

def GDImage(prompt):
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    #Generates and Displays an image

    #Generation
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="512x512",
        quality="standard",
        n=1,
    )

    url = response.data[0].url
    #Display
    st.image(url, use_column_width=True)

def generateRecipe(dish, ingredients, appliances, diet, servings, price):
    prompt_template = f"Give me an in depth recipe for {servings} serving(s) of {dish}. The ingredients I currently have are {ingredients}. The appliances I can use are {appliances}. It must follow a {diet} diet. I want to spend at most ${price}."
    response = chat(
        [
            SystemMessage(content='You are an AI Chef. Give an in depth recipe for the required amount of servings of the dish, including the ingredients, prices, steps, and nothing else.'),
            HumanMessage(content=prompt_template)
        ]
    )
    return response.content



# Define the Streamlit app
def main():
    # Set the title and a greeting message
    st.title('AI Chef')
    st.header('Hello from your AI Chef! I will help you make a recipe')
    
    genre = st.text_input('What type of food would you like to make (Italian, Mexican, etc)?')
    if genre:
        ingredients = st.text_input('What ingredients do you have to cook with?')
        if ingredients:
            appliances = st.text_input('What appliances do you have to cook with (microwave, oven, etc)?')
            if appliances:
                diet = st.text_input('What sort of dietary restrictions do you have (vegetarian, keto, etc)?')
                if diet:
                    servings = st.text_input('How many servings would you like to make?')
                    if servings:
                        price = st.text_input('How much would you like to spend on this meal?')
                        if price:
                            dish = generateDish(genre=genre,ingredients=ingredients,appliances=appliances,diet=diet,servings=servings, price=price)
                            st.write(f'You can make {dish}')
                            GDImage(prompt=dish)
                            recipe = generateRecipe(dish=dish,ingredients=ingredients,appliances=appliances,diet=diet,servings=servings, price=price)
                            st.write(f'Here is the recipe for {dish}')
                            st.write(recipe)

# Run the Streamlit app
if __name__ == '__main__':
    main()
