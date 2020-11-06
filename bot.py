step = 0
import discord
import logging
from self_chat import chatbot_response_b
import tensorflow as tf
from random import randint
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
client = discord.Client()
chat_history_ids = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global step
    if message.content.startswith('*'):
        to_send=chatbot_response_b(step=step,user=message.content)
        print(to_send)
        try:
            await message.channel.send(to_send)
        except:
            await message.channel.send("no response...")


    if message.author == client.user:
        return
    if message.content.startswith('$'):
        if message.content == '$spam':
            pass
        print(message.content)



client.run("NzY0MDU5OTA2MzA2MzQyOTIz.X4AwPQ.PMRjDHOmNX3iqhf-mQgDq8cY7bk")
