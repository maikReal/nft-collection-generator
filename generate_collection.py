import pandas as pd
import os
import shutil
import json
from collection_config import Config


def prepare_images_and_metadata(campaign_name, rarity_distribution_config):

    # Ensure base directory exists for each rarity
    for rarity, info in rarity_distribution_config.items():
        os.makedirs(info['folder'], exist_ok=True)

    # Start naming files from 1
    image_counter = 1

    # Process each rarity
    for rarity, info in rarity_distribution_config.items():
        for i in range(int(info['count'])):
            # Generate new file names
            image_filename = f"{image_counter}.jpg"
            image_dest_path = os.path.join(info['folder'], image_filename)

            # Copy image to the target folder
            shutil.copy(info['path'], image_dest_path)

            # Create JSON metadata file
            metadata = {
                "attributes": {
                    "rarity": rarity,
                    "campaign": campaign_name
                }
            }
            metadata_filename = f"{image_counter}.json"
            metadata_path = os.path.join(info['folder'], metadata_filename)
            with open(metadata_path, 'w') as json_file:
                json.dump(metadata, json_file, indent=4)

            # Increment image counter
            image_counter += 1

    print(f"Images and metadata files created successfully for the {campaign_name} campaign!")


if __name__ == '__main__':

    campaign_name = input('Enter the name of a folder with images and users data: ')

    if campaign_name: 

        collection_config = Config(campaign_name)


        df = pd.read_csv(collection_config.user_data_path, header=None)
        print('Folder is processing: ', campaign_name)
        
        size_with_duplicates = df.size
        print('Total addresses found: ', size_with_duplicates)

        size_without_duplicates = df.drop_duplicates().size
        print('Total unique addresses found: ', size_without_duplicates)
        
        # result = calculate_nft_distribution(size_without_duplicates)
        # print('Number of NFTs per rarity level: ', result)
        print('<--------->')
        print()


        collection_config.set_addresses_number(size_without_duplicates)

        prepare_images_and_metadata(
            campaign_name=campaign_name,
            rarity_distribution_config=collection_config.rarity_distribution_config
        )

    else: 

        raise Exception('[ERROR] No folder name was provided...')

    