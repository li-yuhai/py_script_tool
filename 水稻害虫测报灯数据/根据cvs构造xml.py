headstr = """\
<annotation>
    <folder>VOC</folder>
    <filename>%s</filename>
    <source>
        <database>My Database</database>
        <annotation>COCO</annotation>
        <image>flickr</image>
        <flickrid>NULL</flickrid>
    </source>
    <owner>
        <flickrid>NULL</flickrid>
        <name>company</name>
    </owner>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>%d</depth>
    </size>
    <segmented>0</segmented>
"""

objstr = """\
    <object>
        <name>%s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%d</xmin>
            <ymin>%d</ymin>
            <xmax>%d</xmax>
            <ymax>%d</ymax>
        </bndbox>
    </object>
"""

tailstr = '''\
</annotation>
'''
width = 5472
height = 3648
depth = 3

# 行数据结构体
class Ds:
    def __init__(self, name ,xmin, ymin, xmax, ymax):
        self.name = name
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

# ds = Ds(name='Bob', xmin=1, ymin=2, xmax=2, ymax=3)

# map结构
# my_map = {
#     1: set(),
#     2: set(),
#     3: set()
# }

# 字符串模板拼接
# headstr  = headstr % ('1',1,2,3)
# print(headstr)
#

# key:文件名 val：set()集合
data_map = { }

# 序号,文件名(1),虫子编号(2),虫子名称,中心点x坐标,中心点y坐标,左上角x坐标(6),左上角y坐标(7),右下角x坐标(8),右下角y坐标(9)

import csv

# CSV文件路径
csv_file_path = 'selected_data.csv'

# 打开CSV文件
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    # 创建CSV读取器, 跳过首行
    csv_reader = csv.reader(csvfile, skipinitialspace=True)
    next(csv_reader)  # 跳过标题行
    # 遍历每一行数据
    for row in csv_reader:
        # row 是一个列表，包含了当前行的所有字段
        # print(row[1], row[2])
        ds = Ds(name=row[2], xmin=row[6], ymin=row[9], xmax=row[8], ymax=row[7])
        sset = None
        if row[1] not in data_map.keys():
            data_map[row[1]] = set()
        sset = data_map[row[1]]
        sset.add(ds)
        print(ds.xmin, ds.ymin, ds.xmin, ds.xmax)


for name, ss in data_map.items():
    xml_h = headstr % (name, width, height, 3)
    xml_o = ''
    for obj in ss:
        os = objstr % (obj.name, int(float(obj.xmin)), int(float(obj.ymin)), int(float(obj.xmax)), int(float(obj.ymax)))
        xml_o += os
    xml_str = xml_h + xml_o + tailstr

    # 将字符串写入到 XML 文件
    with open(name.split('.')[0] + ".xml" , "w", encoding="utf-8") as file:
        file.write(xml_str)


