from datasets import load_dataset

# List of datasets to download
datasets = [
    ("ai2_arc", "ARC-Easy", "arc_easy"),
    ("ai2_arc", "ARC-Challenge", "arc_challenge"),
    ("gsm8k", "main", "gsm8k"),
    ("cais/mmlu", "all", "cais_mmlu"),
    ("hellaswag", None, "hellaswag"),
    ("truthful_qa", "generation", "truthful_qa"),
    ("winogrande", "winogrande_xl", "winogrande")
]

for dataset_name, config, save_name in datasets:
    print(f"Downloading {dataset_name}...")
    if config:
        dataset = load_dataset(dataset_name, config)
    else:
        dataset = load_dataset(dataset_name)
    save_path = f"data/{save_name}"
    dataset.save_to_disk(save_path)
    print(f"Saved {dataset_name} to {save_path}")
