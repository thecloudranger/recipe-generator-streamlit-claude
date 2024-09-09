import streamlit as st
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os

# Initialize the Anthropic client
anthropic = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def generate_recipe(ingredients):
    prompt = f"{HUMAN_PROMPT}Generate a recipe using these ingredients: {', '.join(ingredients)}. Include title, ingredients list, and step-by-step instructions.{AI_PROMPT}"

    response = anthropic.completions.create(
        model="claude-2.1",
        max_tokens_to_sample=500,
        prompt=prompt
    )

    return response.completion

st.title("Recipe Generator")

st.write("Enter ingredients you have, and we'll generate a recipe for you!")

ingredients = st.text_input("Enter ingredients (comma-separated)")

if st.button("Generate Recipe"):
    if ingredients:
        ingredient_list = [i.strip() for i in ingredients.split(",")]
        recipe = generate_recipe(ingredient_list)
        st.write(recipe)
    else:
        st.warning("Please enter at least one ingredient.")
