from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
step = 0
def chatbot_response_b(step,user):
    new_user_input_ids = tokenizer.encode(user + tokenizer.eos_token, return_tensors='pt')

    bot_input_ids = torch.cat([chat_history_ids_test, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
    print(bot_input_ids)
    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids_test = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    x = tokenizer.decode(chat_history_ids_test[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    # pretty print last ouput tokens from bot
    print("DialoGPT: {}".format(x))
    return x
