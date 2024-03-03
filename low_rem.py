from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")

model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta", low_cpu_mem_usage=True)
model.load_adapter("brianc07/easypass4")

input_text = "Generate a mechanics problem that involves angular momentum and moment of inertia, only output the problem and nothing else."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=256)
print(tokenizer.decode(outputs[0]))

#config = LoraConfig(lora_alpha=16, lora_dropout=0.1, r=64, bias="none", task_type="CASUAL_LM")
#model.add_adapter(peft_config)

