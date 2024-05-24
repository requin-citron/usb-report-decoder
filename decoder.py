#!/bin/python3

from colorama import Fore
from sys import argv, stdin

# Flag
L_SHIFT = 0x02
L_CONTR = 0x01
L_ALT   = 0x04

R_SHIFT = 0x20
R_CONTR = 0x10
R_ALT   = 0x40

# USB keyboard HID key codes
usb_codes = {
   0x4   : ['q', 'Q']               ,0x5   : ['b', 'B']               ,0x6   : ['c', 'C']               ,0x7   : ['d', 'D']               ,
   0x8   : ['e', 'E']               ,0x9   : ['f', 'F']               ,0xa   : ['g', 'G']               ,0xb   : ['h', 'H']               ,
   0xc   : ['i', 'I']               ,0xd   : ['j', 'J']               ,0xe   : ['k', 'K']               ,0xf   : ['l', 'L']               ,
   0x10  : [',', '?']               ,0x11  : ['n', 'N']               ,0x12  : ['o', 'O']               ,0x13  : ['p', 'P']               ,
   0x14  : ['a', 'A']               ,0x15  : ['r', 'R']               ,0x16  : ['s', 'S']               ,0x17  : ['t', 'T']               ,
   0x18  : ['u', 'U']               ,0x19  : ['b', 'B']               ,0x1a  : ['z', 'Z']               ,0x1b  : ['x', 'X']               ,
   0x1c  : ['y', 'Y']               ,0x1d  : ['w', 'W']               ,0x1e  : ['&', '1', '¹']          ,0x1f  : ['é', '2', '~']          ,
   0x20  : ['"', '3', '#']          ,0x21  : ["\\'", '4', '{']        ,0x22  : ['(', '5', '[']          ,0x23  : ['-', '6', '|']          ,
   0x24  : ['è', '7', '`']          ,0x25  : ['_', '8', '\\']         ,0x26  : ['ç', '9', '^']          ,0x27  : ['à', '0', '@']          ,
   0x28  : ['Enter']                ,0x29  : ['Esc']                  ,0x2a  : ['Backspace']            ,0x2b  : ['\t']                   ,
   0x2c  : [' ']                    ,0x2d  : [')', '°', ']']          ,0x2e  : ['=', '+', '}']          ,0x2f  : ['^', '¨']               ,
   0x30  : ['$', '$', '¤']          ,0x31  : ['Backslash']            ,0x32  : ['*', 'µ']               ,0x33  : ['m', 'M']               ,
   0x34  : ['ù', '%']               ,0x35  : ['Superscript 2']        ,0x36  : [';', '.']               ,0x37  : [':', '/']               ,
   0x38  : ['!', '§']               ,0x39  : ['CapsLock']             ,0x3a  : ['F1']                   ,0x3b  : ['F2']                   ,
   0x3c  : ['F3']                   ,0x3d  : ['F4']                   ,0x3e  : ['F5']                   ,0x3f  : ['F6']                   ,
   0x40  : ['F7']                   ,0x41  : ['F8']                   ,0x42  : ['F9']                   ,0x43  : ['F10']                  ,
   0x44  : ['F11']                  ,0x45  : ['F12']                  ,0x46  : ['Print Screen']         ,0x47  : ['Scroll Lock']          ,
   0x48  : ['Pause']                ,0x49  : ['Insert']               ,0x4a  : ['Home']                 ,0x4b  : ['Page Up']              ,
   0x4c  : ['Delete']               ,0x4d  : ['End']                  ,0x4e  : ['Page Down']            ,0x4f  : ['Right']                ,
   0x50  : ['Left']                 ,0x51  : ['Down']                 ,0x52  : ['Up']                   ,0x53  : ['NmLock']               ,
   0x54  : ['/']                    ,0x55  : ['*']                    ,0x56  : ['-']                    ,0x57  : ['+']                    ,
   0x58  : ['Enter']                ,0x59  : ['1']                    ,0x5a  : ['2']                    ,0x5b  : ['3']                    ,
   0x5c  : ['4']                    ,0x5d  : ['5']                    ,0x5e  : ['6']                    ,0x5f  : ['7']                    ,
   0x60  : ['8']                    ,0x61  : ['9']                    ,0x62  : ['0']                    ,0x63  : ['Keypad Period']        ,
   0x64  : ['<', '>']               ,0x65  : ['App']                  ,0x66  : ['Keyboard Status']      ,0x67  : ['Keypad Equal']         ,
   0x68  : ['F13']                  ,0x69  : ['F14']                  ,0x6a  : ['F15']                  ,0x6b  : ['F16']                  ,
   0x6c  : ['F17']                  ,0x6d  : ['F18']                  ,0x6e  : ['F19']                  ,0x6f  : ['F20']                  ,
   0x70  : ['F21']                  ,0x71  : ['F22']                  ,0x72  : ['F23']                  ,0x73  : ['F24']                  ,
   0x74  : ['Exec']                 ,0x75  : ['Help']                 ,0x76  : ['Menu']                 ,0x77  : ['Select']               ,
   0x78  : ['Stop']                 ,0x79  : ['Again']                ,0x7a  : ['Undo']                 ,0x7b  : ['Cut']                  ,
   0x7c  : ['Copy']                 ,0x7d  : ['Paste']                ,0x7e  : ['Find']                 ,0x7f  : ['Mute']                 ,
   0x80  : ['Volume Up']            ,0x81  : ['Volume Down']          ,0x82  : ['Locking Caps Lock']    ,0x83  : ['Locking Num Lock']     ,
   0x84  : ['Locking Scroll Lock']  ,0x85  : ['Keypad Comma']         ,0x86  : ['Keypad Equal AS400']   ,0x87  : ['International1']       ,
   0x88  : ['International2']       ,0x89  : ['International3']       ,0x8a  : ['International4']       ,0x8b  : ['International5']       ,
   0x8c  : ['International6']       ,0x8d  : ['International7']       ,0x8e  : ['International8']       ,0x8f  : ['International9']       ,
   0x90  : ['LANG1']                ,0x91  : ['LANG2']                ,0x92  : ['LANG3']                ,0x93  : ['LANG4']                ,
   0x94  : ['LANG5']                ,0x95  : ['LANG6']                ,0x96  : ['LANG7']                ,0x97  : ['LANG8']                ,
   0x98  : ['LANG9']                ,0x99  : ['Alternate Erase']      ,0x9a  : ['SysReq']               ,0x9b  : ['Cancel']               ,
   0x9c  : ['Clear']                ,0x9d  : ['Prior']                ,0x9e  : ['Return']               ,0x9f  : ['Separator']            ,
   0xa0  : ['Out']                  ,0xa1  : ['Oper']                 ,0xa2  : ['Clear Again']          ,0xa3  : ['CrSel Props']          ,
   0xa4  : ['ExSel']                ,0xb0  : ['Keypad 00']            ,0xb1  : ['Keypad 000']           ,0xb2  : ['1000 Separator']       ,
   0xb3  : ['Decimal Separator']    ,0xb4  : ['Currency Unit']        ,0xb5  : ['Currency SubUnit']     ,0xb6  : ['Keypad Left Parenthesis'],
   0xb7  : ['Keypad Right Parenthesis'],0xb8  : ['Keypad Left Brace']    ,0xb9  : ['Keypad Right Brace']   ,0xba  : ['Keypad Tab']           ,
   0xbb  : ['Keypad Backspace']     ,0xbc  : ['Keypad A']             ,0xbd  : ['Keypad B']             ,0xbe  : ['Keypad C']             ,
   0xbf  : ['Keypad D']             ,0xc0  : ['Keypad E']             ,0xc1  : ['Keypad F']             ,0xc2  : ['Keypad XOR']           ,
   0xc3  : ['Keypad Chevron']       ,0xc4  : ['Keypad Percent']       ,0xc5  : ['Keypad Less Than']     ,0xc6  : ['Keypad Greater Than']  ,
   0xc7  : ['Keypad BITAND']        ,0xc8  : ['Keypad AND']           ,0xc9  : ['Keypad BITOR']         ,0xca  : ['Keypad OR']            ,
   0xcb  : ['Keypad Colon']         ,0xcc  : ['Keypad Hash']          ,0xcd  : ['Keypad Space']         ,0xce  : ['Keypad At']            ,
   0xcf  : ['Keypad Exclamation']   ,0xd0  : ['Keypad Memory Store']  ,0xd1  : ['Keypad Memory Recall'] ,0xd2  : ['Keypad Memory Clear']  ,
   0xd3  : ['Keypad Memory Add']    ,0xd4  : ['Keypad Memory Subtract'],0xd5  : ['Keypad Memory Multiply'],0xd6  : ['Keypad Memory Divide'] ,
   0xd7  : ['Keypad Plus Minus']    ,0xd8  : ['Keypad Clear']         ,0xd9  : ['Keypad Clear Entry']   ,0xda  : ['Keypad Binary']        ,
   0xdb  : ['Keypad Octal']         ,0xdc  : ['Keypad Decimal']       ,0xdd  : ['Keypad Hexidecimal']   ,0xe0  : ['Left Control']         ,
   0xe1  : ['Left Shift']           ,0xe2  : ['Left Alt']             ,0xe3  : ['Left GUI']             ,0xe4  : ['Right Control']        ,
   0xe5  : ['Right Shift']          ,0xe6  : ['Right Alt']            ,0xe7  : ['Right GUI']            ,0xf0  : ['Function1']            ,
   0xf1  : ['Function2']            ,0xf2  : ['Function3']            ,0xf3  : ['Function4']            ,0xf4  : ['Function5']            ,
   0xf5  : ['Function6']            ,0xf6  : ['Function7']            ,0xf7  : ['Function8']            ,0xf8  : ['Function9']            ,
   0xf9  : ['Function10']           ,0xfa  : ['Function11']           ,0xfb  : ['Function12']           ,0xfc  : ['Function13']           ,
   0xfd  : ['Function14']           ,0xfe  : ['Function15']           ,0xff  : ['Function16']           ,0x100 : ['Lock1']                ,
   0x101 : ['Lock2']                ,0x102 : ['Lock3']                ,0x103 : ['Lock4']                ,0x104 : ['Lock5']                ,
   0x105 : ['Lock6']                ,0x106 : ['Lock7']                ,0x107 : ['Lock8']                ,0x108 : ['Lock9']                ,
   0x109 : ['Lock10']               ,0x10a : ['Lock11']               ,0x10b : ['Lock12']               ,0x10c : ['Lock13']               ,
   0x10d : ['Lock14']               ,0x10e : ['Lock15']               ,0x10f : ['Lock16']               ,0x110 : ['Latch1']               ,
   0x111 : ['Latch2']               ,0x112 : ['Latch3']               ,0x113 : ['Latch4']               ,0x114 : ['Latch5']               ,
   0x115 : ['Latch6']               ,0x116 : ['Latch7']               ,0x117 : ['Latch8']               ,0x118 : ['Latch9']               ,
   0x119 : ['Latch10']              ,0x11a : ['Latch11']              ,0x11b : ['Latch12']              ,0x11c : ['Latch13']              ,
   0x11d : ['Latch14']              ,0x11e : ['Latch15']              ,0x11f : ['Latch16']              ,0x120 : ['Next Layer']           ,
   0x121 : ['Previous Layer']                                        
}

def read_report(file):
   last = list()
   for line in file:
      line = line.decode("utf-8",errors="ignore") 
      if not 'Report: ' in line:
          continue
      
      line = line.strip().split('Report: ')[1]

      lst_code = [int(line[x:x+2],16) for x in range(0, len(line),2)]
      modifiers = lst_code[0]

      report = list(filter(lambda x: x!=0 and x not in last,lst_code[1:]))

      last = report + list(filter(lambda x: x!=0 and x in last,lst_code[1:]))
      if len(report):
         yield [modifiers] + report # add modifiers

if __name__ == "__main__":
   if len(argv) != 2:
      print(f"Usage: {argv[0]} ./example.cap")
      exit(1)

   file = open(argv[1], "rb") if argv[1]!="-" else stdin.buffer.raw # open file if name is not - else read from stdin
   caps_lock = False
   for report in read_report(file):
      modifiers      = report[0]
      index_modifier = int(caps_lock)

      if   (modifiers & L_SHIFT) or (modifiers & R_SHIFT):
         index_modifier = int(not caps_lock)
      elif (modifiers & L_ALT)   or (modifiers & R_ALT):
         index_modifier = 2
      elif (modifiers & L_CONTR) or (modifiers & R_CONTR):
         index_modifier = 3

      text = ""
      for el in report[1:]:
         lst_char = usb_codes.get(el) # char is a list 

         if el == 0x39:
            caps_lock      = not caps_lock
            index_modifier = int(caps_lock)

         if index_modifier < len(lst_char): # get correct char from list
            char = lst_char[index_modifier]
         else:
            char = lst_char[0]

         if char == "Enter":
            char += "\n"

         
         if len(char)>1: # not single char
            char = Fore.GREEN + char + Fore.RESET
         
         text += char
      
      print(text,end="")
