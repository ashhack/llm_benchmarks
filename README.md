# LLM Benchmarks

This repository contains scripts and data for benchmarking Large Language Models (LLMs) on various tasks.

## Datasets

### ARC Easy Dataset
The ARC Easy dataset is a collection of multiple-choice science questions designed for elementary and middle school students. It consists of questions from various science topics.

- **Source**: AI2 ARC (AI2 Reasoning Challenge) - Easy subset
- **Hugging Face Dataset**: [ai2_arc](https://huggingface.co/datasets/ai2_arc)
- **Format**: Multiple-choice questions with 4 options (A-D)
- **Splits**: Train, Validation, Test

#### Sample Question
**Question:** Which factor will most likely cause a person to develop a fever?  
**Options:**  
- A: a leg muscle relaxing after exercise  
- B: a bacterial population in the bloodstream  
- C: several viral particles on the skin  
- D: carbohydrates being digested in the stomach  
**Correct Answer:** B

## Setup

1. Install required dependencies:
   ```bash
   pip install datasets
   ```

2. Run the data downloader:
   ```bash
   python data_downloader.py
   ```

This will download the ARC Easy dataset and save it to the `data/arc_easy_dataset/` directory in Arrow format.

## Usage

To load and explore the dataset:

```python
from datasets import load_from_disk

# Load the dataset
dataset = load_from_disk('data/arc_easy_dataset')

# Access splits
train_data = dataset['train']
val_data = dataset['validation']
test_data = dataset['test']

# Example: Print first sample
print(train_data[0])
```

## Files

- `data_downloader.py`: Script to download and save the ARC Easy dataset
- `data/`: Directory containing downloaded datasets
  - `arc_easy_dataset/`: ARC Easy dataset in Hugging Face format
  - `arc_easy_dataset.zip`: Zipped version of the dataset
- `README.md`: This file

## License

The ARC dataset is provided by AI2 and follows their licensing terms. Please refer to the original dataset for licensing information.