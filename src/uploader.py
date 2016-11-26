import os
from ftplib import FTP


def empty_this_directory(ftp):
    files_in_dir = ftp.nlst()
    for f in files_in_dir:
        ftp.delete(f)


def create_empty_directory(ftp, dir_name):
    file_list = ftp.nlst()
    if dir_name in file_list:
        ftp.cwd(dir_name)
        empty_this_directory(ftp)
        ftp.cwd('..')
    else:
        ftp.mkd(dir_name)


def upload_images(img_path_list, folder_name):
    uploaded_urls = []

    print 'Connecting to ftp server...'
    ftp = FTP(os.environ['FTP_SERVER'])
    ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASS'])
    ftp.cwd('pub_html')

    print 'Preparing directory on ftp server...'
    if folder_name and folder_name != '.':
        create_empty_directory(ftp, folder_name)
        ftp.cwd(folder_name)
    else:
        empty_this_directory()

    print 'Uploading images to ftp server...'
    for img_path in img_path_list:
        img_name = os.path.basename(img_path)
        with open(img_path, 'rb') as img_file:
            ftp.storbinary('STOR ' + img_name, img_file)
        uploaded_urls.append(os.environ['FTP_URL'] + folder_name + '/' + img_name)

    print 'Closing connection with ftp server...'
    ftp.quit()

    return uploaded_urls
