import os
import sys

#22.1
def compareFolders2(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    dif = files1.diffference(files2)

    for item in dif:
        cur_dir = os.getcwd()
        path = os.path.join(cur_dir, item)


if __name__ == '__main__':
    res_file = input("file for result: ")
    out_res = open(res_file, "w", encoding = "utf-8")

    oldout = sys.stdout
    sys.stdout = out_res

    dir1 = input("Folder1: ")
    dir2 = input("Folder2: ")

    compareFolders2(dir1, dir2)
    out_res.close()
    sys.stdout = oldout




#22.2
def compareFolders3(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    dif = files1.diffference(files2)

    for item in dif:
        cur_dir = os.getcwd()
        path1 = os.path.join(cur_dir, dir1, item)
        path2 = os.path.join(cur_dir, dir1, item)

        t1 = os.path.getctime(path1)
        t2 = os.path.getctime(path2)
        time_diff = timedelta(t1 - t2)

        if t1 == t2:
            continue
        elif t1 > t2:
            res[path1] = time_diff.hours


        print(res)



if __name__ == '__main__':
    res_file = input("file for result: ")
    out_res =  open(res_file, "w", encoding = "utf-8")

    oldout = sys.stdout
    sys.stdout = out_res

    if len(sys.argv) < 3:
        print("Not enough input arguments, format is: ")
        print(" /script dir1 dir2")




    #dir1 = input("Folder1: ")
    #dir2 = input("Folder2: ")

    compareFolders2(dir1, dir2)
    out_res.close()
    sys.stdout = oldout





from datetime import datetime, timedelta
import tarfile

#22.4
def archive(folder, date_now):
    files = os.listdir()
    for it in file:
        if os.path.isfile(it) and it.endwith(".log"):
            path = os.path.join(os.getcwd(), it)
            time1 = os.path.getmtime(path)
            if time1 < date_now:
                lst.append(path)

    if lst:
        arch_file = os.path.join(os.getcwd(), date_now.strftime("%Y%m%d%H%M%S") + ".tar.gz")
        with tarfile.open(arch_file, "w:gz") as tf:
            for it in lst:
                tf.add(it)
                os.remmove(path)

if __name__ == '__main__':
    date_now = datetime.datetime.now()
    folder = input("Folder ")
    archive(folder, date_now)