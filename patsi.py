import sys
import cmd
import multiprocessing
import subprocess
import os
import http.client
import atexit
import code
import readline
import pyaudio
import random
from colors import Color
from eq import Equilizer
import speech_recognition as sr

class Patsi(cmd.Cmd):
    
    def do_eq(self, line):
        cnum1 = "48"
        cnum2 = "5"
        cube = 5**4
        pre = "\033[" + cnum1 + ";" + cnum2 + ";"
        block = "m       "
        RESET = "\033[0;0m"
        for color in range(0, cube, 1):
            bseq0 = "\033[0;0;m"
            color1 = str(random.randrange(16, 51, 1))
            color2 = str(random.randrange(52, 87, 1))
            color3 = str(random.randrange(88, 123, 1))
            color4 = str(random.randrange(124, 159, 1))
            color5 = str(random.randrange(160, 195, 1))
            color6 = str(random.randrange(196, 231, 1))
            bseq1 = pre + color1
            bseq2 = pre + color2
            bseq3 = pre + color3
            bseq4 = pre + color4
            bseq5 = pre + color5
            bseq6 = pre + color6
            sys.stdout.write(bseq1 + block + bseq0)
            sys.stdout.write(bseq2 + block + bseq0)
            sys.stdout.write(bseq3 + block + bseq0)
            sys.stdout.write(bseq4 + block + bseq0)
            sys.stdout.write(bseq5 + block + bseq0)
            sys.stdout.write(bseq6 + block + bseq0)
            sys.stdout.flush()
            os.system("clear")
        return self
            
    def do_listen(self, line):
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
            heard = r.recognize_google(audio)
        print(heard)

    def do_speak(self, line):
        listen_cmd = "gtts-cli '"  + line + "' --output patsy.mp3"
        listen = os.popen(listen_cmd)
        listen.close()
        speak_cmd = "afplay patsy.mp3"
        speak = os.popen(speak_cmd)
        print(line)
        self.last_output = speak
        os.system("clear")
        #sys.stdout.write(YELLOW)
        speak.close()

    def do_sing(self, line):
        sing_cmd = "afplay Crazy.mp3"
        sing = os.popen(sing_cmd)
        print(line)
        self.last_output = sing
        os.system("clear")
        sing.close()
    
    def do_shell(self, line):
        "Run a shell command"
        print("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output

    def do_list(self, path):  
        path = '.'
        files = os.listdir(path)
        for name in files:
            print(name)

    def do_emote(self, line):
        eq()

    #def main(self, line):
    #    p1 = multiprocessing.Process(target=emote)
    #    p2 = multiprocessing.Process(target=emote)
    #    p1.start()
    #    p2.start
    #    p1.join()
    #    p2.join

if __name__ == '__main__':
   Patsi()