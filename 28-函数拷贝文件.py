import sys
def copy(src_fname,dst_fname):
    src_fobj = open(src_fname,'rb')  # 以读写的方式打开
    dst_fobj = open(dst_fname,'wb')  # 以写入的方式打开
    
    while True:
        data = src_fobj.read(4096)
        if not data:  # 如果data为空
            break
        dst_fobj.write(data)

    src_fobj.close()
    dst_fobj.close()

# 创建实例
copy(sys.argv[1],sys.argv[2])
