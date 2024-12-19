from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv
from pydantic import BaseModel
import instructor
import time

load_dotenv()

client = OpenAI()
inst_client = instructor.from_openai(client)

ant_client = Anthropic()
inst_ant_client = instructor.from_anthropic(ant_client)

def time_openai(messages):
    # Time the native OpenAI call
    start_time = time.time()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )
    end_time = time.time()
    return response.choices[0].message.content, end_time - start_time




# # Time the instructor call
def time_instructor_openai(messages, response_model):
    start_time = time.time()
    response = inst_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        response_model=response_model,
    )
    end_time = time.time()
    return response, end_time - start_time



def time_anthropic(prompt, messages):
    # Time the native Anthropic call
    start_time = time.time()
    response = ant_client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        system=prompt,
        messages = messages
    )
    end_time = time.time()
    return response.content[0].text, end_time - start_time


def time_instructor_anthropic(messages, response_model):
    # Time the instructor Anthropic call
    start_time = time.time()
    response = inst_ant_client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        messages=messages,
        response_model=response_model,
    )
    end_time = time.time()
    return response, end_time - start_time
