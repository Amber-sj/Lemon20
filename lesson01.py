



from selenium import webdriver
import time

#等待方式
#time sleep()  ----强制等待时间
#元素定位
#元素定位：一获取页面元素，进行接下来的操作，例如输入，点击等。---重点


# #启动浏览器
# driver = webdriver.Firefox()
# driver.get("http://erp.lemfix.com/login.html")
# time.sleep(2)
# # driver.get("http://www.baidu.com")
#
# #通过执行js，新开一个窗口
# js = "window.oprn('http://www.baidu.com')"
# driver.execute_script(js)


#
# #浏览器窗口最大化
# driver.maximize_window()
#
#
# #后退、前进、刷新页面
# time.sleep(2)
# driver.back()   #返回上一页面
# time.sleep(2)
# driver.forward()  #前进到下一页面
# time.sleep(2)
# driver.refresh()   #刷新页面

#关闭浏览器
# driver.close()
# driver.quit（）

#用例1，打开erp网站
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://erp.lemfix.com/login.html")
driver.maximize_window()


#用例2
#输入正确的用户和密码能正常登录，点击登录
username = driver.find_element_by_id('username').send_keys('13916686542')
username = driver.find_element_by_id('password').send_keys('lemon123')
username = driver.find_element_by_id('btnSubmit').click()

#用例3
#判断正常登录，登录成功

login_user = driver.find_element_by_xpath('//p').text   #获取登录后的用户信息
# login_user = driver.find_element_by_xpath(''//div[@class='pull-left.info']/p'').text
if login_user == '13916686542':
    print('这个登录用户名是：{}'.format(login_user))
else:
    print('这个登录用户名不正确')
#用例4：点击零售出库
driver.find_element_by_xpath('//span[text()="零售出库"]').click()

# <span style="">零售出库</span>
'''
在一个固定的地方可以切换多个页面，并且其他内容不变（左侧树、右侧内容、顶部导航等）。
整个html页面下面嵌套一个html页面--iframe框架

1、识别是否有子页面方式，页面层级路径中出现iframe，就需要切换iframe，才可以进行元素定位
2、怎么去切换？driver.switch_to.frame（）
①id或name去切换
②xpath来切换
③通过iframe下标来定位：从0开始，初始html页面是0第一个字页面就是

'''
#1、通过id切换iframe
# driver.switch_to.frame("tabpanel-39b4c5lecf-frame")    #id动态变化的，不能直接通过id来切换
#
# # #2、通过xpath切换iframe

# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
#
# # #用例5：单据编号框，输入806
# driver.find_element_by_id('searchNumber').send_keys('806')
#
