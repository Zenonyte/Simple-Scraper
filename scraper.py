import os


def run(count):
    import requests
    num = 1
    rmv = ['"leaderboardName"', '"score"']
    while True:
        s = requests.get(f'https://x9c98fh3ng.execute-api.eu-west-1.amazonaws.com/production/leaderboard?campaignId={num}&limit=100') # Log URL, num being the campaign's number.
        t = s.text
        if t != '[]':
            t = t.translate({ord(c): None for c in '[]'})
            t_l = t.split('},{')
            retry = True
            while retry:
                try:
                    f = open(f'Logs/{num}.txt', 'wb')
                    retry = False
                except FileNotFoundError:
                    print(f'{num}: Folder doesn\'t exist, creating.. ')
                    import os
                    os.mkdir('Logs')
                    print('Folder created.')
            for i in t_l: # Code for reformatting & beautifying the data.
                i_l = i.split(',')
                i_l.reverse()
                add_colon = True
                for x in i_l:
                    for y in rmv:
                        x = x.replace(y, '')
                    f.write(x.translate({ord(c): None for c in '{}:\"'}).encode('utf-8'))
                    if add_colon:
                        f.write(':'.encode('utf-8'))
                        add_colon = False
                f.write('\n'.encode('utf-8'))
            f.close()
            print(f'Saved {num}. ({count})')
            count += 1
        else:
            print(f'{num} is empty. ')
        num += 1


def rem():
    import shutil
    try:
        shutil.rmtree('Logs')
        print('Success. ')
        return True
    except OSError as e:
        print(e)
        return False


while True:
    log_count = 0
    try:
        for path in os.listdir('Logs/'):
            log_count += 1
        print(f'{log_count} logs stored. ')
    except FileNotFoundError:
        print('No logs stored. ')
    command = str(input('> ')).lower()
    if command == 'run':
        run(1)
    elif command == 'rem':
        rem()
    elif command in ['help', 'cmds', 'cmd', '?']:
        print('run - downloads logs\nrem - removes logs\nhelp, cmds, cmd, ? - lists commands')
    else:
        print('Wrong command. ')
    print('\n')
