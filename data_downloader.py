from datasets import load_dataset

# Load the ARC Easy dataset
dataset = load_dataset("ai2_arc", "ARC-Easy")

# Save the dataset in Arrow format
dataset.save_to_disk("data/arc_easy_dataset")
