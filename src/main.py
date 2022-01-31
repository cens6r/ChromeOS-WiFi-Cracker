import os, sys, time

from utils.banner import Banner
from utils.logger import Logger

def main():
  print(Banner.BANNER())
  Logger.info('ChromeOS Wifi Password Cracker')
  Logger.warning('Make sure your operating system is ChromeOS and developer mode is on.')

  if sys.platform == 'linux':
    Logger.success('ChromeOS Detected')
    pass
  else:
    Logger.error('OS not supported.')

  Logger.info('Starting program in 3 seconds...')
  time.sleep(3)

  Logger.info('Entering shell...')
  os.popen('shell')

  Logger.info('Entering sudo...')
  os.popen('sudo su')

  Logger.info('Searching for root...')
  os.popen('cd/home root')

  Logger.info('Getting code...')
  code = os.popen('ls').read()
  Logger.info(f'Code Found! {code}')

  Logger.info('Entering code directory...')
  os.popen(f'cd {code}')

  Logger.info('Getting list of wifi...')
  wifiList = os.popen('more shill/shill.profile').read()
  print(wifiList)
  Logger.info('Find your wifi and copy the text next to passphrase=rot47: .')
  rot47 = str(input('Enter ROT47 Encrypted Text: '))
  password = os.popen(f"echo {rot47} | tr ‘!-~’ ‘P-~!-O’").read()

  if password:
    Logger.success(f'Password has been found: {password}')
  else:
    Logger.error('Password has not been found.')

if __name__ == '__main__':
  main()
