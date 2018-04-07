import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BCM)
#Assume board layout
keys=[['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]

class HackPSUkeypad():
   def __init__(self, columns=[40,38,36,32], rows=[35,33,31,29]):
      self.cols=columns
      self.rows=rows
      for col in columns:
         GPIO.setup(col, GPIO.OUT)
      for row in rows:
         GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
   def __del__(self):
      GPIO.cleanup()
   def read(self, col, row):
      GPIO.output(col, GPIO.HIGH)
      found=GPIO.input(row)==GPIO.HIGH
      GPIO.output(col, GPIO.LOW)
      return found
   def getKey(self, blocking=True, timeout=5):
      start=time.time()
      found=False
      while True:
         for col in self.cols:
            for row in self.rows:
               if self.read(col,row):
                  while self.read(col,row):
                     pass
                  return self.getVal(col,row)
         if not blocking and time.time()-start > timeout:
            return None
         time.sleep(0.1)
   def getVal(self, col, row):
      return keys[self.rows.index(row)][self.cols.index(col)]
   def getPin(self):
      vals=''
      while True:
         key=self.getKey()
         print(str(key))
         if key=='#':
            break
         elif key == '*':
            vals=""
         else:
            vals+=key
      return vals
