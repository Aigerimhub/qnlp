from transformers import GPT2LMHeadModel, GPT2TokenizerFast, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

train_dataset = TextDataset(tokenizer=tokenizer, file_path="data/kazakh_corpus.txt", block_size=128)
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

training_args = TrainingArguments(
    output_dir="./gpt_kazakh",
    overwrite_output_dir=True,
    per_device_train_batch_size=4,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=1,
)

trainer = Trainer(model=model, args=training_args, train_dataset=train_dataset, data_collator=data_collator)
trainer.train()
model.save_pretrained("gpt_kazakh")
tokenizer.save_pretrained("gpt_kazakh")