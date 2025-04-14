from datasets import load_dataset

# This loads the full dataset (can also use split="train[:100]" to get only 100 rows)
dataset = load_dataset("GeorgiaTech/cnotesum", split="train[:1058]")

# Convert to lists
clinical_notes = dataset["clinical_notes"]
summaries = dataset["summary"]
