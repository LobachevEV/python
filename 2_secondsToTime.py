if __name__ == '__main__':
    timeInSeconds = int(input('Enter time in seconds: '))
    seconds = timeInSeconds % 60
    minutes = timeInSeconds // 60
    hours = 0
    if minutes >= 60:
        hours = minutes // 60
        minutes = minutes % 60
    timeString = '{hours:02g}:{minutes:02g}:{seconds:02g}'
    print(timeString.format(hours=hours, minutes=minutes, seconds=seconds))
