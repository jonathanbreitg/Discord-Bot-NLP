import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import os
import tensorflow as tf
from random import randint
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Example Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    'chatterbot.corpus.english'
)




client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$generate'):
        input_ids = tokenizer.encode(message.content[9:], return_tensors='tf')
        tf.random.set_seed(randint(5))
        sample_outputs = model.generate(
            input_ids,
            do_sample=True,
            max_length=50,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1
        )
        print("Output:\n" + 100 * '-')
        for i, sample_output in enumerate(sample_outputs):
          print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))
        print(tokenizer.decode(sample_output, skip_special_tokens=True))
        await message.channel.send(tokenizer.decode(sample_output, skip_special_tokens=True))
        return
    if message.content.startswith('$'):
        if message.content == '$spam':
            await message.channel.send('i dont like spamming')
            await message.channel.send('but ok i guess')
            await message.channel.send('labne')
            await message.channel.send('no i should pick a better message')
            await message.channel.send('everyone spams gay')
            await message.channel.send('gay')
            await message.channel.send('gay')
            await message.channel.send('gay')
            await message.channel.send('gay')
            return
        print(message.content)
        response = chatbot.get_response(message.content)
        print(response)
        await message.channel.send(response)


client.run(os.environ['token_discord'])
