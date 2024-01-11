import openai
from IPython.display import display, Markdown, Latex, HTML, JSON
import time

client = openai.OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

### Translation
# prompt = f"""
# Translate the following English text to Spanish: \ 
# ```Hi, I would like to order a blender```
# """

# prompt = f"""
# Tell me which language this is: 
# ```Combien coûte le lampadaire?```
# """

# prompt = f"""
# Translate the following text to French and Spanish
# and an English pirate: \
# ```I want to order a basketball```
# """

# prompt = f"""
# Translate the following text to Spanish in both the \
# formal and informal forms: 
# 'Would you like to order a pillow?'
# """

# response = get_completion(prompt)
# print(response)



### Universal Translator
### Imagine you are in charge of IT at a large multinational e-commerce company. Users are 
### messaging you with IT issues in all their native languages. Your staff is from all over the ### world and speaks only their native languages. You need a universal translator!'''

# user_messages = [
#     "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
#     "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
#     "Il mio mouse non funziona",                                 # My mouse is not working
#     "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
#     "我的屏幕在闪烁"                                               # My screen is flashing
# ] 

# for issue in user_messages:
#     prompt = f"Tell me what language this is: ```{issue}```"
#     lang = get_completion(prompt)
#     print(f"Original message ({lang}): {issue}")
#     time.sleep(20) #time delay for free-tier rate limit of 3 RPM

#     prompt = f"""
#     Translate the following text to English and Korean: ```{issue}```
#     """
#     response = get_completion(prompt)
#     print(response, "\n")
#     time.sleep(20) #time delay for free-tier rate limit of 3 RPM



### Tone Transformation
### Writing can vary based on the intended audience. ChatGPT can produce different tones.

# prompt = f"""
# Translate the following from slang to a business letter: 
# 'Dude, This is Joe, check out this spec on this standing lamp.'
# """
# response = get_completion(prompt)
# print(response)



### Format Conversion - ChatGPT can translate between formats. The prompt should describe the input and output formats.
# data_json = { "resturant employees" :[ 
#     {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
#     {"name":"Bob", "email":"bob32@gmail.com"},
#     {"name":"Jai", "email":"jai87@gmail.com"}
# ]}

# prompt = f"""
# Translate the following python dictionary from JSON to an HTML \
# table with column headers and title: {data_json}
# """
# response = get_completion(prompt)

# with open("response.html", "w") as file:
#     file.write(response)



### Spellcheck / Grammar - To signal the LLM you want it to proofread text, instruct the model to 'proofread' or 'proofread and correct'.

# text = [
#     "The girl with the black and white puppies have a ball.",  # The girl has a ball.
#     "Yolanda has her notebook.", # ok
#     "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
#     "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
#     "Your going to need you’re notebook.",  # Homonyms
#     "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
#     "This phrase is to cherck chatGPT for speling abilitty"  # spelling
#     ]

# for t in text:
#     prompt = f"""Proofread and correct the following text
#     and rewrite the corrected version. If you don't find
#     and errors, just say "No errors found". Don't use 
#     any punctuation around the text:
#     ```{t}```"""
#     response = get_completion(prompt)
#     print(response)
#     time.sleep(22)

# text = f"""
# Got this for my daughter for her birthday cuz she keeps taking \
# mine from my room.  Yes, adults also like pandas too.  She takes \
# it everywhere with her, and it's super soft and cute.  One of the \
# ears is a bit lower than the other, and I don't think that was \
# designed to be asymmetrical. It's a bit small for what I paid for it \
# though. I think there might be other options that are bigger for \
# the same price.  It arrived a day earlier than expected, so I got \
# to play with it myself before I gave it to my daughter.
# """
# prompt = f"proofread and correct this review: ```{text}```"
# response = get_completion(prompt)
# print(response)


# from redlines import Redlines

# diff = Redlines(text,response)
# display(Markdown(diff.output_markdown)) ## If Jupyter