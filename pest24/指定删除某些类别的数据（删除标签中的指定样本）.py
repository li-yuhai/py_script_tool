
import xml.etree.ElementTree as ET
import  os

# pest24_names =  {
#         'Rice planthopper': 1,  'Rice Leaf Roller': 2, 'Striped rice bore':3,  'Armyworm': 5,  'Bollworm' : 6,
#         'Meadow borer': 7,  'Athetis lepigone': 8, 'Spodoptera litura': 10,   'Spodoptera exigua': 11,
#         'Stem borer':12,  'Little Gecko': 13,  'Plutella xylostella': 14, 'Spodoptera cabbage': 15,
#         'Scotogramma trifolii Rottemberg': 16,  'Yellow tiger': 24, 'Land tiger': 25,  'eight-character tiger': 28,
#          'holotrichia oblita':29,  'holotrichia parallela': 31,   'Anomala corpulenta': 32, 'Gryllotalpa orientalis': 34,
#         'Nematode trench': 35, 'Agriotes fuscicollis Miwa': 36, 'Melahotus': 37
#
# }

# 1，14，28，29，35，37

# 要删除的对象名称列表
# objects_to_remove_names = ['Rice planthopper', 'Plutella xylostella', 'eight-character tiger', 'holotrichia oblita', 'Nematode trench', 'Melahotus']

objects_to_remove_names = ["Plutella xylostella", "Rice planthopper", "eight-character tiger"]

anno_path = 'D:/lxl_suining_cqcb/Pest24/Annotations/'
output = os.getcwd() + '/out/'
files = os.listdir(anno_path)
for file in files:
    xml_file_path = anno_path + file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    # 在这里添加你要删除的XML元素的逻辑
    # 例如，删除所有名为 "Bollworm" 的 <object> 元素
    # 遍历XML树，删除符合条件的<object>元素
    for object_to_remove_name in objects_to_remove_names:
        objects_to_remove = root.findall(f".//object[name='{object_to_remove_name}']")

        for object_to_remove in objects_to_remove:
            # 删除 <object> 元素
            root.remove(object_to_remove)

    # 保存修改后的XML文件
    tree.write(output + file)













