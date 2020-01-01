import termios, fcntl, sys, os
import random
import multiprocessing
import subprocess
from eq import Equilizer
import numpy as np
import simpleaudio as sa



""" def argsin():
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y

    if args.quiet:
        print(answer)
    elif args.verbose:
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
        input()
    else:
        print("{}^{} == {}".format(args.x, args.y, answer))
     """

home = "//Users/heremias"

async def Track(id):
    print("Hello Patsy")

async def Sub(id):
    process_time = random.randint(1,5)
    #await asyncio.sleep(process_time)
    print("Sub: {}, completed in {} seconds".format(id, process_time))
    
def getch():
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
                if c:
                    print("\r\nGot character", repr(c))
                    os.system("clear")
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def timer():
# =============================================================================
#     i = 1
#     # High Intensity
#     BLACK='\033[0;90m'       # Black
#     RED='\033[0;91m'         # Red
#     GREEN='\033[0;92m'       # Green
#     YELLOW='\033[0;93m'      # Yellow
#     BLUE='\033[0;94m'        # Blue
#     PURPLE='\033[0;95m'      # Purple
#     CYAN='\033[0;96m'        # Cyan
#     WHITE='\033[0;97m'       # White
# 
#     while i < 5000:
#         print("\r\n\r\nTime")
#         print(i, int(i/90), int(i/300), int((i/90)/30), flush=True)
#         sys.stdout.write(RED)
#         os.system("clear")
#         sys.stdout.write("\r\n")
#         i += 1
#     return
# =============================================================================
#    sys.stdout.write(GREEN)
    print("Welcome to Patsy ")

def tone():
    first = ("q","w","e","t","y","u","i")
    second = ("a","s","d","f","g","h","j","k")
    third = ("z","x","c","v","b","n","m",",",".")
    up = ("tab")
    down = ("shift")
    
    # =============================================================================
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Return:
    #         print "return pressed"
    #     else:
    #         QComboBox.keyPressEvent(self, event)
    # 
    # def event(self, event):
    #     if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab:
    #         print "tab pressed"
    #         return False
    #     return QWidget.event(self, event)
    # 
    # =============================================================================
    
    frequency = 440  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds
    
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)
    
    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)
    
    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    
    # Wait for playback to finish before exiting
    play_obj.wait_done()

def now():
    subprocess.call('afplay Crazy.mp3', shell=True)
    return
 
def patso():
    pateq = Equilizer()
    return

def main():
    p1 = multiprocessing.Process(target=now)
    p2 = multiprocessing.Process(target=patso)
    p3 = multiprocessing.Process(target=getch)
    p4 = multiprocessing.Process(target=getch)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

if __name__ == '__main__':
    try:
        main()
        #patsy = Patsi().cmdloop()
        #loop = asyncio.get_event_loop()
        #loop.set_debug(1)
        #loop.run_until_complete(main())
        #print(dl.result())
    except Exception as e:
        print(e)
        pass
    finally:
        print("finally")
        #Patsi(completekey=True)
        #loop.close()
        #Patsi().cmdloop(),,, """