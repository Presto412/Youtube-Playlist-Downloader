# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from urlretreiver import crawl
import os
from pprint import pprint
import requests
from bs4 import BeautifulSoup
def main():
    if not os.path.exists("Music Downloads"):
        os.mkdir("Music Downloads")

    playlist_url = raw_input("Enter the playlist URL here:")
    # url_list = crawl(playlist_url)
    url_list = crawl("https://www.youtube.com/playlist?list=PLsapGnWL6LQlaWaFvSzQ-3GmDxSWPq2RK")

    for url in url_list:
        mp3_url = "http://www.youtubeinmp3.com/download/?video=" + url
        main_url = "http://www.youtubeinmp3.com/"
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        }
        data = {
         "video" : url
        }
        dl_page = requests.get(mp3_url,params = data,verify = False )
        # print(dl_page.content)
        page_content = dl_page.content
        root = BeautifulSoup(page_content,"html.parser")
        link = main_url + root.find(id= "download")['href']

        dl = requests.get(link,verify=False,headers = headers)
        filename = dl.headers['Content-disposition'][21:].strip('"')

        with open(os.path.join("Music Downloads",filename),"w") as f:
            for chunk in dl:
                f.write(chunk)
        print "Downloaded :"+filename
main()
