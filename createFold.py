import os,time
pic_name = time.strftime("%Y-%b-%d_%p-%H-%M", time.localtime())
os.system("raspistill -o {}.jpg -t 5000".format(pic_name))