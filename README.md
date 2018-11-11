# Virtual Keyboard
A tool by Scott Langridge :)

## What is Virtual Keyboard?
Virtual keyboard is a tool in the form of a python class designed to be used within other programs to send keystrokes as if sent by the user. For example: I will be personally using it to tab into a window and hit space to pause a video, before tabbing back out as part of another project.

## Methods:
* decode(string):
  * Decodes a code from a string input, using the CODE_DICT dictionary in CODE_DICT
* key_down(string)
  * Presses down a key
* key_up(string)
  * Releases a key
* key_stroke(string)
  * Presses down then releases a key
* type(string)
  * Presses down keys in string in order
  * Surround a code with #s to enter that as one whole code
    * Eg: '#tab#' presses the tab key
* keys_down_then_release(string)
  * Does the same as type, except that every key is held until the last one is pressed
  * Useful for keyboard shortcuts

## Custom Macros
You can enter your own custom macros to avoid having to keep typing long and unsightly code into type() or keys_down_then_release(). 

Do this by adding them into CUSTOM_CODES in CODE_DICT. An example and alt tab are already there to show you how to format it.
