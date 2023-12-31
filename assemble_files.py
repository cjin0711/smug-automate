import os, time

#double slash to avoid unicode error
directory = "C:\\Users\\cjin0\\Downloads"

files = []

#finds interval between current time and file modification time(in secs)
def check_recent(mod_time):
    return time.time() - mod_time

def assemble(elapsed_time):
    #iterate through directory
    for file in os.listdir(directory):

        file_path = f"{directory}\\{file}"

        #makes sure image files fit correct format
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            time_interval = check_recent(os.path.getmtime(file_path))

            #checks if file was downloaded recently
            if time_interval < elapsed_time:
                files.append(file_path)

    #resolution to duplicate file upload
    return '\n'.join(files)







        

        
