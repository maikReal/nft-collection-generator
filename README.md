# NFT collection generator

The basic script that can generate all necessary metadata and images divided by 4 rarity levels

## Requirements

1. Create a folder in the root with the following data:
   - Add 4 different images of different rarity levels. Check example in the 'test' folder
   - Add a user_data.txt or user_data.csv file with the list of addresses for a particular collection. Check example in the 'test' folder
2. Modify the percentage of different raritry level per image in the collection_config.py file

## Setup

1. Install requirements

```bash
pip install -r requirements.txt
```

2. Laucnh a script

```bash
python generate_collection.py
```

3. Enter the folder name with all data, e.g. 'test_campaign'
4. Get the result in the provided folder. A new folder will be called 'collection'
