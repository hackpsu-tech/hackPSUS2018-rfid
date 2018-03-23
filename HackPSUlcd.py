import I2C_LCD_Driver
from time import *
mylcd = I2C_LCD_Driver.lcd()
#some sort of call to server?
'''
https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

'''
class Debug:
 def __init__(self,wifi,location,scan,status):
  self.wifi = wifi
  self.location = location
  self.scan = scan
  self.status = status
 def displayDebug(self):
  padding = " " * 16
  display_string = "Wifi:{}location:{}Scan:{}Status:{}".format(self.wifi,self.location,self.scan,self.status)
  padded_string = display_string + padding
 #to scroll
  for i in range (0, len(display_string)):
   lcd_text = padded_string[((len(display_string)-1)-i):-i]
   mylcd.lcd_display_string(lcd_text,1)
   sleep(0.2)
   mylcd.lcd_display_string(padding[(15+i):i], 1)

class Hacker:
 def __init__(self,name,arg1,arg2):
  self.name = name
  self.arg1 = arg1
  self.arg2 = arg2
 def displayHack(self):
  mylcd = I2C_LCD_Driver.lcd()
  str_padding = " " * 16
  my_long_string = "Scrolling arg1:{}Scrolling arg2:{}".format(self.arg1,self.arg2)
  my_long_string = str_padding + my_long_string
  mylcd.lcd_display_string(self.name,1)
  for i in range (0, len(my_long_string)):
   lcd_text = my_long_string[i:(i+16)]
   mylcd.lcd_display_string(lcd_text,2)
   sleep(0.2)
   mylcd.lcd_display_string(str_padding,2)

class Lunch:
 def __init__(self, name, rep, diet):
  self.name = name
  self.rep = rep
  self.diet = diet
 def displayLunch(self):
class Debug:
 def __init__(self,wifi,location,scan,status):
  self.wifi = wifi
  self.location = location
  self.scan = scan
  self.status = status
 def displayDebug(self):
  padding = " " * 16
  display_string = "Wifi:{}location:{}Scan:{}Status:{}".format(self.wifi,self.location,self.scan,self.status)
  padded_string = display_string + padding
 #to scroll
  for i in range (0, len(display_string)):
   lcd_text = padded_string[((len(display_string)-1)-i):-i]
   mylcd.lcd_display_string(lcd_text,1)
   sleep(0.2)
   mylcd.lcd_display_string(padding[(15+i):i], 1)

class Hacker:
 def __init__(self,name,arg1,arg2):
  self.name = name
  self.arg1 = arg1
  self.arg2 = arg2
 def displayHack(self):
  mylcd = I2C_LCD_Driver.lcd()
  str_padding = " " * 16
  my_long_string = "Scrolling arg1:{}Scrolling arg2:{}".format(self.arg1,self.arg2)
  my_long_string = str_padding + my_long_string
  mylcd.lcd_display_string(self.name,1)
  for i in range (0, len(my_long_string)):
   lcd_text = my_long_string[i:(i+16)]
   mylcd.lcd_display_string(lcd_text,2)
   sleep(0.2)
   mylcd.lcd_display_string(str_padding,2)

class Lunch:
 def __init__(self, name, rep, diet):
  self.name = name
  self.rep = rep
  self.diet = diet
 def displayLunch(self):
  if self.rep ==  "True":
   self.rep= "T"
  else:
   self.rep ="F"
  if self.diet == None:
   self.diet = "F"
  else:
   self.diet = "T"
  str = "rep:{} diet:{}".format(self.rep,self.diet)
  mylcd = I2C_LCD_Driver.lcd()
  mylcd.lcd_display_string(self.name,1)
  mylcd.lcd_display_string(str,2)

