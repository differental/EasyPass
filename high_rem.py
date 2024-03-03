from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")

model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
model.load_adapter("brianc07/easypass4")

input_text = "Generate four mechanics problems that involves angular momentum and moment of inertia, only output the problem and nothing else. A spherical ball is rolling down the slope "
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=2048)
print(tokenizer.decode(outputs[0]))

#config = LoraConfig(lora_alpha=16, lora_dropout=0.1, r=64, bias="none", task_type="CASUAL_LM")
#model.add_adapter(peft_config)
