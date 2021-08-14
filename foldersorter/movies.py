import os
import re
import shutil

sortdir = "C:\\Downloads\\plzno\\"

#store contents to sort
filenames = os.listdir(sortdir)
suffix = "mkv"

for each_file in filenames:
    if (suffix in each_file) and ("." in each_file):
        newname = each_file.split(".")
        newname[-1] = newname[-1].replace(suffix, "." + suffix) # replace suffix - 1 

        # parse full episode id from newname
        for words in newname:
            if (re.search("S..E..", words)) != None: full_ep_id = newname[newname.index(words)]
            else: continue

        season_id = full_ep_id[0:len(full_ep_id)-3] # season ID assumes first three character format
        episode_id = full_ep_id[len(full_ep_id)-3:len(full_ep_id)] #episode id assumes last three character format

        # everything before the episode ID is considered the show name, and merged into a single string
        showname_temp = newname[0:newname.index(full_ep_id)] 
        showname = ""
        for words in showname_temp:
            showname += words + " "
        
        if "." not in suffix: suffix = "." + suffix # workaround for some weird glitch where suffix gets more and more dots concat on the end for each file

        full_filename = showname + full_ep_id + suffix

        print("Show name:", showname)
        print("Episode ID: ", full_ep_id)
        print("Suffix:", suffix)
        print("Fixed name:", full_filename)
        
        season_folder = season_id.replace("S","Season ")
        print(season_folder)

        os.rename(sortdir + each_file, sortdir + full_filename)
        sorted_path = sortdir + showname.strip() + "\\"

        #strip endings off folder names to prevent making invalid folders!
        season_folder = season_folder.strip()
        full_filename = full_filename.strip()
        sorted_path = sorted_path.strip()
        each_file = each_file.strip()
        if not os.path.isdir(sorted_path): os.mkdir(sorted_path)
        sorted_path = sorted_path + season_folder + "\\"
        if not os.path.isdir(sorted_path): os.mkdir(sorted_path)

        shutil.move(sortdir + full_filename, sorted_path + full_filename)
