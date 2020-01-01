import cmd
import os
import http.client
import atexit
import code
import readline
import pyaudio
import speech_recognition as sr

readline.parse_and_bind('tab: complete')
readline.parse_and_bind('set editing-mode vi')

while True:
    line = input('Prompt ("stop" to quit): ')
    if line == 'stop':
        break
    print ('ENTERED: "%s"' % line)


class HelloWorld(cmd.Cmd):
    """Sound Electric Light Frequency"""
    
    FRIENDS = [ 'hank', 'patsy' ]
    last_output = ''
    STRANGERS = [ 'stranger', 'dude' ]
    myname = 'jeremy'
    prompt = 'j: '
            
    def do_hi(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = person + ': hi! j'
        elif person:
            greeting = person + ": hello, "
        else:
            greeting = 'do I know you'
        print(greeting)
        self.prompt = 'me: '
        
    def complete_hi(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
    
    def do_hello(self, person):
        "Greet the person"
        if person and person in self.STRANGERS:
            greeting = person + ': hi' 
        elif person:
            greeting = person + ": hello, "
        else:
            greeting = 'excuse me'
        print(greeting)
    
    def complete_hello(self, text, line, begidx, endidx):
        if not text:
            completions = self.STRANGERS[:]
        else:
            completions = [ f
                            for f in self.STRANGERS
                            if f.startswith(text)
                            ]
        return completions
    
    def do_who(self, line):
        print("who are you?")
    
    def do_shell(self, line):
        "Run a shell command"
        print("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output
    
    def do_echo(self, line):
        # Obviously not robust
        print(line.replace('$out', self.last_output))
    
    def do_speak(self, line):
        listen_cmd = "gtts-cli '"  + line + "' --output patsy.mp3"
        listen = os.popen(listen_cmd)
        listen.close()
        speak_cmd = "afplay patsy.mp3"
        speak = os.popen(speak_cmd)
        print(line)
        self.last_output = speak
        speak.close()
    
    def do_open(self, line):
        fo = open("foo.txt", "rw+")
        print("opening: ", fo.name)
        line = fo.readline(line)
        print("Read Line: %s" % (line))
        fo.close()
    
    def do_read(self, line):
        line = fo.readline(line)
        print("Read Line: %s" % (line))
        
    def do_close(self, line):
        fo.close()
    
    def do_list(dir_list, path):  
        path = '.'
        files = os.listdir(path)
        for name in files:
            print(name)
  
    def do_files(file_list, path):
        s = "%s%d%s"%("\n", len(file_list), " files of " + os.path.abspath(path)) 
        l = len(s) 
        print(s) 
        print("="*l)
        for index, file in enumerate(file_list): 
            print(str(index+1) + ") ", file)
    
    def do_newt(self, line):
        new_cmd = "vi "  + line
        save_cmd = ":w:q"
        new = os.popen(new_cmd)
        save = os.popen(save_cmd)
        
    def do_run(self, line):
        print("running shell command:", line)
        output = os.popen('open -a "' + line + '"').read()
        print(output)
        self.last_output = output
        
    def do_web(self, line):
        conn = http.client.HTTPSConnection(line)
        conn.request("GET", "/")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        data1 = r1.read()
        print(data1)

    def do_listen(self, line):
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
            heard = r.recognize_google(audio)
        print(heard)

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()