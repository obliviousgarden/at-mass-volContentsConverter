# 目的是从str中解析出物质的组分，并包含组分中元素的含量
from utils.component import Component
from utils.element import Element
from utils.common_components import CommonComponentTool
from utils.common_elements_NIST import search_atomic_mass


def split_substance_and_media(common_component_tool:CommonComponentTool,substance_str: str, media_str: str):
    # 1 在common component中匹配
    # 2-A 如果找到了 输出既有的component_list和mass_density_list
    # 2-B 如果没找到 那么输出重新构造的component_list和mass_density_list
    substance_component = common_component_tool.get_common_component(substance_str)
    media_component = common_component_tool.get_common_component(media_str)
    if substance_component is None:
        substance_component = Component(substance_str, 1.0)
    if media_component is None:
        media_component = Component(media_str, 1.0)
    component_list = [substance_component, media_component]
    # 3 遍历 component，获取element_list
    element_str_list = []
    for component in component_list:
        element_str_list.extend(component.get_element_list())
    element_str_list = list(set(element_str_list))
    element_list = []
    for element_str in element_str_list:
        element_list.append(Element(element_str, search_atomic_mass(element_str)))
    # 4 返回2个list
    return component_list, element_list
