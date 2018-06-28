# -*-coding:utf-8-*-
"""文件压缩工具"""

import os
import tarfile
import zipfile


# 使用zip方式压缩文件，多用于windows系统
def zip_compress(source):
    # source:文件路径
    source = source.encode('utf-8').decode('UTF-8')
    target = source[0:source.rindex(".")] + '.zip'
    try:
        with zipfile.ZipFile(target, 'w') as zip_file:
            zip_file.write(source, source[source.rindex('/'):], zipfile.ZIP_DEFLATED)
            zip_file.close()
    except IOError as e:
        print('Compress file[%s] with zip model failed.Case:%s' % (source, e))
        target = source
    return target


# 使用tar方式压缩文件，多用于Linux系统
def tar_compress(source):
    source = source.encode('utf-8').decode('UTF-8')
    target = source[0:source.rindex(".")] + '.tar.gz'
    try:
        with tarfile.open(target, 'w:gz') as tar_file:
            tar_file.add(source, arcname=source[source.rindex("/"):])
    except IOError as e:
        print('Compress file[%s] with tar model failed.Case:%s' % (source, e))
        target = source
    return target


# 文件压缩率计算
def compress_rate(source_size, target_size):
    return round((source_size - target_size) / float(source_size), 4)


# 压缩文件
def compress_attachment(attachment):
    length = os.path.getsize(attachment)
    # 如果附件大于2个字节，就压缩文件；如1mb，即1*1024*1024*2
    if length > 2:
        zip_compress('file/text.txt')
        print('File [%s] compress rate is %s%%' % (
            os.path.basename(attachment), compress_rate(length, os.path.getsize(attachment)) * 100))


compress_attachment('file/text.txt')
