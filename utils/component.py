# mass density unit is g/cm^3
import re


class Component:
    def __init__(self, component_str: str, mass_density:float):
        self.composition_str = component_str
        self.chemical_formula_list = re.findall(r'([A-Z][a-z]*)(\d*\.?\d*)', component_str)
        self.element_list=[]
        self.subscript_list=[]
        for item in self.chemical_formula_list:
            self.element_list.append(item[0].title())
            if item[1] == '':
                self.subscript_list.append(1)
            else:
                self.subscript_list.append(float(item[1]))
        self.mass_density = mass_density
    def get_composition_str(self):
        return self.composition_str
    def get_chemical_formula_list(self):
        return self.chemical_formula_list
    def get_element_list(self):
        return self.element_list
    def get_subscript_list(self):
        return self.subscript_list
    def get_mass_density(self):
        return self.mass_density
    def set_mass_density(self,new_mass_density:float):
        self.mass_density = new_mass_density

# if __name__ == "__main__":
#     component_str = "FeCo3O4Ca1.5F2"
#     print(Component(component_str).element_list)
#     print(Component(component_str).subscript_list)

