import json
import os,sys
import shutil
from utils.component import Component

#
# Co = Component('Co', 8.9)
# Fe = Component('Fe', 7.874)
# CoFe = Component('CoFe', 8.63)
# SrF2 = Component('SrF2', 4.24)
# MgF2 = Component('MgF2', 3.15)
# BaF2 = Component('BaF2', 4.89)
# Al2O3 = Component('Al2O3', 3.95)
# SiO2 = Component('SiO2', 2.65)
# Ta2O5 = Component('Ta2O5', 8.2)
# AlF3 = Component('AlF3', 2.88)


class CommonComponentTool:
    __common_component_dict = {}
    __base_path = ''
    __user_data_dir = ''
    __json_file_path = ''

    def __init__(self,user_data_dir):
        self.__user_data_dir = user_data_dir
        if getattr(sys, 'frozen', False):
            # Running as compiled exe
            self.__base_path = sys._MEIPASS
        else:
            # Running as script
            self.__base_path = os.path.dirname(__file__)
        if self.__common_component_dict == {}:
            # list 是空的话，那么需要从json文件初始化json
            self.__json_file_path = os.path.join(user_data_dir, "common_component.json")
            if os.path.exists(self.__json_file_path) is False:
                # 如果不存在，那么把__base_path路径下的文件复制到响应路径
                shutil.copy(os.path.join(self.__base_path,'common_component.json'), self.__user_data_dir)
            with open(self.__json_file_path, 'r') as json_file:
                self.__common_component_dict = json.load(json_file)
            print('CommonComponentInit:', json.dumps(self.__common_component_dict, indent=4))
        print('__base_path',self.__base_path)
        print('__user_data_dir',self.__user_data_dir)
        print('__json_file_path',self.__json_file_path)

    def get_common_component(self, component_str: str) -> Component:
        if component_str in self.__common_component_dict:
            key = component_str
            value = float(self.__common_component_dict[component_str])
            print('Get Common Component:', key, '\t', value, 'g/cm^3')
            return Component(key, value)
        else:
            return None

    def get_all_common_component(self):
        return self.__common_component_dict

    def update_json(self):
        with open(self.__json_file_path, 'w') as json_file:
            json.dump(self.__common_component_dict, json_file)

    def add_common_component(self, component_str: str, mass_density: float):
        # Add new common component to JSON file
        self.__common_component_dict[component_str] = mass_density
        print('Add Common Component:', component_str, '\t', mass_density, 'g/cm^3')
        self.update_json()

    def delete_common_component(self, component_str: str):
        if component_str in self.__common_component_dict:
            del self.__common_component_dict[component_str]
        self.update_json()

#
# def get_common_component(component_str: str) -> Component:
#     if component_str == Co.get_composition_str():
#         return Co
#     elif component_str == Fe.get_composition_str():
#         return Fe
#     elif component_str == CoFe.get_composition_str():
#         return CoFe
#     elif component_str == SrF2.get_composition_str():
#         return SrF2
#     elif component_str == MgF2.get_composition_str():
#         return MgF2
#     elif component_str == BaF2.get_composition_str():
#         return BaF2
#     elif component_str == Al2O3.get_composition_str():
#         return Al2O3
#     elif component_str == SiO2.get_composition_str():
#         return SiO2
#     elif component_str == Ta2O5.get_composition_str():
#         return Ta2O5
#     elif component_str == AlF3.get_composition_str():
#         return AlF3
#     else:
#         return None


if __name__ == "__main__":
    tool = CommonComponentTool()
    tool.get_common_component('SrF2')
    tool.add_common_component('AAA', 12.3456)
# def get_common_component(component_str:str)->Component:
#     variables, functions, parameters = analyze_file(__file__)
#     if component_str in variables:
#         component = globals().get(component_str)
#         print('Common component found:'+component.get_composition_str()+',\t'+str(component.get_mass_density())+'g/cm^3')
#         return component
#     else:
#         print('Common component not found.')
#         return None

# if __name__ == "__main__":
#     variables, functions, parameters = analyze_file(__file__)
#
#     print("Variables:", variables)
#     print("Functions:", functions)
#     print("Parameters:", parameters)
#
#     component = get_common_component('SrF3')
#     print(component==None)
