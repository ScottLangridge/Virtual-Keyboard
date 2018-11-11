from time import sleep
from code_dict import CODE_DICT
from code_dict import CUSTOM_CODES
import ctypes


class VirtualKeyboard:
    #Set custom codes to matching definitions for user defined quick codes
    def __init__(self):
        self.user32 = ctypes.windll.user32


    #Returns code from key
    def decode(self, key):
        return CODE_DICT[key.lower()]


    #Presses down key
    def key_down(self, key):
        self.user32.keybd_event(self.decode(key), 0, 0, 0)
        sleep(0.1)


    #Lets go of key
    def key_up(self, key):
        self.user32.keybd_event(self.decode(key), 0, 2, 0)
        sleep(0.1)


    #Quickly presses then lets go of key
    def key_stroke(self, key):
        self.key_down(key)
        self.key_up(key)


##    Type whole messages. Letters will be read as keys, except # which denotes
##    the start of a multi-char key. EG: To write:
##
##    hello
##        world
##
##    You should enter: "hello#enter##tab#world
    def type(self, keys):
        if keys in CUSTOM_CODES.keys():
            self.type(CUSTOM_CODES[keys])
        else:
            code = ''
            in_code = False

            for char in keys:
                if char == '#':
                    if in_code:
                        self.key_stroke(code)
                        code = ''
                        in_code = False
                    else:                            
                        in_code = True
                        
                elif in_code:
                    code = code + str(char)
                else:
                    self.key_stroke(str(char))


    #Presses keys down one by one then releases together.
    #Good for things like "#alt##tab#" or "#ctrl##alt##delete#"
    def hold_keys(self, keys):
        if keys in CUSTOM_CODES.keys():
            self.hold_keys(CUSTOM_CODES[keys])
        else:
            code = ''
            in_code = False

            for char in keys:
                if char == '#':
                    if in_code:
                        self.key_down(code)
                        code = ''
                        in_code = False
                    else:                            
                        in_code = True
                        
                elif in_code:
                    code = code + str(char)
                else:
                    self.key_down(str(char))

            for char in keys:
                if char == '#':
                    if in_code:
                        self.key_up(code)
                        code = ''
                        in_code = False
                    else:                            
                        in_code = True
                        
                elif in_code:
                    code = code + str(char)
                else:
                    self.key_up(str(char))
