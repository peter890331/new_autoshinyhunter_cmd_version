import time
from datetime import datetime
import win32gui,win32api,win32con,win32ui,win32com.client
import cv2
import requests
import json
import re
from bs4 import BeautifulSoup
import uiautomator2 as u2
import subprocess
import string
letters=string.ascii_lowercase + string.ascii_uppercase

#----------------------------------------------------------------------------------------------------------------
def parameter_setting():
    #記事本參數設定
    f = open('parameter_setting.txt', "r" ,encoding = "utf-8") # 開啟並讀取檔案
    lines = f.readlines() # 讀取檔案內容的每一行文字為陣列
    #for line in lines:
        #print(line, end = '') # 印出時結尾不印new line
    channelid = lines[0][10:-1]
    L_wanted = int(lines[3][9:-1])
    more_check = int(lines[6][11:-1])
    check_delay = int(lines[9][12:-1])
    wifi_delay = int(lines[12][11:-1])
    check_position = int(lines[15][15])
    male_and_female = str(lines[18][16])
    specific_pokemon = str(lines[21][17:-1])
    shiny_symbol =  int(lines[24][13])
    phone_name = lines[27][11:-1]
    DC_headers = {'authorization': str(lines[30][12:-2])}
    Pokedex100_header_User_Agent = lines[33][30:-2]
    Pokedex100_header_Cookie = lines[36][26:-2]

    f.close() # 關閉檔案
    return channelid, L_wanted, more_check, DC_headers, Pokedex100_header_User_Agent, Pokedex100_header_Cookie, phone_name, check_position, check_delay, wifi_delay, specific_pokemon, male_and_female, shiny_symbol
#----------------------------------------------------------------------------------------------------------------

def DC_crawler(channelid): #DC爬蟲 https://youtu.be/xh28F6f-Cds
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers = DC_headers) #選擇DC特定頻道爬蟲
    jsonn = json.loads(r.text)
    Pokedex100_url  = re.findall(r'(https?://[^\s]+)', jsonn[0]['embeds'][0]['description'])[0][:-1] #尋找Pokedex100網址
    Pokedex100_name_with_more_letter = re.findall(r'( [^\s]+)',jsonn[0]['content'])[0]
    Pokedex100_name = ''
    for word in Pokedex100_name_with_more_letter:
        if word in letters:
            Pokedex100_name += word
    Pokedex100_CP = re.findall(r'(CP[^\s]+)',jsonn[0]['content'])[0][2:-2]
    Pokedex100_L_with_more_letter = re.findall(r'(L[^\s]+)',jsonn[0]['content'])[0]
    try:
        Pokedex100_L = int(Pokedex100_L_with_more_letter[1:-2])
    except:
        Pokedex100_L_with_more_letter = re.findall(r'(L[^\s]+)', jsonn[0]['content'])[1]
        Pokedex100_L = int(Pokedex100_L_with_more_letter[1:-2])

    try:
        Pokedex100_have_shiny = re.findall(r'(shiny[^\s]+)',jsonn[0]['content'])[0]
    except:
        Pokedex100_have_shiny = 0

    if re.search(r'(♂)',jsonn[0]['content']) != None:
        Pokedex100_sex = '1'
    elif re.search(r'(♀)',jsonn[0]['content']) != None:
        Pokedex100_sex = '0'
    else: Pokedex100_sex = 'none'

    if shiny_symbol == 1:
        if Pokedex100_have_shiny != 0:
            if specific_pokemon != str():
                if Pokedex100_name in specific_pokemon.split():
                    if male_and_female != '0' and male_and_female != '1':
                        can_catch = 1
                        return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                        # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                    else:
                        if Pokedex100_sex == male_and_female:
                            can_catch = 1
                            return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                            # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                        else:
                            can_catch = 0
                            return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                            # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)

                else:
                    can_catch = 0
                    return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                    # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)

            elif specific_pokemon == str():
                if male_and_female != '0' and male_and_female != '1':
                    can_catch = 1
                    return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                    # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                else:
                    if Pokedex100_sex == male_and_female:
                        can_catch = 1
                        return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                        # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                    else:
                        can_catch = 0
                        return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                        # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)

        elif Pokedex100_have_shiny == 0:
            can_catch = 0
            return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
            # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)

    elif shiny_symbol == 0:
        if specific_pokemon != str():
            if Pokedex100_name in specific_pokemon.split():
                if male_and_female != '0' and male_and_female != '1':
                    can_catch = 1
                    return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                    # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                else:
                    if Pokedex100_sex == male_and_female:
                        can_catch = 1
                        return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                        # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                    else:
                        can_catch = 0
                        return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                        # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
            else:
                can_catch = 0
                return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)

        elif specific_pokemon == str():
            if male_and_female != '0' and male_and_female != '1':
                can_catch = 1
                return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
            else:
                if Pokedex100_sex == male_and_female:
                    can_catch = 1
                    return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                    # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)
                else:
                    can_catch = 0
                    return can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L  # 回傳Pokedex100網址與CP、L
                    # print(can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L)

def Pokedex100_crawler(Pokedex100_header_User_Agent, Pokedex100_header_Cookie):
    Pokedex100_headers = {'User-Agent': Pokedex100_header_User_Agent,
                          'Cookie': Pokedex100_header_Cookie}

    resp = requests.get(Pokedex100_url, headers= Pokedex100_headers) #對Pokedex100網址爬蟲
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup)
    coord_index = soup.find_all('input')
    coord = coord_index[0].get('value') #尋找座標
    #print(coord)

    return coord #回傳座標

def click_position(hwnd, x_position, y_position): #點擊子句柄的相對座標
    """
    鼠標左鍵點擊座標
    :param hwnd:
    :param x_position:
    :param y_position:
    :return:
    """
    # 將兩個16位的值連接成一個32位的地址座標
    long_position = win32api.MAKELONG(x_position, y_position)
    win32api.SendMessage(hwnd, win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP, long_position)
    # 點擊左鍵
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(0.5)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

def window_capture(filename,hwnd,pos=None):
    filename = filename
    hwnd = hwnd  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    if pos==None:
        x1=0
        y1=0
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
    else:
        x1=pos[0]
        y1=pos[1]
        w=pos[2]-pos[0]
        h=pos[3]-pos[1]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, MoniterDev[0][2][2], MoniterDev[0][2][3])
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((x1, y1), (w, h), mfcDC, (x1, y1), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    #清楚图片数据，防止内存泄露
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()

def find_picture(target_gray,template):
    #获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target_gray,template,cv2.TM_SQDIFF_NORMED)
    #归一化处理
    #cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    strmin_val = str(min_val)
    #绘制矩形边框，将匹配区域标注出来
    #min_loc：矩形定点
    #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(target_gray,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
    #显示结果,并将匹配值显示在标题栏上
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    X=min_loc[0]
    Y=min_loc[1]
    return X, Y, twidth, theight, min_val
#----------------------------------------------------------------------------------------------------------------

print('- new_autoshinyhunter_v3.0 - made by Peter YU')
print('')
print('請確認parameter_setting.txt參數設定，完成請按下Enter鍵')
input("Press Enter to continue...")
channelid, L_wanted, more_check, DC_headers, Pokedex100_header_User_Agent, Pokedex100_header_Cookie, phone_name, check_position, check_delay, wifi_delay, specific_pokemon, male_and_female, shiny_symbol = parameter_setting()
print('請手動開啟NemoADB.exe，並可最小化其視窗，完成請按下Enter鍵')
input("Press Enter to continue...")
print('請將手機啟用AtxAgent，開啟GPS Joystick傳送至任意位置並隱藏，開啟Pokemon Go並確認遊戲視角與記事本設定相同，完成請按下Enter鍵')
input("Press Enter to continue...")
wifi_mode = int(input("請選擇手機連接模式，USB連接請輸入0(建議)、Wifi連接請輸入1："))
if(wifi_mode == 0):
    print(' * USB連接模式')
    print('請將手機以USB接上電腦，完成請按下Enter鍵')
    input("Press Enter to continue...")
    subprocess.Popen("cd .\\scrcpy-win64-v1.21 && adb disconnect", shell=True, stdout=subprocess.PIPE)
    time.sleep(1)
    win32api.ShellExecute(0, 'open', '.\\scrcpy-win64-v1.21\\scrcpy.exe', '', '', 1)
    time.sleep(3)
    wifi_delay = 0

elif(wifi_mode == 1):
    print(' * Wifi連接模式')
    wifi_ip = str(input("請將手機開啟Wifi並先連接上電腦，再輸入ip位置："))
    time.sleep(1)
    subprocess.Popen("cd .\\scrcpy-win64-v1.21 && adb tcpip 5555", shell=True, stdout=subprocess.PIPE)
    #time.sleep(1)
    NemoADB_hwnd = win32gui.FindWindow(None, u"NemoADB for GPS Joystick")  # 獲得JoystickADB的句柄
    NemoADB_hwnd_wifi = win32gui.FindWindowEx(NemoADB_hwnd, 0, 'Button', 'WiFi')  # 獲得JoystickADB wifi的句柄
    click_position(NemoADB_hwnd_wifi, 25, 25)
    time.sleep(1)
    print('請將手機與電腦連接拔除，完成請按下Enter鍵')
    input("Press Enter to continue...")
    subprocess.Popen("cd .\\scrcpy-win64-v1.21 && adb connect " + wifi_ip + ":5555 && scrcpy -t -b2M -m1080", shell=True, stdout=subprocess.PIPE)
    time.sleep(3)
    wifi_delay = wifi_delay

print(' ')
start_time = datetime.now()
print('start_time :' + str(start_time))
print(' ')

phone_hwnd = win32gui.FindWindow(None, phone_name) #獲得手機的句柄
NemoADB_hwnd = win32gui.FindWindow(None,u"NemoADB for GPS Joystick") #獲得JoystickADB的句柄
#NemoADB_hwnd_paste_coord = win32gui.FindWindowEx(NemoADB_hwnd, 0, 'Button', 'Paste') #獲得JoystickADB 貼上coord的句柄
#NemoADB_hwnd_START = win32gui.FindWindowEx(NemoADB_hwnd, 0, 'Button', '   START   ') #獲得JoystickADB 傳送定位的句柄
#NemoADB_hwnd_Edit = win32gui.FindWindowEx(NemoADB_hwnd, 0, 'Edit', '') #獲得JoystickADB 輸入框的句柄
#NemoADB_hwnd_left, NemoADB_hwnd_top, NemoADB_hwnd_right, NemoADB_hwnd_bottom = win32gui.GetWindowRect(NemoADB_hwnd)#獲得JoystickADB的句柄定位

if(wifi_mode == 0):
    d = u2.connect() #uiautomator2連接手機(手機要先安裝ATXagent)
    d.info
elif(wifi_mode == 1):
    d = u2.connect(wifi_ip)
    d.info
    time.sleep(1)

shiny_template = cv2.imread('template\\shiny.jpg', 0)
weather_alert_template = cv2.imread('template\\weather_alert.jpg', 0)
#USB_connect_check_template = cv2.imread('template\\USB_connect_check.jpg', 0)
move_too_fast_template = cv2.imread('template\\move_too_fast.jpg', 0)
gym_X_template = cv2.imread('template\\gym_X.jpg', 0)
poke_stop_X_template = cv2.imread('template\\poke_stop_X.jpg', 0)
rocket_team_X_template = cv2.imread('template\\rocket_team_X.jpg', 0)

Pokedex100_url_temp = '0'
check_pokemon = 0
new_coord_waiting = 0

while True:
    phone_hwnd_left, phone_hwnd_top, phone_hwnd_right, phone_hwnd_bottom = win32gui.GetWindowRect(phone_hwnd)  # 獲得手機的句柄定位
    can_catch, Pokedex100_url, Pokedex100_name, Pokedex100_CP, Pokedex100_L = DC_crawler(channelid) #呼叫DC_crawler(channelid)函式

    if can_catch == 1 :
        if(Pokedex100_url != Pokedex100_url_temp and Pokedex100_L >= L_wanted):
            coord = Pokedex100_crawler(Pokedex100_header_User_Agent,Pokedex100_header_Cookie)  # 呼叫Pokedex100_crawler(Pokedex100_header_User_Agent, Pokedex100_header_Cookie)函式
            Pokedex100_url_temp = Pokedex100_url
            NemoADB_hwnd_Edit = win32gui.FindWindowEx(NemoADB_hwnd, 0, 'Edit', '') #獲得JoystickADB 輸入框的句柄
            win32gui.SendMessage(NemoADB_hwnd_Edit, win32con.WM_SETTEXT, None, coord) #在JoystickADB 輸入框貼上coord
            NemoADB_hwnd_START = win32gui.FindWindowEx(NemoADB_hwnd, 0, 'Button', '   START   ') #獲得JoystickADB 傳送定位的句柄
            time.sleep(1)
            click_position(NemoADB_hwnd_START, 25, 25) #點擊傳送定位
            print('tp to :' + str(coord))
            print('Pokemon Name :' + Pokedex100_name, ', CP :' + Pokedex100_CP, ', L :' + str(Pokedex100_L))
            time.sleep(22 + wifi_delay)
            #print(1)
            '''shell = win32com.client.Dispatch("WScript.Shell") #強制手機窗口上層，避免錯誤追加函式
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(phone_hwnd) #強制手機窗口上層'''
            window_capture('weather_alert&move_too_fast_screenshot', phone_hwnd, pos=None)
            target = cv2.imread('.\\weather_alert&move_too_fast_screenshot')
            target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
            X, Y, twidth, theight, min_val = find_picture(target_gray, move_too_fast_template)
            # print('   move_too_fast_screenshot :' + str(min_val))
            time.sleep(0.5)
            if (abs(min_val) < abs(0.02)):
                print('   move_too_fast?')
                d.click(545, 1558)
                time.sleep(0.5 + wifi_delay)

            X, Y, twidth, theight, min_val = find_picture(target_gray, weather_alert_template)
            #print('   weather_alert_screenshot :' + str(min_val))
            time.sleep(0.5)
            if (abs(min_val) < abs(0.02)):
                print('   weather_alert?')
                d.click(545, 1558)
                time.sleep(0.5 + wifi_delay)

            if(check_position == 0):
                d.click(532, 1716)
                time.sleep(0.15 + wifi_delay)
                d.click(532, 1566)
                time.sleep(0.15 + wifi_delay)
                d.click(532, 1866)
                time.sleep(0.15 + wifi_delay)
                d.click(267, 1716)
                time.sleep(0.15 + wifi_delay)
                d.click(797, 1716)
            elif(check_position == 1):
                d.click(534, 1477)
                time.sleep(0.15 + wifi_delay)
                d.click(534, 1426)
                time.sleep(0.15 + wifi_delay)
                d.click(534, 1528)
                time.sleep(0.15 + wifi_delay)
                d.click(455, 1477)
                time.sleep(0.15 + wifi_delay)
                d.click(613, 1477)

            time.sleep(4 + wifi_delay)
            check_pokemon = check_pokemon + 1
            print('check_pokemon :' + str(check_pokemon))

            window_capture('screenshot', phone_hwnd, pos=None)
            target = cv2.imread('.\\screenshot')
            target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
            X, Y, twidth, theight, min_val = find_picture(target_gray, gym_X_template)
            time.sleep(0.5)
            #print('   screenshot_gym :' + str(min_val))
            if (abs(min_val) < abs(0.015)):
                print('   gym?')
                d.click(545, 2135)
                time.sleep(0.5 + wifi_delay)

            X, Y, twidth, theight, min_val = find_picture(target_gray, poke_stop_X_template)
            time.sleep(0.5)
            #print('   screenshot_poke_stop :' + str(min_val))
            if (abs(min_val) < abs(0.015)):
                print('   poke_stop?')
                d.click(541, 2110)
                time.sleep(0.5 + wifi_delay)

            X, Y, twidth, theight, min_val = find_picture(target_gray, rocket_team_X_template)
            time.sleep(0.5)
            #print('   screenshot_rocket_team :' + str(min_val))
            if (abs(min_val) < abs(0.015)):
                print('   rocket_team?')
                d.click(541, 2110)
                time.sleep(0.5 + wifi_delay)
                d.click(541, 2110)
                time.sleep(0.5 + wifi_delay)
                d.click(541, 2110)
                time.sleep(2 + wifi_delay)
                d.click(541, 2110)
                time.sleep(0.5 + wifi_delay)


            target = cv2.imread('.\\screenshot')
            target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
            X, Y, twidth, theight, min_val = find_picture(target_gray, shiny_template)
            time.sleep(0.5)
            #print('   shiny_screenshot_1 :' + str(min_val))
            if (abs(min_val) < abs(0.02)):
                print(' ')
                print('!!! SHINY !!!')
                print(' ')
                end_time = datetime.now()
                print('end_time :' + str(end_time))
                #print(' ')
                input("Please STOP the code")
            else:
                print('not shiny==')

            for t in range(0, more_check):
                time.sleep(check_delay + wifi_delay)
                window_capture('shiny_screenshot_' + str(t+2), phone_hwnd, pos=None)
                target = cv2.imread('.\\shiny_screenshot_' + str(t+2))
                target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
                X, Y, twidth, theight, min_val = find_picture(target_gray, shiny_template)
                time.sleep(0.5)
                #print('   shiny_screenshot_' + str(t+2) + ' :' + str(min_val))
                if (abs(min_val) < abs(0.02)):
                    print(' ')
                    print('!!! SHINY !!!')
                    print(' ')
                    end_time = datetime.now()
                    print('end_time :' + str(end_time))
                    #print(' ')
                    input("Please STOP the code")
                else:
                    print('not shiny==')

            print(' ')
            d.click(104, 266)
            time.sleep(wifi_delay)
            new_coord_waiting = 0

        else:
            new_coord_waiting = new_coord_waiting + 1
            if(new_coord_waiting == 1):
                print('No new coord, waiting', end = ' ')
                time.sleep(0.5)
                print('.', end = ' ')
                time.sleep(0.5)
                print('.', end = ' ')
                time.sleep(0.5)
                print('.')
                time.sleep(0.5)
                print(' ')
            else:
                time.sleep(0.5)

    elif can_catch == 0:
        new_coord_waiting = new_coord_waiting + 1
        if (new_coord_waiting == 1):
            print('No new coord, waiting', end=' ')
            time.sleep(0.5)
            print('.', end=' ')
            time.sleep(0.5)
            print('.', end=' ')
            time.sleep(0.5)
            print('.')
            time.sleep(0.5)
            print(' ')
        else:
            time.sleep(0.5)
