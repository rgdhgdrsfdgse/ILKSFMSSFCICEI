import colorama
from colorama import Fore, Style, Back
import time
import webbrowser
import os
import ctypes
colorama.init()

ver = 1.0

ctypes.windll.kernel32.SetConsoleTitleW(f'Thundux v{ver} [BETA] | Loading.')
time.sleep(0.3)
ctypes.windll.kernel32.SetConsoleTitleW(f'Thundux v{ver} [BETA] | Loading..')
time.sleep(0.3)
ctypes.windll.kernel32.SetConsoleTitleW(f'Thundux v{ver} [BETA] | Loading...')
time.sleep(0.3)
ctypes.windll.kernel32.SetConsoleTitleW(f'Thundux v{ver} [BETA] | Loading.')
time.sleep(0.3)
ctypes.windll.kernel32.SetConsoleTitleW(f'Thundux v{ver} [BETA] | Launched!')














#                        .▄▄ ·  ▄▄· ▄▄▄  ▪   ▄▄▄·▄▄▄▄▄.▄▄ ·                 
#        ▪     ▪         ▐█ ▀. ▐█ ▌▪▀▄ █·██ ▐█ ▄█•██  ▐█ ▀.     ▪     ▪     
#         ▄█▀▄  ▄█▀▄     ▄▀▀▀█▄██ ▄▄▐▀▀▄ ▐█· ██▀· ▐█.▪▄▀▀▀█▄     ▄█▀▄  ▄█▀▄ 
#        ▐█▌.▐▌▐█▌.▐▌    ▐█▄▪▐█▐███▌▐█•█▌▐█▌▐█▪·• ▐█▌·▐█▄▪▐█    ▐█▌.▐▌▐█▌.▐▌
#         ▀█▄▀▪ ▀█▄▀▪     ▀▀▀▀ ·▀▀▀ .▀  ▀▀▀▀.▀    ▀▀▀  ▀▀▀▀      ▀█▄▀▪ ▀█▄▀▪








def scriptplate():
    script = ''
    scriptname = ''
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)








def main():
  print(Fore.CYAN)
  print(f""" {Style.BRIGHT}
        ▄▄▄▄▄ ▄ .▄ ▄• ▄▌ ▐ ▄ ·▄▄▄▄  ▄• ▄▌▐▄• ▄ 
        •██  ██▪▐█ █▪██▌•█▌▐███▪ ██ █▪██▌ █▌█▌▪
         {Style.NORMAL}▐█.▪██▀▐█ █▌▐█▌▐█▐▐▌▐█· ▐█▌█▌▐█▌ ·██· 
         ▐█▌·██▌▐▀ ▐█▄█▌██▐█▌██. ██ ▐█▄█▌▪▐█·█▌
         {Fore.BLUE}▀▀▀ ▀▀▀  · ▀▀▀ ▀▀ █▪▀▀▀▀▀•  ▀▀▀ •▀▀ ▀▀{Fore.RESET}
                 ——————————X——————————
                     Need Support?
                 discord.gg/V4kShbhMpx
                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}
                      [1] Scripts
                    [2] VIP Servers{Fore.RESET}{Style.NORMAL}
                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}""")
  optionz = int(input("                           "))
  if optionz == 1:
    print(f"""{Fore.RESET}{Style.NORMAL}                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}
                        SCRIPTS{Fore.RESET}{Style.NORMAL}
                 ——————————X——————————
      {Fore.CYAN}{Style.BRIGHT}
               [1] Jailbreak Vynixius GUI
                   [2] Da Hood Crash
                  [3] Da Hood Aimlock
                 [4] Mortem Metallum GUI
                 [5] Da Hood Fps Aimlock
                  [6] KAT Autofarm Gui
            [7] Strongman Simulator Autofarm
                     [8] KAT OP Gui
               [9] Trade Tower Farming Gui
                    [10] Chat Bypass
                   [11] Bedwars OP Gui
               [12] Tower of Hell GHub Gui
                    [13] Da Hood Nuke
                   [14] Fates Admin V2
               [15] Anime Warriors Autofarm
                 [16] Pet Simulator X Gui
       [17] Millionaire Empire Tycoon Infinity money
                  [18] East Brickton GUI
                 [19] RoBeats Auto Player
                  [20] Universal Aimbot
                    [21] The Lift Gui
                [22] Anomic Alwayswin Gui
              [23] Lumber Tycoon Dupe Money
           [24] Your Bizarre Adventure Item Esp
              [25] Da Hood Silent aim / Lock
                [26] Infinite Yield Admin
                       [27] OwlHub
              [28] Car Crusher 2 Gui AutoFarm
           [29] Robloxian High School Mods V3 Gui
               [30] Myth Piece Autfofarm Gui
                [31] King Legacy Auto Farm
          [32] Whack People Free Weapons Gamepass
                  [33] Bedwars Vape Gui
                  [34] Base Battles Gui
       [35] Fling Things and People Click void fling
             [36] Da Hood suicide (In fun gui)
                 {Fore.RESET}{Style.NORMAL}
                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}
             Ctrl F to search for a script!{Fore.RESET}{Style.NORMAL}
                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}""")
    options = int(input(f"""                   Input script ID: """))
    if options == 1:
      script =  'loadstring(game:HttpGet("https://raw.githubusercontent.com/RegularVynixu/Vynixius/main/Jailbreak/Jailbreak"))()'
      scriptname = 'Jailbreak Vynixius GUI'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      exit()
      time.sleep(30)
    elif options == 2:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/racemodex/my-scripts/master/dahoodcrash", true))()'
      scriptname = 'Da Hood Crash'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 3:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Karz1337/ZordOverParty/main/Zord3Crack"))()'
      scriptname = 'Da Hood Aimlock'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 4:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/hggfgf/scripts/main/mortem%20metallum.txt", true))()'
      scriptname = 'Mortem Metallum GUI'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 5:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Karz1337/ZordOverParty/main/Zord3Crack"))()'
      scriptname = 'Da Hood Fps Aimlock'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 6:
      script = "loadstring(game:HttpGet('https://raw.githubusercontent.com/zReal-King/Knife-Ability-Test-Script/main/Knife%20Ability%20Test%20Script'))()"
      scriptname = 'KAT Autofarm Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 7:
      script = 'loadstring(game:HttpGet("https://hastebin.com/raw/nehumukoxa.md"))()'
      scriptname = 'Strongman Simulator Autofarm'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 8:
      script = 'loadstring(game:HttpGet("https://pastebin.com/raw/6rd91GZx", true))()'
      scriptname = 'KAT OP Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 9:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/laderite/zenhub/main/script"))()'
      scriptname = 'Trade Tower Farming Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 10:
      script = 'loadstring(game:HttpGet("https://the-shed.xyz/roblox/scripts/ChatBypass", true))()'
      scriptname = 'Chat Bypass'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 11:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/7GrandDadPGN/VapeV4ForRoblox/main/NewMainScript.lua", true))()'
      scriptname = 'Bedwars OP Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 12:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/2dgeneralspam1/scripts-and-stuff/master/scripts/garfield%20hub", true))()'
      scriptname = 'Tower of Hell GHub Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 13:
      script = "loadstring(game:HttpGet('https://raw.githubusercontent.com/IcxyLol/nuke/main/README.md'))()"
      scriptname = 'Da Hood Nuke'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 14:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/fatesc/fates-admin/main/main.lua"))();'
      scriptname = 'Fates Admin V2'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()

    elif options == 15:
      script = "loadstring(game:HttpGet('https://raw.githubusercontent.com/insanedude59/AnimeWarriors/main/Output.lua'))()"
      scriptname = 'Anime Warriors Autofarm'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 16:
      script = 'loadstring(game:HttpGet("https://pastebin.com/raw/95HthyJq"))()'
      scriptname = 'Pet Simulator X Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 17:
      script = 'game:GetService("ReplicatedStorage").updateCollector:FireServer(1e18)'
      scriptname = 'Millionaire Empire Tycoon Infinity money'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 18:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/IlIlIllIIlI/Scripts/main/EastBrickton.lua", true))()'
      scriptname = 'East Brickton GUI'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 19:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/LegoHacks/RoBeats/master/Main.lua"))();'
      scriptname = 'RoBeats Auto Player'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 20:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Blissful4992/Miscellaneous/main/UNIVERSAL.lua"))()'
      scriptname = 'Universal Aimbot'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 21:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/timkaMLG1/TheLiftFucker/main/main.lua",true))()'
      scriptname = 'The Lift Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 22:
      script = "loadstring(game:HttpGet('https://raw.githubusercontent.com/KryptonMiner/Prankbros/main/main.py'))()"
      scriptname = 'Anomic Alwayswin Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 23:
      script = 'loadstring(game:HttpGet("https://pastebin.com/raw/hnVtRcyb"))()'
      scriptname = 'Lumber Tycoon Dupe Money'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 24:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/toeydeklnw/HUB-obfuscator/main/YBA%20ITEMS%20ESP"))()'
      scriptname = 'Your Bizarre Adventure Item Esp'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 25:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Stefanuk12/ROBLOX/master/Games/Da%20Hood/SilentAimAimLock.lua"))()'
      scriptname = 'Da Hood Silent aim / Lock'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 26:
      script = "loadstring(game:HttpGet(('https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source'),true))()"
      scriptname = 'Infinite Yield Admin'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 27:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ZinityDrops/OwlHubLink/master/OwlHubBack.lua"))();'
      scriptname = 'OwlHub'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 28:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/saucekid/scripts/main/CarCrushers.lua"))()'
      scriptname = 'Car Crusher 2 Gui AutoFarm'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 29:
      script = "loadstring(game:HttpGet(('https://raw.githubusercontent.com/Nazor1/RHS-MODS-V3/main/RHSMODSV3.1%20OBFUSCATED.lua')))()"
      scriptname = 'Robloxian High School Mods V3 Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 30:
      script = "loadstring(game:HttpGet(('https://raw.githubusercontent.com/XTheMasterX/Scripts/Main/MythPiece'),true))()"
      scriptname = 'Myth Piece Autfofarm Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 31:
      script = "loadstring(game:HttpGet('https://raw.githubusercontent.com/Reset0817/Scripts/main/KingLegacy'))()"
      scriptname = 'King Legacy Auto Farm'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 32:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/heber126/eeeee/main/e"))()'
      scriptname = 'Whack People Free Weapons Gamepass'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 33:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/7GrandDadPGN/VapeV4ForRoblox/main/NewMainScript.lua", true))()'
      scriptname = 'Bedwars Vape Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 34:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/WetCheezit/Base-Battles/main/.lua"))()'
      scriptname = 'Base Battles Gui'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 35:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/ShrimpsHub/ShrimpsHub/main/ShrimpsHub"))()'
      scriptname = 'Fling Things and People Click void fling'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 36:
      script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/NighterEpic/Faded/main/YesEpic", true))()'
      scriptname = 'Da Hood suicide (In fun gui)'
      scripty = open(f"{scriptname}.txt","w")
      scripty.write(f"{script}")
      scripty.close()
      print(f"                    Script Pasted!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    else:
      print("              This is not a valid option.")
      time.sleep(3)
  if optionz == 2:
    print(f"""{Fore.RESET}{Style.NORMAL}                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}
                       VIP SERVERS{Fore.RESET}{Style.NORMAL}
                 ——————————X——————————
                 {Fore.CYAN}{Style.BRIGHT}
             [1] Survive the Night [UPDATE]
                      [2] Da Hood
              [3] Anime Fighting Simulator
                   [4] Tower of Hell
               [5] Tower Defense Simulator
                      [6] Mad City
                      [7] Arsenal
                 [8] Lifting Simulator
                      [9] Ro-Ghoul
                    [10] Blox Fruits
                  [11] Pet Simulator X
                 {Fore.RESET}{Style.NORMAL}
                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}""")
    options = int(input(f"""                   Input Server ID: """))
    if options == 1:
      ServerLink = "https://www.roblox.com/games/990364410?privateServerLinkCode=54854472539647967322058976787133"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 2:
      ServerLink = "https://www.roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=74185243475160654352286120906905"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 3:
      ServerLink = "https://www.roblox.com/games/4042427666/DUNGEONS-Anime-Fighting-Simulator?privateServerLinkCode=11165510253210961427792717826525"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 4:
      ServerLink = "https://www.roblox.com/games/1962086868/Tower-of-Hell?privateServerLinkCode=86039914991262888755060638689247"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 5:
      ServerLink = "https://www.roblox.com/games/3260590327/Tower-Defense-Simulator?privateServerLinkCode=38892024497186755530565578401553"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 6:
      ServerLink = "https://www.roblox.com/games/1224212277/Mad-City?privateServerLinkCode=18453605690528050454932149409946"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 7:
      ServerLink = "https://www.roblox.com/games/286090429/Arsenal?privateServerLinkCode=21613709739907904650675643728245"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 8:
      ServerLink = "https://www.roblox.com/games/3652625463/Lifting-Simulator?privateServerLinkCode=45953442128588141433177667242122"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 9:
      ServerLink = "https://www.roblox.com/games/914010731/Higher-Mind-Ro-Ghoul-ALPHA?privateServerLinkCode=46170764787898345230109717666315"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 10:
      ServerLink = "https://www.roblox.com/games/2753915549/UPDATE-14-Blox-Fruits?privateServerLinkCode=00419009354889845583304086137834"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
    elif options == 11:
      ServerLink = "https://www.roblox.com/games/6284583030/MYTHICAL-Pet-Simulator-X?privateServerLinkCode=33526366351153821793316599088079"
      webbrowser.open(ServerLink)
      print(f"                    Server Opened!")
      print(f"              You can now close the app.")
      time.sleep(30)
      exit()
  else:
    print("              This is not a valid option.")
    time.sleep(3)
main()
