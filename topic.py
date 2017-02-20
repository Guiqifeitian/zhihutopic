#-*- coding:utf-8 -*-

from selenium import webdriver
import time
import os

def mlogin():
    profile_dir = r"C:\Users\tuobashao\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))

    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get("http://www.zhihu.com/topic/20011767/followers")

    js1 = "var q=document.body.scrollTop=100000"
    js2 = """
        (function () {
            var y = document.body.scrollTop;
            var step = 100;
            window.scroll(0, y);


            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 50);
                }
                else {
                    window.scroll(0, y);
                    document.title += "scroll-done";
                }
            }


            setTimeout(f, 1000);
        })();
        """
    js3 = """
            (function(){
                var button = document.getElementById("zh-load-more")
                button.click()
            })();
        """


    # 20个循环，900人
    # 40个循环，2100人
    # 50个循环，2700人
    # 55个循环，2860
    for i in range(1):

        browser.execute_script(js2)
        time.sleep(2)

        #a标签一定要用js脚本去点击！！！
        browser.execute_script(js3)
        time.sleep(2)


    browser.execute_script(js2)

    time.sleep(2)
    #browser.close()

    names = browser.find_elements_by_css_selector('.zg-link.author-link')
    rank = 0
    with open('followersT.txt','w') as f:
        f.write('total followers of this subject is '+str(len(names))+'\n')
        for each in names:
            rank += 1
            #print each.text,each.get_attribute('href'),rank
            print each.text
            f.write(each.text.encode('gbk')+','+each.get_attribute('href')+'\n')

def main():
    mlogin()

if __name__ == '__main__':
    main()