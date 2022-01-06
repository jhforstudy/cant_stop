def printlogo():
    print(" _____                _  _       _____  _                 ")
    print("/  __ \              ( )| |     /  ___|| |                ")
    print("| /  \/  __ _  _ __  |/ | |_    \ `--. | |_   ___   _ __  ")
    print("| |     / _` || '_ \    | __|    `--. \| __| / _ \ | '_ \ ")
    print("| \__/\| (_| || | | |   | |_    /\__/ /| |_ | (_) || |_) |")
    print(" \____/ \__,_||_| |_|    \__|   \____/  \__| \___/ | .__/ ")
    print("                                                   | |    ")
    print("                                                   |_|    ")
    print("Ver 2.0.1.")

def color1(string):
    return ("\033[92m" + string + "\033[37m")

def color2(string):
    return ("\033[94m" + string + "\033[37m")
    
def color3(string):
    return ("\033[95m" + string + "\033[37m")

def color4(string):
    return ("\033[33m" + string + "\033[37m")

def color5(string):
    return ("\033[90m" + string + "\033[37m")