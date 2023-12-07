import os
import random
import shutil
import csv
import numpy as np

def CopyFile(imageDir,test_rate,save_test_dir,save_train_dir):
	#imageDir:每个类别的所有图像在计算机中的位置
	#test_rate:copy的图片(测试集图片)数目所占总的比例
	#save_train_dir:移动的图片保存的位置
    image_number = len(imageDir)  #图片总数目
    test_number = int(image_number * test_rate)#要移动的图片数目(测试集图片)
    print("要移动到%s目录下的图片数目为:%d"%(save_test_dir,test_number))
    test_samples = random.sample(imageDir, test_number)#随机截取列表imageDir中数目为test_number的元素
    # copy图像到目标文件夹
    if not os.path.exists(save_test_dir):
        os.makedirs(save_test_dir)
        print("save_test_dir has been created successfully!")
    else:
        print("save_test_dir already exited!")
    if not os.path.exists(save_train_dir):
        os.makedirs(save_train_dir)
        print("save_train_dir has been created successfully!")
    else:
        print("save_train_dir already exited!")
    for i,j in enumerate(test_samples):
        shutil.copy(test_samples[i], save_test_dir+test_samples[i].split("/")[-1])
    print("test移动完成！")
    for train_imgs in imageDir:
        if train_imgs not in test_samples:
            shutil.copy(train_imgs, save_train_dir+train_imgs.split("/")[-1])
    print("train移动完成")#剩下的为训练集

#只需给定file_path、test_rate即可完成整个任务
#原始路径+分割比例
################################
file_path="D:/rice_bing/rice_disease/data"
test_rate = 0.3
################################
file_dirs=os.listdir(file_path)
origion_paths=[]
save_test_dirs=[]
save_train_dirs=[]
for path in file_dirs:
   origion_paths.append(file_path+"/"+path+"/")
   save_train_dirs.append("./train/"+path+"/")
   save_test_dirs.append("./test/"+path+"/")
for i,origion_path in enumerate(origion_paths):
    image_list = os.listdir(origion_path) #获得原始路径下的所有图片的name（默认路径下都是图片）
    image_Dir=[]
    for x,y in enumerate(image_list):
        image_Dir.append (os.path.join(origion_path, y))
    print("%s目录下共有%d张图片！"%(origion_path,len(image_Dir)))
    CopyFile(image_Dir,test_rate,save_test_dirs[i],save_train_dirs[i])
print("all datas has been moved successfully!")


