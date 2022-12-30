#get API key as a secret
import os
my_secret = os.environ['COHERE_API_KEY']

#import Cohere & input API key
import cohere
co = cohere.Client(my_secret)

#command model to write story
response = co.generate(
  prompt="Write a scene that can show off your dramatic chops or comedic style",
  model='command-xlarge-20221108',
  max_tokens=450
)

#display the story
print (response)

# hello new friends! if you would like to fork, you can get your own free API key here: https://dashboard.cohere.ai/welcome/register?utm_source=other&utm_medium=social&utm_campaign=nicks-repl