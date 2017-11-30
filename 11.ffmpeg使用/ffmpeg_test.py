 import os, subprocess
# 抽帧
def cut_one_piece():
    path = 'E:\juren buchong'

    output_file_path = 'E:\juren buchong'
    # files = os.listdir(path)

    # file_name = 'mgdm_mgAI_Origin_Video_1506689951_00000001.mp4'
    # subprocess.call(['ffmpeg', '-i', os.path.join(path, file_name), '-r', '1', '%04d.jpg'])

    files = os.listdir(path)
    for file in files:
        output_path = os.path.join(output_file_path, file[:-4])
        os.mkdir(output_path)
        os.chdir(output_path)

        output_file_name = file[:-4] + '_00_Preprocessing_20171106_%08d_00.jpg'

        subprocess.call(['ffmpeg', '-i', os.path.join(path, file), '-r', '1', output_file_name])    # 抽帧命令