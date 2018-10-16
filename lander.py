#!/usr/bin/python3

import socket, time, datetime, random, platform, argparse, termcolor
from pprint import pprint


parser = argparse.ArgumentParser(description='MARS v0.001')
parser.add_argument('-v', '--verbose', action='store_true', help='Be versbose with logging.')
parser.add_argument('--local', action='store_true', help='host will bind only on localhost.')
parser.add_argument('--debug', action='store_true', help ='')
args = parser.parse_args()
# establish configuration, check if it's already set up and





def log(msg, level):
	""" Error logging function, level 1 is information, level 2 is warning and level 3 is critical. """
	try:
		with open('/var/log/mars', 'a+') as logfile:
			if level == 1:
				level_word = 'Information'
				fullmsg = '[{}][{}] {}.\r\n'.format(datetime.datetime.today().strftime('%a %b %d %H:%M:%S %Y'), level_word, msg)
				if args.verbose:
					print(fullmsg)
				logfile.writelines(fullmsg)
				return
			elif level == 2:
				level_word = 'Warning'
				fullmsg = '[{}][{}] {}, '.format(datetime.datetime.today().strftime('%a %b %d %H:%M:%S %Y'), level_word, msg)
				print(fullmsg)
				logfile.writelines(fullmsg)
			elif level == 3:
				level_word = 'Critical'
				fullmsg = '[{}][{}] {}, '.format(datetime.datetime.today().strftime('%a %b %d %H:%M:%S %Y'), level_word, msg)
				print('{}\nCritical Error Encountered, Press any key to exit...'.format(fullmsg))
				if args.debug:
					pprint(vars())
				input('')
				exit(1)
	except IOError:
		print(colored('Error 01: Logfile not writeable.'))
		exit(1)


log('Execution begin.', 1)
time.sleep(3)
log('Testing Warning', 2)
time.sleep(3)
log('Testing Critical', 3)
pprint(vars())
