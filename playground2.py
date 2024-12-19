from playground import time_openai, time_instructor_openai, time_anthropic, time_instructor_anthropic
from typing import Literal, Union
from pydantic import BaseModel
with open("prompt.txt", "r") as f:
    system_prompt = f.read()
    
# Variables that need to be formatted in system_prompt:
print("Variables needed for system_prompt formatting:")
print("- CUSTOMER_CONVERSATION")
print("- USER_STORIES") 
print("- ALREADY_SELECTED_STORY")


class UserStorySelectorWithRAG(BaseModel): 
    content: Literal["unsupportedRequest", "tryThisUserStory"]
    storyId: Union[str, None] = None
    storyTitle: Union[str, None] = None
    explanation: Union[str, None] = None
    customerMessage: Union[str, None] = None

user_message = "Hi I need to add my new waitress to boh. she doesnt need admin access"
customer_conversation = f'''
{{ "role": "user", "content": "{user_message}" }}
'''

user_stories = '''
{"storyId": "1", "title": "Guide a user to add a new menu item"},
{"storyId": "12", "title": "Guide a BOH user to add new standard employees, fill in their general information, assign a location, login code if needed, add a job position. This does not guide a user to sync new employees."},
{"storyId": "21", "title": "Guide a BOH user to add a new manager in BOH. Managers are the only ones able to edit the menu, add new users, or edit user info. It does not guide a user to add emails to any other SpotOn platform such as reporting or Dashboard."},
{"storyId": "33", "title": "Guide a user to delete another user"},
{"storyId": "42", "title": "Guide a user to deactivate another user"},
{"storyId": "50", "title": "Guide a user  to add a new user to the dashboard"},
{"storyId": "61", "title": "Guide a user to edit or delete a menu group"},
{"storyId": "72", "title": "Guide a user to add new emails to Reporting Access"},
{"storyId": "83", "title": "Guide a user to reset their password"},
{"storyId": "94", "title": "Guide a user to edit or delete a tax percentage for a menu item or group"}

'''

already_selected_story = '''
'''

formatted_prompt = system_prompt.format(CUSTOMER_CONVERSATION=customer_conversation, USER_STORIES=user_stories, ALREADY_SELECTED_STORY=already_selected_story)


import random
import string


openai_times = []
anthropic_times = []
instructor_openai_times = []
instructor_anthropic_times = []

for i in range(40):
    random_string = "\n\n" + ''.join(random.choices(string.ascii_letters + string.digits, k=20))

    openai_response, openai_time = time_openai([{"role": "system", "content": formatted_prompt + random_string}, {"role": "user", "content": user_message}])
    anthropic_response, anthropic_time = time_anthropic(formatted_prompt + random_string, [{"role": "user", "content": user_message} ])
    instructor_openai_response, instructor_openai_time = time_instructor_openai([{"role": "system", "content": formatted_prompt + random_string}, {"role": "user", "content": user_message}], UserStorySelectorWithRAG)
    instructor_anthropic_response, instructor_anthropic_time = time_instructor_anthropic([{"role": "system", "content": formatted_prompt + random_string}, {"role": "user", "content": user_message}], UserStorySelectorWithRAG)

    openai_times.append(openai_time)
    anthropic_times.append(anthropic_time)
    instructor_openai_times.append(instructor_openai_time)
    instructor_anthropic_times.append(instructor_anthropic_time)


print("OpenAI times:", openai_times)
print("Anthropic times:", anthropic_times)
print("Instructor OpenAI times:", instructor_openai_times)
print("Instructor Anthropic times:", instructor_anthropic_times)

print("OpenAI average:", sum(openai_times) / len(openai_times))
print("Anthropic average:", sum(anthropic_times) / len(anthropic_times))
print("Instructor OpenAI average:", sum(instructor_openai_times) / len(instructor_openai_times))
print("Instructor Anthropic average:", sum(instructor_anthropic_times) / len(instructor_anthropic_times))

import statistics
print("OpenAI std dev:", statistics.stdev(openai_times))
print("Anthropic std dev:", statistics.stdev(anthropic_times))
print("Instructor OpenAI std dev:", statistics.stdev(instructor_openai_times))
print("Instructor Anthropic std dev:", statistics.stdev(instructor_anthropic_times))




    
    