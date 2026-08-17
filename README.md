# new_autoshinyhunter_cmd_version
new_autoshinyhunter_v3.0, made by Peter Yu.  

另有帶有 GUI 的升級版，[new_autoshinyhunter_gui_version][12]。

[12]: https://github.com/peter890331/new_autoshinyhunter_gui_version

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=22&pause=1000&color=36BCF7&center=false&vCenter=false&width=600&lines=No+longer+maintained,+but+should+work.;沒在維護了，但應該能用。" alt="Typing SVG" /></a>

> 一個在Pokémon GO中自動點擊色違且iv100的寶可夢的外掛腳本。    
> A game bot script that automatically clicks and only filters to those pokémons that is shiny and iv100 in Pokémon GO.
>
> I am a Taiwanese, so some instructions and description of parameters in the program are described in traditional Chinese, Taiwan No.1!!!!!

### ❗ 警告：僅以此練習程式編寫，請勿在遊戲中使用外掛，否則後果自負！本人對此內容不負任何法律責任。 ❗    
### ❗ WARNING: Practice programming only, please do not use it to cheat on the game!     
### The consequences are your own! I will not be responsible for any law liability to this content. ❗    
 <img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/icon.png" width="300px">

---
 
## Foreword
In Pokémon Go, beyond your pokémon’s CP (Combat Power), all your caught pokémons have semi-hidden base stats called individual values, or IVs. IVs determine how strong a Pokémon can potentially get. For example, a perfect IV Chansey will have a higher CP at its maxed out level, as opposed to a Chansey with only so-so IVs. There are just three stats to worry about: Attack, Defense, and Stamina, each of which maxes out at 15, and the pokémon with all three stats of 15 is called the iv100 pokémon, it means that this pokémon is the strongest in the same kind of pokémons. In addition, shiny pokémons are rare variants of pokémons that are differently colored than other pokémons of their species. In the game, the chance of having iv100 pokémons on the map is already very low, not to mention that it is also a shiny pokémon, so can see how difficult it is to obtain a pokémon with these two characteristics from the general game method.

---

## Overview
This game bot script can fully automatically send your game position to any location in the world where the specified iv100 pokémon appear, and click on the pokémon to determine whether it is a shiny, if not, then continue to try in the whole world, if yes, stop the script and wait for manual capture.    

Equipment and Software Requirements:
  1. A rooted Android phone with GPS JoyStick ([Google Play][1]) installed **IN THE SYSTEM**, install uiautomator2 ([Github][5]) services such as ATX-agent (may not be necessary for the new version), and of course, install Pokémon GO.
  2. A Windows computer.
  3. scrcpy ([Github][2], [scrcpy-win64-v2.0 download link][3]), this application mirrors Android devices connected via USB or over TCP/IP, and allows to control the device with the keyboard and the mouse of the computer.
  4. NemoADB by PokeNemo ([Official Website][4]), NemoADB is a GUI program useful to speed up your shundo snipe if you have an Android device with GPS Joystick and a Windows PC.
  5. A Discord ([Official Website][6]) account that has joined the Pokedex100 ([Official Website][7]) server, Pokedex100 provides pokémon coordinates all over 30 countries, it used to snipe iv100 pokémons. Free account is enough, no need to pay, because this game bot script also doesn't support croods crawler of donor channels.

[1]: https://play.google.com/store/apps/details?id=com.theappninjas.fakegpsjoystick
[2]: https://github.com/Genymobile/scrcpy
[3]: https://github.com/Genymobile/scrcpy/releases/download/v2.0/scrcpy-win64-v2.0.zip
[4]: https://www.pokenemo.com/nemoadb/
[5]: https://github.com/openatx/uiautomator2
[6]: https://discord.com/
[7]: https://pokedex100.com/

---

## How to use, For users
For users, you can directly download the final version in Releases, it contains a direct executable exe file, and can run it directly after setting some parameters.  
### Steps:
   1. Download the final version files in Releases, unzip each zip file into folders, then place the unziped folders with the new_autoshinyhunter_v3.0.exe file and parameter_settings.txt file in the same folder you created, and for those who are not playing game in traditional Chinese, some of the template screenshots in the template folder will need to be re-screenshot in your game language.
   2. Download scrcpy and unzip it, then place in the the same folder you created too, the folder will look like this:  
      <img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/folder.png" width="200px">
      
   3. Setup parameters in the parameter_settings.txt file, the descriptions of the parameters are as follows:
      1. `channelid`  
         - 選擇欲爬蟲的DC Pokedex頻道id，在網頁版DC的F12 - Network - message?limit=50 - Request URl  
         - The ID of the Discord channel used to broadcast the iv100 pokémons. Go to the Pokedex100 server in web version of Discord, and there is usually a channel called 100communitcy, or a special channel on community days, and press F12 on the browser after selecting the channel, then you can find a number string in the Network - messages?limit=50 - Request URL, the number is `channelid` (if you don't find it, press F5 and look again), however, only free-to-use channels are supported, i.e. channels where the button displays "Click for Coords" instead of "Click for Donor coord".
      2. `L_wanted`  
         - 想要抓的寶可夢至少等級  
         - `L_wanted` means the minimum level of pokémons you want to catch, if set to 0, it will catch all levels of pokémons, if set to 30, it will only catch pokémons above the level 30.
      3. `more_check`  
         - 想要多確認是不是色違的次數(建議取決於該寶可夢的跳躍頻率)  
         - `more_check` means the number of times you want to confirm whether it is a shiny pokémon or not, it is recommended to depend on the jumping frequency of the pokémon.
      4. `check_delay`  
         - 多確認是否色違的間隔(建議取決於該寶可夢的上下移動頻率)  
         - `check_delay` means the time interval to check if it is a shiny pokémon, it is recommended to depend on the up and down movement frequency of the pokémon.
      5. `wifi_delay`  
         - 使用Wifi連接模式時要多等待的延遲時間(取決於網路速度)  
         - `wifi_delay` means the time delay when using Wifi connection mode, it is recommended to depend on Wifi speed.
      6. `check_position`
         - 遊戲視角畫面最大化時設置為0；遊戲視角畫面最小化時則設置為1(適合會飛行，不在腳邊的寶可夢，ex.飛翔皮卡丘)
         - `check_position` means the binary value that depends on the game perspective, set to 0 when the game perspective is maximized; set to 1 when the game perspective is minimized (suitable for those pokémons who will fly or not beside the feet, ex. Flying Pikachu), the maximized game perspective looks like:  
           <img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/maximized%20game%20perspective.png" width="200px">

           , and the minimized game perspective looks like:  
           <img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/minimized%20game%20perspective.png" width="200px">

      7. `male_and_female`
         - 若欲捕捉特定性別的寶可夢，公的設置為1；母的設置為0；若不指定，則空白 
         - `male_and_female` means the value that depends on the specific gender of pokémons you want to catch, male set to 1; female set to 0; if not specified, then blank.
      8. `specific_pokemon`
         - 若DC Pokedex頻道中含有多種寶可夢但只想抓取特定幾種時，打上寶可夢名字（寶可夢間以空白鍵相隔，ex：=Cranidos Shieldon Larvitar）；若無，則空白
         - If the channel of Pokedex100 server contains multiple pokémons but you only want to catch a few specific of them, type the name of those specific pokémons, separated by blank keys, ex：=Cranidos Shieldon Larvitar; if not specified, then blank.
      9. `shiny_symbol`
          - 要抓取的寶可夢在DC Pokedex頻道中是否正常擁有色違符號，若有（通常都有）則設置為1；若包含任何一種要欲抓取的特定寶可夢無色違符號，則設置為0
          - `shiny_symbol` means the binary value that depends on if pokémons to be captured in the channel of Pokedex100 server has the shiny symbol, if yes (usually available) then set to 1;  if it contains any one of the specific pokemon you want to capture, but without shiny symbol, then set to 0, the shiny symbol look like this: <img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/shiny%20symbol.png" width="20px">.
      10. `phone_name`
          - 手機在scrcpy的視窗名
          - The window name of your phone in scrcpy. It is recommended that run scrcpy once before setting this parameter to determine the window name, the way to run scrcpy is: after enable USB debugging on the phone and connecting to the computer with USB, run scrcpy.exe directly.
      11. `DC_headers`
          - 網頁版DC的授權碼，在網頁版DC的F12 - Network - message?limit=50 - authorization
          - The authorization code of the web version of Discord. Go to the Pokedex100 server in web version of Discord, then select the channel of i. `channelid`, and press F12 on the browser after selecting the channel, then you can find the string in the Network - messages?limit=50 - authorization, the string is `DC_headers` (if you don't find it, press F5 and look again).
      12. `Pokedex100_header_User_Agent`
          - Pokedex100的User-Agent，在Pokedex100網頁的F12 - Network - free=h0rphYCSfP97gO - User-Agent
          - The User-Agent code of the Pokedex100 web page. Click on the "Click for Coords" button of a pokémon in Pokedex100 channel randomly, then you will be directed to the Pokedex100 web page, and after authorizate with your Discord account, press F12 on the browser, then you can find the string in the Network - free=XXXXXXXXXXXXXX - User-Agent, the whole string is `Pokedex100_header_User_Agent` (if you don't find it, press F5 and look again).
      13. `Pokedex100_header_Cookie`
          - Pokedex100的Cookie，在Pokedex100網頁的F12 - Network - free=h0rphYCSfP97gO - Set-Cookie
          - The Cookies of the Pokedex100 web page. Click on the "Click for Coords" button of a pokémon in Pokedex100 channel randomly, then you will be directed to the Pokedex100 web page, and after authorizate with your Discord account, press F12 on the browser, then you can find Network - free=XXXXXXXXXXXXXX - Set-Cookie, there may be two of them, what we need are 'csrftoken' and 'sessionid', the 'csrftoken' and 'sessionid' titles should also be pasted like: 'csrftoken=XXXXXXXXXXXXXX; sessionid=XXXXXXXXXXXXXX' (if you don't find it, press F5 and look again).
</br></br>
      - Notice that in this parameter_settings.txt file, every space, blank line, equal sign and semicolon, etc. is necessary, do not change the format, it should look like this:  
        <img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/parameter_settings.png" width="500px">
         
   4. Run new_autoshinyhunter_v3.0.exe file, the descriptions when runnig as follows:
      1. - 請確認parameter_setting.txt參數設定，完成請按下Enter鍵
         - Please confirm parameters setting of parameter_setting.txt file, and press Enter to continue.
      2. - 請手動開啟NemoADB.exe，並可最小化其視窗，完成請按下Enter鍵
         - Please open NemoADB.exe in NemoADB folder manually, and can minimize its window, and press Enter to continue.
      3. - 請將手機啟用AtxAgent，開啟GPS Joystick傳送至任意位置並隱藏，開啟Pokemon Go並確認遊戲視角與記事本設定相同，完成請按下Enter鍵
         - Please enable AtxAgent on your phone (may not be necessary), open GPS Joystick and send to any location then hide its operating interface, open Pokemon Go and make sure the game perspective is the same as the vi. `check_position` setting, and press Enter to continue.
      4. - 請選擇手機連接模式，USB連接請輸入0(建議)、Wifi連接請輸入1
         - Please select the phone connection mode, input 0 (recommended) for USB connection and 1 for Wifi connection, and always remember to open the USB debugging mode before connecting.
         
         A. 若選擇USB連接模式, If select USB connection mode:
         1. - 請將手機以USB接上電腦，完成請按下Enter鍵
            - Please connect your phone to the computer by USB, and press Enter to continue.

         B. 若選擇Wifi連接模式, If select Wifi connection mode:
         1. - 請將手機開啟Wifi並先連接上電腦，再輸入ip位置
            - Please turn on the Wifi on your phone and connect it to the computer by USB first, then input the IP address of your phone, it can usually be found in the phone's settings, looks like: 192.XXX.XX.XXX.
         2. - 請將手機與電腦連接拔除，完成請按下Enter鍵
            - Please disconnectthe USB connection between your phone and computer, and press Enter to continue.
           
         Please remember, if your Wifi is slow, it is recommended that set the v. `wifi_delay` bigger.
</br></br>
      - Then your phone window should pop up automatically, and start sending the location and click on the pokémons, however, if there is no new pokémon coords in the Pokedex100 channel, it may show: No new coord, waiting . . ., just wait for the channel to update.
        
   5. Enjoy the convenience brought by this scripts 🤓.
      - Notice that the UIAUTOMATOR of AtxAgent should be activated automatically when the script starts to run, but sometimes it doesn't work, so if you observe that the script doesn't click on the screen, you need to run the UIAUTOMATOR manually again. Press "刷新 服务 状态" in the ATX app, and if it displays {"running":false}, press "启动 UIAUTOMATOR", then can go back to Pokemon Go.

---

## Make updates, For Developers or the future ?
 - This script use my current phone (RMX2111) for testing, if using different brand or type of phones, when clicking on the screen, may be due to differences in screen size or resolution, resulting in a distorted click position, so in the future, it may be possible to add functions to adapt to different screens.
 - Now the script uses template images in the template folder for image recognition to determine which screen it is on, but sometimes when click on the wrong target, the script will still continue, for example, when click on Team Rockets, for unknown reasons, it does not detect, no return to the map as soon as possible may lose time, this will be a weakness that can be rethought to improve.
 - During the Halloween event, all PokeStops will turn to orange color, which will cause all PokeStops to be unrecognizable when clicked on, because those are rely on the blue color for recognition, so this could lead to an error when script executing.
 - Add coords crawler of donor channels, now only free-to-use channels are supported, because I'm poor, can't afford to sponsor.

---

## Some examples when using
These videos are the gains of my actual use for a period of time, as evidenced by the videos.

(Click in to download to watch the full video.)

Self-made script:

<a href="https://github.com/peter890331/new_autoshinyhunter/blob/figures/Self-made%20script.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter/blob/figures/Self-made%20script.gif" width="200" height=auto>
</a>

Self-made script updated (2023/11/13) :

<a href="https://github.com/peter890331/new_autoshinyhunter/blob/figures/Self-made%20script%202.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter/blob/figures/Self-made%20script%202.gif" width="200" height=auto>
</a>

ALL shiny:

<a href="https://github.com/peter890331/new_autoshinyhunter/blob/figures/ALL%20shiny.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter/blob/figures/ALL%20shiny.gif" width="200" height=auto>
</a>

ALL shiny updated (2023/11/13) :

<a href="https://github.com/peter890331/new_autoshinyhunter/blob/figures/ALL%20shiny%202.mp4">
  <img src="https://github.com/peter890331/new_autoshinyhunter/blob/figures/ALL%20shiny%202.gif" width="200" height=auto>
</a>

These screenshots are my actual usage, including testing while developing, I also like to use the script while doing other things, while I focus on other things, the script will continue to click pokémons for me.
</br>
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/1.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/2.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/3.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/4.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/5.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/6.png" width="100px">
</br></br>
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/7.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/8.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/9.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/10.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/11.png" width="100px">
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/12.jpg" width="100px">
</br></br>
And then an update (2023/11/13) for use on Halloween.
</br>
<img src= "https://github.com/peter890331/new_autoshinyhunter/blob/figures/13.png" width="100px">

(Unowns was captured using another script that I written previously, which was used to collect all kinds of Unowns.)

---

## Notes
### scrcpy
scrcpy ([Github][2], [scrcpy-win64-v2.0 download link][3]), this application mirrors Android devices connected via USB or over TCP/IP, and allows to control the device with the keyboard and the mouse of the computer.  
Here are some command steps can use to test the Wifi connection mode:
1. cd /d C:\Users\XXX\scrcpy-win64-vX.XX
2. adb tcpip 5555
3. adb connect 192.XXX.XX.XXX:5555
4. scrcpy -t -b2M -m800
   
Then here are two useful shortcuts to turn off the phone screen while connected:
- Turn device screen off (keep mirroring):	MOD+o
- Turn device screen on:	MOD+Shift+o  
  (MOD key is usually Alt)
  
And a traditional Chinese teaching video on [Youtube][8].

[8]: https://youtu.be/WkTd5OxDZ-8

### WindowThumbnail
If you are using your computer to do other things at the same time as running this script, and want to keep checking if shiny pokémon has appeared, you can use WindowThumbnail ([Github][9], [WindowThumbnail-v1.0 download link][11]) to continuously displays your phone screen or the cmd of this script in a small window on the upper level of your computer.

And a traditional Chinese tutorial on [巴哈姆特][10].

[9]: https://github.com/neilchennc/WindowThumbnail
[10]: https://forum.gamer.com.tw/Co.php?bsn=19017&sn=318177
[11]: https://github.com/neilchennc/WindowThumbnail/releases/download/v1.0/WindowThumbnail-v1.0.exe

### PyInstaller
If there are updates to this script in the future,    
can use PyInstaller to package the .py file into an .exe file, use 'pyinstaller -F XXX.py' command,    
to add your own icon, use 'pyinstaller --onefile --windowed --icon=icon.ico XXX.py' command.

---

### ❗ 再次警告：僅以此練習程式編寫，請勿在遊戲中使用外掛，否則後果自負！本人對此內容不負任何法律責任。 ❗    
### ❗ WARNING AGAIN: Practice programming only, please do not use it to cheat on the game!     
### The consequences are your own! I will not be responsible for any law liability to this content. ❗   
