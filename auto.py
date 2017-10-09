from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
import re


class AutoSeeVedio(object):

    def __init__(self, user, pwd):
        super(AutoSeeVedio, self).__init__()
        self.user = user                # 用户名
        self.pwd = pwd                  # 用户密码

        self.pattern = re.compile(r'\d{2}:\d{2}:\d{2}')  # 获取时间的正则

        self.startAuto()                # 开始自动看视频

    def startAuto(self):
        self.driver = webdriver.Chrome()                    # 打开谷歌浏览器
        self.driver.get(url='http://www.zhihuishu.com/')    # 打开智慧树网站

        # 模拟登录
        self.driver.find_element_by_xpath(
            '//*[@id="login-register"]/li[1]/a').click()  # 点登录
        self.driver.find_element_by_xpath(
            '//*[@id="lUsername"]').send_keys(self.user)  # 输用户名
        self.driver.find_element_by_xpath(
            '//*[@id="lPassword"]').send_keys(self.pwd)  # 输密码
        self.driver.find_element_by_xpath(
            '//*[@id="f_sign_up"]/div/span').click()     # 点登录
        time.sleep(1)

        # 点继续学习
        self.driver.find_element_by_xpath(
            '//*[@id="course_recruit_studying_ul"]/li[1]/div[2]/div[2]/a').click()
        time.sleep(3)
        # 切换窗口句柄
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(1)
        # 关掉提示
        self.driver.find_element_by_class_name('popbtn_yes').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="j-assess-criteria_popup"]/span[2]').click()
        time.sleep(1)

        # 获取当前视频播放时间长度
        lastTime = self.driver.find_element_by_css_selector(
            '.clearfix.video.children.current_play').text
        lastTime = self.pattern.findall(lastTime)[0].split(':')  # 读取视频播放的时间
        # 将时间转换成秒，
        # 并加多15秒，给长一点时间保证视频完全看完
        lastTime = int(lastTime[1]) * 60 + \
            int(lastTime[2]) + 15     

        start = datetime.now()           # 获取开始看视频的时间
        while True:
            end = datetime.now()         # 获取当前时间
            if (end - start).seconds > lastTime:
                # 计算时间是否已经看够了，看够了就跳下一个视频
                start = datetime.now()
                self.driver.find_element_by_xpath(
                    '/html/body/div[3]/div[5]/div/div[5]/div').click()
            try:
                # 监听弹窗，弹出来就点关闭，没有就继续监听
                self.driver.find_element_by_class_name('popbtn_cancel').click()
            except:
                pass

if __name__ == '__main__':
    me = AutoSeeVedio(user='yourUserName', pwd='yourPassword') # 你的用户名和密码
    me.startAuto()
