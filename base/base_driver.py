from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = 'S003380000161'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 增加可输入中文的参数配置
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 启动时不清除应用信息
    desired_caps['noReset'] = True
    # 实例化手机
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)