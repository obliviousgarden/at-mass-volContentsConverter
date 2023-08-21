from utils.analyze_file import analyze_file

from utils.component import Component
Co = Component('Co',8.9)
Fe = Component('Fe',7.874)
SrF2 = Component('SrF2',4.24)
MgF2 = Component('MgF2',3.15)
Al2O3 = Component('Al2O3',3.95)
AlF3 = Component('AlF3',2.88)

def get_common_component(component_str:str)->Component:
    if component_str == Co.get_composition_str():
        return Co
    elif component_str == Fe.get_composition_str():
        return Fe
    elif component_str == SrF2.get_composition_str():
        return SrF2
    elif component_str == MgF2.get_composition_str():
        return MgF2
    elif component_str == Al2O3.get_composition_str():
        return Al2O3
    elif component_str == AlF3.get_composition_str():
        return AlF3
    else:
        return None

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