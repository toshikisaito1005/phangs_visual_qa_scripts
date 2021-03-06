import os
import sys
import glob

dir_data = glob.glob("../science_*/group.*/member.*/")
dir_current = os.getcwd()

for i in range(len(dir_data)):
    os.chdir(dir_data[i])
    done = glob.glob("calibrated/")
    if not done:
        print("run : " + dir_data[i].split("/")[1] + " " \
              + str(i) + "/" + str(len(dir_data)))
        os.chdir("script")
        execfile(glob.glob("*scriptForPI.py")[0])
    else:
        print("skip: " + dir_data[i].split("/")[1] + " " \
              + str(i) + "/" + str(len(dir_data)))
    os.chdir(dir_current)


