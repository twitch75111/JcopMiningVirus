import subprocess
import requests


def update_client_version(version):
    with open("version.txt", "r") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False


def main():
    version = requests.get("https://raw.githubusercontent.com/mynameispyo/JcopMiningVirus/main/version.txt").text
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return "[*] Updated to latest version: v{}..".format(version)
    else:
        return "[*] You are already up to date with git origin master."


if __name__ == '__main__':
    print("[*] Checking version information..")
    print(main())
