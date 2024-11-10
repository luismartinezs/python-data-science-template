# https://docs.ell.so/

import ell

ell.init(store="./logdir")

@ell.simple(model="gpt-4o-mini")
def hello(world: str):
    """You are a helpful assistant""" # System prompt
    name = world.capitalize()
    return f"Say hello to {name}!" # User prompt

hello("sam altman") # just a str, "Hello Sam Altman! ..."


from typing import List

@ell.simple(model="gpt-4o-mini", temperature=1.0, n=10)
def write_ten_drafts(idea : str):
   """You are an adept story writer. The story should only be 3 paragraphs"""
   return f"Write a story about {idea}."

@ell.simple(model="gpt-4o", temperature=0.1)
def choose_the_best_draft(drafts : List[str]):
   """You are an expert fiction editor."""
   return f"Choose the best draft from the following list: {'\n'.join(drafts)}."

drafts = write_ten_drafts(idea)

best_draft = choose_the_best_draft(drafts) # Best of 10 sampling.


@ell.tool()
def scrape_website(url : str):
   return requests.get(url).text

@ell.complex(model="gpt-5-omni", tools=[scrape_website])
def get_news_story(topic : str):
   return [
      ell.system("""Use the web to find a news story about the topic"""),
      ell.user(f"Find a news story about {topic}.")
   ]

message_response = get_news_story("stock market")
if message_response.tool_calls:
   for tool_call in message_response.tool_calls:
      pass
if message_response.text:
   print(message_response.text)
if message_response.audio:
   # message_response.play_audio() supprot for multimodal outputs will work as soon as the LLM supports it
   pass