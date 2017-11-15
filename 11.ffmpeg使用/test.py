# -*- coding: utf-8 -*-
import os, subprocess
# 抽帧, 输入：原视频文件夹，输出目录，输出重命名记录
def cut_image(resource_path, output_file_path, output_record):

    files = os.listdir(resource_path)
    index = 0
    for file in files:
        file_path = os.path.join(resource_path, file)
        if os.path.isdir(file_path):
            continue

        index += 1

        pre_file_name = 'mgdm_characterDetectionAI_Origin_Video_20171115_%08d_00' % index
        output_path = os.path.join(output_file_path, pre_file_name)
        with open("C:\Users\Administrator\Desktop\missions\huoying\Preprocessing\Preprocessing\Image\huoyingthename.txt", 'a+') as s:
            s.write('%s\t%s\n' % (file, pre_file_name))
        record.write('%s\t%s\n' % (file, pre_file_name))

        os.mkdir(output_path)
        os.chdir(output_path)

        output_file_name = pre_file_name + '_Preprocessing_20171115_%08d_00.jpg'

        subprocess.call(['ffmpeg', '-i', file_path, '-r', '1', output_file_name])  # 抽帧命令
 
rp = 'E:\huoying-new2'
op = 'E:\huoying-new2'
rc = 'nameList'
cut_image(rp, op, rc)