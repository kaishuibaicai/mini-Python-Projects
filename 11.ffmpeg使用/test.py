import so, subprocess
# 抽帧, 输入：原视频文件夹，输出目录，输出重命名记录
def cut_image(resource_path, output_file_path, output_record):
    record = open(output_record, 'w', encoding='utf-8')

    files = os.listdir(resource_path)
    index = 0
    for file in files:
        file_path = os.path.join(resource_path, file)
        if os.path.isdir(file_path):
            continue

        index += 1

        pre_file_name = 'mgdm_characterDetectionAI_Origin_Video_20171113_%08d_00' % index
        output_path = os.path.join(output_file_path, pre_file_name)

        record.write('%s\t%s\n' % (file, pre_file_name))

        os.mkdir(output_path)
        os.chdir(output_path)

        output_file_name = pre_file_name + '_Preprocessing_20171108_%08d_00.jpg'

        subprocess.call(['ffmpeg', '-i', file_path, '-r', '1', output_file_name])  # 抽帧命令
    record.close()

rp = 'E:\quanyecha\5\5'
op = 'E:\quanyecha\5\5'
rc = 'nameList'
cut_image(rp, op, rc)