# train 中的各个类别在所有数据集的占比


all = {'Rice planthopper': 1511, 'Rice Leaf Roller': 1240, 'Striped rice bore': 1285, 'Armyworm': 8880, 'Bollworm': 28014,
       'Meadow borer': 16516, 'Athetis lepigone': 30339, 'Spodoptera litura': 1951, 'Spodoptera exigua': 7263, 'Stem borer': 1804,
       'Little Gecko': 4279, 'Plutella xylostella': 953, 'Spodoptera cabbage': 2304, 'Scotogramma trifolii Rottemberg': 4679,
       'Yellow tiger': 1686, 'Land tiger': 475, 'eight-character tiger': 168, 'holotrichia oblita': 108,
       'holotrichia parallela': 11675, 'Anomala corpulenta': 53347, 'Gryllotalpa orientalis': 6528, 'Nematode trench': 167,
       'Agriotes fuscicollis Miwa': 6484, 'Melahotus': 768}


train = {'Rice planthopper': 997, 'Rice Leaf Roller': 444, 'Striped rice bore': 378, 'Armyworm': 4443,
         'Bollworm': 13907, 'Meadow borer': 9873, 'Athetis lepigone': 17246, 'Spodoptera litura': 924,
         'Spodoptera exigua': 3163, 'Stem borer': 809, 'Little Gecko': 2492, 'Plutella xylostella': 554,
         'Spodoptera cabbage': 1058, 'Scotogramma trifolii Rottemberg': 2356, 'Yellow tiger': 853, 'Land tiger': 219,
         'eight-character tiger': 99, 'holotrichia oblita': 54, 'holotrichia parallela': 6216, 'Anomala corpulenta': 29735,
         'Gryllotalpa orientalis': 2921, 'Nematode trench': 100, 'Agriotes fuscicollis Miwa': 3203, 'Melahotus': 428}

mm = {}
for name in all.keys():
    mm[name] = train[name] / all[name]

print(mm)
print(len(mm))
for name in mm.keys():
    print(name + ": " + str(mm[name]))

