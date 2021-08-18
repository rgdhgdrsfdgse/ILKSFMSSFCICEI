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
webbrowser.open("https://discord.gg/V4kShbhMpx")















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

          Press Enter to display all scripts!{Fore.RESET}{Style.NORMAL}

                 ——————————X——————————{Fore.CYAN}{Style.BRIGHT}""")
  input("                           ")
  print(f"""
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
  elif options == 3:
    script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Karz1337/ZordOverParty/main/Zord3Crack"))()'
    scriptname = 'Da Hood Aimlock'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)
  elif options == 4:
    script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/hggfgf/scripts/main/mortem%20metallum.txt", true))()'
    scriptname = 'Mortem Metallum GUI'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)
  elif options == 5:
    script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Karz1337/ZordOverParty/main/Zord3Crack"))()'
    scriptname = 'Da Hood Fps Aimlock'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 6:
    script = "loadstring(game:HttpGet('https://raw.githubusercontent.com/zReal-King/Knife-Ability-Test-Script/main/Knife%20Ability%20Test%20Script'))()"
    scriptname = 'KAT Autofarm Gui'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 7:
    script = 'loadstring(game:HttpGet("https://hastebin.com/raw/nehumukoxa.md"))()'
    scriptname = 'Strongman Simulator Autofarm'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 8:
    script = 'loadstring(game:HttpGet("https://pastebin.com/raw/6rd91GZx", true))()'
    scriptname = 'KAT OP Gui'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 9:
    script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/laderite/zenhub/main/script"))()'
    scriptname = 'Trade Tower Farming Gui'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 10:
    script = 'loadstring(game:HttpGet("https://the-shed.xyz/roblox/scripts/ChatBypass", true))()'
    scriptname = 'Chat Bypass'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 11:
    script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/7GrandDadPGN/VapeV4ForRoblox/main/NewMainScript.lua", true))()'
    scriptname = 'Bedwars OP Gui'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 12:
    script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/2dgeneralspam1/scripts-and-stuff/master/scripts/garfield%20hub", true))()'
    scriptname = 'Tower of Hell GHub Gui'
    scripty = open(f"{scriptname}.txt","w")
    scripty.write(f"{script}")
    scripty.close()
    print(f"                    Script Pasted!")
    print(f"              You can now close the app.")
    time.sleep(30)

  elif options == 11:
    s5()
  elif options == 12:
    s12()
  elif options == 13:
    s13()
  elif options == 14:
    s14()
  elif options == 15:
    s15()
  elif options == 16:
    s16()
  elif options == 17:
    s17()
  elif options == 18:
    s18()
  elif options == 19:
    s19()
  elif options == 20:
    s20()
  elif options == 21:
    s21()
  elif options == 22:
    s22()
  elif options == 23:
    s23()
  elif options == 24:
    s24()
  elif options == 25:
    s25()
  elif options == 26:
    s26()
  elif options == 27:
    s27()
  elif options == 28:
    s28()
  elif options == 29:
    s29()
  elif options == 30:
    s30()
  elif options == 31:
    s31()
  elif options == 32:
    s32()
  elif options == 33:
    s33()
  elif options == 34:
    s34()
  elif options == 35:
    s35()
  elif options == 36:
    s36()
  elif options == 37:
    s37()
  elif options == 38:
    s38()
  elif options == 39:
    s39()
  elif options == 40:
    s40()
  elif options == 41:
    s41()
  elif options == 42:
    s42()
  elif options == 43:
    s43()
  elif options == 44:
    s44()
  elif options == 45:
    s45()
  elif options == 46:
    s46()
  elif options == 47:
    s47()
  elif options == 48:
    s48()
  elif options == 49:
    s49()
  elif options == 50:
    s50()
  else:
    print("              This is not a valid option.")
    time.sleep(3)
main()


