class Element:
    def __init__(self,element_str:str,atomic_mass:float):
        self.element_str = element_str.title() #首字母大写
        self.atomic_mass = atomic_mass
    def get_element_str(self)->str:
        return self.element_str
    def get_atomic_mass(self)->float:
        return self.atomic_mass
    def set_atomic_mass(self,new_atomic_mass:float):
        self.atomic_mass = new_atomic_mass