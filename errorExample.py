#! python
import traceback
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of he program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.error('i is ' + str(i) + ', total is ' + str(total))
    return total
def write_log():
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('the traceback info was written to errorInfo.txt')
factorial(5)

try:
    raise Exception('This is the error message.')
except:
    write_log()

door = 'open'
assert door == 'open','the door obviously needs to be "open" '
door = 'zzz'



