def printRuntime(seconds,finished=False):
    seconds = int(seconds)
    status = 'has been running for'
    if finished == True:
        status = 'finished in'

    if seconds < 60:
        print('The script {} {} seconds'.format(status,seconds))
        return
    elif seconds < 3600:
        minutes = seconds // 60
        seconds = seconds - 60*minutes
        print('The script {} {} minutes & {} seconds'.format(status,minutes,seconds))
        return
    else:
        hours = seconds // 3600
        minutes = (seconds - 3600*hours) // 60
        seconds = seconds - 3600*hours - 60*minutes
        print('The script {} {} hours, {} minutes & {} seconds'.format(status,hours,minutes,seconds))
        return

import time
startTime = time.time()
