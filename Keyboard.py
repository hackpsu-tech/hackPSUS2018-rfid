import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
keys=[['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]
class Keyboard():
   def __init__(self, columns=[21,20,16,12], rows=[19,13,6,5]):
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
   def getPin(self, length=3):
      vals=''
      while len(vals) < length:
         key=self.getKey()
         if key=='#':
            vals=vals[:-1]
         elif key == '*':
            vals=""
         else:
            print key
            vals+=key
      return vals
