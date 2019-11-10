from datetime import datetime as dt
import time

while True:
    website_list = ['www.facebook.com' , 'facebook.com' , 'twitter.com' , 'www.twitter.com' , 'www.instagram.com' , 'www.youtube.com']
    #path_to_host = "C:\Windows\System32\drivers\etc\hosts
    path_to_host = "D:\\hosts"
    redirect_url = "127.0.0.1"

    time_now = dt.now().hour
    if (time_now <= 8 or time_now>= 18):
        print('fun hour')
        with open(path_to_host , 'r+') as file:
            contents = file.readlines()
            file.seek(0)
            for line in contents:
                if not any (website in line for website in website_list):
                    file.write(line)
                file.truncate()
    else:
        print('working hours !')
        with open(path_to_host, 'r+') as file:
            contents = file.read()
            # print(contents)
            for web in website_list :
                if web in contents:
                    pass
                else:
                    file.write("\n" + redirect_url + "  " + web + "\n")
    time.sleep(5)


