import os, time
from pathlib import Path

#locates user 'Downloads' directory
path = str(os.path.join(Path.home(), "Downloads"))
raw_path = path.replace("\\",'/')

files = []

#finds interval between current time and file modification time(in secs)
def check_recent(mod_time):
    return time.time() - mod_time

def assemble(elapsed_time):

    #accepted file formats
    str_form = '.heic,.heif,.jpg,.jpeg,.png,.gif,.3gp,.3g2,.3gp2,.avi,.h264,.m4v,.mov,.mp4,.mpeg,.mts,.ogg,.ogv,.qt,.webm,.wmv,image/heic,image/heif,image/jpeg,image/png,image/gif,video/3gpp,video/3gpp2,video/x-msvideo,video/h264,video/mp4,video/quicktime,video/mpeg,video/mp2t,video/ogg,video/webm,video/x-ms-wmv'
    accepted_formats = str_form.split(',')

    #iterate through directory
    for file in os.listdir(raw_path):

        file_path = f"{raw_path}/{file}"
        
        #makes sure image files fit correct format
        if file.endswith(tuple(accepted_formats)):
            time_interval = check_recent(os.path.getmtime(file_path))

            #checks if file was downloaded recently
            if time_interval < elapsed_time:
                files.append(file_path)

    if not files:
        raise Exception("No files found.")
    
    #resolution to duplicate file upload
    return '\n'.join(files)

