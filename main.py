import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", torch_dtype=torch.bfloat16, device_map="auto")

print(pipeline('text-generation',model="HuggingFaceH4/zephyr-7b-beta", torch_dtype=torch.bfloat16, device_map="auto")('Generate a mechanics problem for me'))

print("model initialised")
# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
]
print("message initialised")
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print("prompt initialised")
outputs = pipe(prompt,  pad_token_id=50256, max_length=10, num_return_sequences=1, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print("output initialised")
print(outputs[0]["generated_text"])
