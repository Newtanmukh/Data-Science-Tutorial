import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


os.environ['GEMINI_API_KEY'] = "YOUR-API-KEY"
llm = ChatGoogleGenerativeAI( model="gemini-3-flash-preview",temperature=0.6)



def generate_restaurant_cuisine_and_items(cuisine):
    cuisine_template = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a hotel for {cuisine} food. suggest a good name for this. tell me just one name thats it.'
    )

    name_chain = cuisine_template | llm | StrOutputParser()

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Suggest some menu items for {restaurant_name}. Return it as comma separated values.'
    )

    food_items_chain = prompt_template_items | llm | StrOutputParser()

    restaurant_name = name_chain.invoke({'cuisine': cuisine})
    menu_response = food_items_chain.invoke({'restaurant_name': restaurant_name})

    return {'restaurant_name': restaurant_name, 'menu_response': menu_response}


if __name__ == "__main__":
    print(generate_restaurant_cuisine_and_items(cuisine="Breakfast"))