from transformers import AutoTokenizer, AutoModelForCausalLM

#tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b")
#model = AutoModelForCausalLM.from_pretrained("google/gemma-7b")


tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta")

input_text = "Generate a mechanics problem that involves angular momentum and moment of inertia, only output the problem and nothing else."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))