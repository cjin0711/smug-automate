# SMUG-AUTOMATE

## What is smug-automate?
smug-automate is an automation tool for creating new galleries on the [SmugMug](https://www.smugmug.com/) platform.

This tool is powered by the Selenium Webdriver module.

Formats supported: `.heic, .heif, .jpg, .jpeg, .png, .gif, .3gp, .3g2, .3gp2, .avi, .h264, .m4v, .mov, .mp4, .mpeg, .mts, .ogg, .ogv, .qt, .webm, .wmv, image/heic, image/heif, image/jpeg, image/png, image/gif, video/3gpp, video/3gpp2, video/x-msvideo, video/h264, video/mp4, video/quicktime, video/mpeg, video/mp2t, video/ogg, video/webm, video/x-ms-wmv`

## Local Usage
Python should be installed onto your local system.

1. Clone the smug-automate repository into your chosen working directory.
```
git clone https://github.com/cjin0711/smug-automate.git
```

2. Install the Python Selenium package.
```
pip install selenium
```

3. Select browser for webdriver (defaulted to Brave browser). To use Chrome browser instead, delete or comment out in `smug.py`:
```
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
```

4. Make sure that all files to be uploaded are in your 'Downloads' directory.
```
e.g. C:\Users\cjin0\Downloads
```

5. Run `smug.py`.
```
py smug.py [arg1] [arg2(optional)]
```
* arg1 -> Name of the new gallery.
* arg2 -> How long ago (in minutes) you want files recently downloaded/modified to be uploaded to the gallery.
  - For example: Say the current time is 3:30pm. 
                 You want to upload two files you downloaded around half an hour prior (e.g. 3:03pm & 3:06pm).
                 You can run `py smug.py "New Gallery" 30` to encapsulate any file downloaded up to 30 minutes ago.
  - If arg2 is left blank, files downloaded/modified up to 5 minutes ago will be uploaded to the new gallery.

6. Enter your SmugMug login credentials.

## NOTE
* Do NOT download/modify files you do NOT plan on uploading right after downloading files that you DO plan on uploading 
  prior to gallery creation. This will lead to the incorrect files being uploaded to the gallery as well.
  - Correct ✓: download files for gallery -> run `smug.py` -> free to download other files
  - Incorrect ✗: download files for gallery -> download/modify irrelevant files -> run `smug.py`

## Next Step
* SmugMug browser extention that downloads selected files directly from the source (e.g. Email, Website)

