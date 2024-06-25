#!/usr/bin/env python3

import os, random

home = os.enviorn.get('XDG_CACHE_HOME')

if len(os.listdir(f"{home}/current")) == 0:
    if len(os.listdir(f"{home}/todo/")) == 0:
        os.rename(f"{home}/todo/", f"{home}/temp")
        os.rename(f"{home}/done/", f"{home}/todo/")
        os.rename(f"{home}/temp", f"{home}/done/")
    f = random.choice(os.listdir(f"{home}/todo/"))
    os.rename(f"{home}/todo/" + f , f"{home}/current/0.txt")

# commit_msg_filepath = sys.argv[1]
count = int(os.listdir(f"{home}/current")[0].split('.')[0]) + 1
with open(f"{home}/current/" + os.listdir(f"{home}/current")[0], "r") as f:
    temp =""
    lines = f.readlines()
    for x in range(count):
        temp += lines[x]
    print(temp)
    # with open(commit_msg_filepath, 'w') as send:
    #     send.write(temp)
    if count == len(lines):
        os.rename(f"{home}/current/" + str(count - 1) + ".txt" , f"{home}/done/"+ str(len(os.listdir(f"{home}/done/")))+".txt")
    else:
        os.rename(f"{home}/current/" + str(count - 1)+ ".txt" , f"{home}/current/" + str(count)+ ".txt")