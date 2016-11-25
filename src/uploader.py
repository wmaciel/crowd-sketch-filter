import os
from ftplib import FTP

def upload_images(img_path_list):
    uploaded_urls = []
    ftp = FTP(os.environ['FTP_SERVER'])
    ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASS'])
    ftp.cwd('pub_html')
    for img_path in img_path_list:
        img_name = os.path.basename(img_path)
        with open(img_path, 'rb') as img_file:
            ftp.storbinary('STOR ' + img_name, img_file)
        uploaded_urls.append(os.environ['FTP_URL'] + img_name)
    ftp.quit()
    return uploaded_urls
