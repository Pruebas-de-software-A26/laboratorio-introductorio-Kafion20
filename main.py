import operations
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filemode = "w",
    filename = "test.log" 
)

if __name__  =="__main__":

    logging.info('TEST CASE 1')
    resullt = operations.add(1,2)

    if resullt == 3:
        logging.info('PASS')
    else:
        logging.error('FAIL')

    logging.info('TEST CASE 2')
    resultado = operations.power(2,3)
    if resultado == 8:
        logging.info('PASS')
    else:
        logging.info('FAIL')
    logging.error('no sireve la funcion de  power')







'''
    result = operations.add(6,7)
    logging.info(f"Result = {result}")
    logging.warning("lo que sea")
    logging.error('Error')
    logging.debug('el valor en a y b son ...')
    logging.critical('buen critico ')
'''