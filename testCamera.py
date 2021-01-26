import os,time
pic_folder_date = time.strftime("%Y-%b-%d", time.localtime())
os.system("mkdir {}".format(pic_folder_date))