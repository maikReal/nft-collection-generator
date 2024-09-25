class Config:

    def __init__(self, root_folder_name):
            self.root_folder_name = root_folder_name
            self.addresses_number = None

            self.legend_img_path = f'{self.root_folder_name}/legend.png'
            self.super_rare_img_path = f'{self.root_folder_name}/super_rare.png'
            self.rare_img_path = f'{self.root_folder_name}/rare.png'
            self.regular_img_path = f'{self.root_folder_name}/regular.png'

            self.user_data_path = f'{self.root_folder_name}/user_data.txt'

            self.legend_type_size = 0.05 # 5%
            self.super_rare_type_size = 0.10 # 10%
            self.rare_type_size = 0.20 # 20%
            self.regular_type_size = 0.65 # 65%

            self.rarity_distribution_config = None

    
    def set_addresses_number(self, number):
          self.addresses_number = number

          self.define_rarity_distribution_dict()

    def define_rarity_distribution_dict(self):
          self.rarity_distribution_config = {
                "legend": {
                    "path": self.legend_img_path,
                    "count": self.addresses_number * self.legend_type_size, 
                    "folder": f"{self.root_folder_name}/collection/Legend"
                },
                "super_rare": {
                    "path": self.super_rare_img_path, 
                    "count": self.addresses_number * self.super_rare_type_size, 
                    "folder": f"{self.root_folder_name}/collection/Super_Rare"
                },
                "rare": {
                    "path": self.rare_img_path, 
                    "count": self.addresses_number * self.rare_type_size, 
                    "folder": f"{self.root_folder_name}/collection/Rare"
                },
                "regular": {
                    "path": self.regular_img_path, 
                    "count": self.addresses_number * self.regular_type_size, 
                    "folder": f"{self.root_folder_name}/collection/Regular"
                }
            }