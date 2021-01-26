
import os,time
pi_date = time.strftime("%Y-%b-%d_%p-%H-%M", time.localtime())
pi_day = time.strftime("%Y-%b-%d", time.localtime())
test_time = time.strftime("%H-%M", time.localtime())
while 0!=1:
    pi_date = time.strftime("%Y-%b-%d_%p-%H-%M", time.localtime())
    test_time = time.strftime("%H-%M", time.localtime())
    
    if test_time==test_time:
        os.system("mkdir {}".format(pi_day))
        os.system("raspistill -o {}.jpg -t 5000".format(pi_date))
        break