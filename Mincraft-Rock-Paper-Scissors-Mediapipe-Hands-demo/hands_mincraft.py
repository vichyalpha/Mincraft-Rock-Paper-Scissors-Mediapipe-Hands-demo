import cv2
import mediapipe as mp
import time
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import keyboard
import scipy.io.wavfile as wav 
import sounddevice as sd
import random


from mcje.minecraft import Minecraft
import param_MCJE as param





mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Mediapipe Hands demo in Minecraft')

you = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
       0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,
       0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,
       0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,
       0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,
       0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,
       0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

ai  = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,
       0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,
       0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,
       0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,
       0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,
       0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

win = [0,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,
       0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,
       0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,
       0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,
       0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,]

lose= [1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,
       1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,
       1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,
       1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,
       1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,]

draw= [1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,
       1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,
       1,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,1,
       1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,
       1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,]

x=0
y=0
for y in range(49):
   for x in range(110):
      mc.setBlock(100-x,53-y,1,param.IRON_BLOCK)
      x=0


x=0
y=0
for y in range(7):
   for x in range(18):
      if you[x+18*y] == 1:
         mc.setBlock(40-x,49-y,0,param.GOLD_BLOCK)
      else:
         mc.setBlock(40-x,49-y,0,param.AIR)
      x += 1
   y += 1
   x=1

x=0
y=0
for y in range(7):
   for x in range(18):
      if ai[x+18*y] == 1:
         mc.setBlock(69-x,49-y,0,param.SEA_LANTERN_BLOCK)
      else:
         mc.setBlock(69-x,49-y,0,param.AIR)
      x += 1
   y += 1
   x=1

# グー=1,チョキ=2,パー=3
def jyanken_gu_set():
    x=1
    y=0
    for y in range(20):
       for x in range(20):
          if jyanken_gu[x+20*y] == 1:
            mc.setBlock(40-x,40-y,0,param.GOLD_BLOCK)
          else:
            mc.setBlock(40-x,40-y,0,param.AIR)
          x += 1
       y += 1
       x=1

def jyanken_tyoki_set():
    x=1
    y=0
    for y in range(20):
       for x in range(20):
          if jyanken_tyoki[x+20*y] == 1:
            mc.setBlock(40-x,40-y,0,param.GOLD_BLOCK)
          else:
            mc.setBlock(40-x,40-y,0,param.AIR)
          x += 1
       y += 1
       x=1

def jyanken_pa_set():
    x=1
    y=0
    for y in range(20):
       for x in range(20):
          if jyanken_pa[x+20*y] == 1:
            mc.setBlock(40-x,40-y,0,param.GOLD_BLOCK)
          else:
            mc.setBlock(40-x,40-y,0,param.AIR)
          x += 1
       y += 1
       x=1

def jyanken_ai_gu_set():
    x=1
    y=0
    for y in range(20):
       for x in range(20):
          if jyanken_gu[x+20*y] == 1:
            mc.setBlock(70-x,40-y,0,param.SEA_LANTERN_BLOCK)
          else:
            mc.setBlock(70-x,40-y,0,param.AIR)
          x += 1
       y += 1
       x=1

def jyanken_ai_tyoki_set():
    x=1
    y=0
    for y in range(20):
       for x in range(20):
          if jyanken_tyoki[x+20*y] == 1:
            mc.setBlock(70-x,40-y,0,param.SEA_LANTERN_BLOCK)
          else:
            mc.setBlock(70-x,40-y,0,param.AIR)
          x += 1
       y += 1
       x=1

def jyanken_ai_pa_set():
    x=1
    y=0
    for y in range(20):
       for x in range(20):
          if jyanken_pa[x+20*y] == 1:
            mc.setBlock(70-x,40-y,0,param.SEA_LANTERN_BLOCK)
          else:
            mc.setBlock(70-x,40-y,0,param.AIR)
          x += 1
       y += 1
       x=1


def kati():
   mc.postToChat('You Win!')
   x=0
   y=0
   for y in range(5):
      for x in range(19):
         if win[x+19*y] == 1:
            mc.setBlock(55-x,20-y,0,param.STONE)
         else:
            mc.setBlock(55-x,20-y,0,param.AIR)
         x += 1
      y += 1
      x=1
        
def make():
   mc.postToChat('You Lose.')
   x=0
   y=0
   for y in range(5):
      for x in range(19):
         if lose[x+19*y] == 1:
            mc.setBlock(55-x,20-y,0,param.STONE)
         else:
            mc.setBlock(55-x,20-y,0,param.AIR)
         x += 1
      y += 1
      x=1

def draws():
   mc.postToChat('draw.')
   x=0
   y=0
   for y in range(5):
      for x in range(19):
         if draw[x+19*y] == 1:
            mc.setBlock(55-x,20-y,0,param.STONE)
         else:
            mc.setBlock(55-x,20-y,0,param.AIR)
         x += 1
      y += 1
      x=1

jyanken_gu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,
              0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,
              0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,
              0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,
              0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,
              0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,
              0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,
              0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,
              0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,
              0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,
              0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,
              0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,
              0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
              0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

jyanken_tyoki = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,
                 0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,
                 0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,
                 0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,
                 0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,
                 0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,
                 0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,
                 0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,
                 0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
                 0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

jyanken_pa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,
              0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,
              0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,
              0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,
              0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,
              0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,
              0,0,1,0,0,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,
              0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,
              0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,
              0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,
              0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,
              0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,
              0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,
              0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,
              0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
              0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()
vol = 0
volumeBar = 400
volumePercent = 0
muteStatus = False

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

previousTime = 0

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    lml = []
    xl = []
    yl = []
    box = []
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

      for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
        h, w, _ = image.shape
        xc, yc = int(lm.x * w), int(lm.y * h)
        lml.append([id, xc, yc])
        xl.append(xc)
        yl.append(yc)


      # 親指
      x1, y1 = lml[1][1], lml[1][2]
      x2, y2 = lml[4][1], lml[4][2]
      cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
      cv2.circle(image, (x1, y1), 10, (255,0,0), cv2.FILLED)
      cv2.circle(image, (x2, y2), 10, (255,0,0), cv2.FILLED)
      cv2.line(image, (x1, y1), (x2, y2), (255,0,0), 3)
      oyayubi_distance = math.hypot(x2 - x1, y2 - y1)

      # 人差し指
      x1, y1 = lml[5][1], lml[5][2]
      x2, y2 = lml[8][1], lml[8][2]
      cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
      cv2.circle(image, (x1, y1), 10, (255, 244, 32), cv2.FILLED)
      cv2.circle(image, (x2, y2), 10, (255, 244, 32), cv2.FILLED)
      cv2.line(image, (x1, y1), (x2, y2), (255, 244, 32), 3)
      hitosasi_distance = math.hypot(x2 - x1, y2 - y1)

      # 中指
      x1, y1 = lml[9][1], lml[9][2]
      x2, y2 = lml[12][1], lml[12][2]
      cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
      cv2.circle(image, (x1, y1), 10, (0, 192, 0), cv2.FILLED)
      cv2.circle(image, (x2, y2), 10, (0, 192, 0), cv2.FILLED)
      cv2.line(image, (x1, y1), (x2, y2), (0, 192, 0), 3)
      nakayubi_distance = math.hypot(x2 - x1, y2 - y1)

      # 薬指
      x1, y1 = lml[13][1], lml[13][2]
      x2, y2 = lml[16][1], lml[16][2]
      cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
      cv2.circle(image, (x1, y1), 10, (0,32,255), cv2.FILLED)
      cv2.circle(image, (x2, y2), 10, (0,32,255), cv2.FILLED)
      cv2.line(image, (x1, y1), (x2, y2), (0,32,255), 3)
      kusuriyubi_distance = math.hypot(x2 - x1, y2 - y1)

      # 小指
      x1, y1 = lml[17][1], lml[17][2]
      x2, y2 = lml[20][1], lml[20][2]
      cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
      cv2.circle(image, (x1, y1), 10, (160,32,255), cv2.FILLED)
      cv2.circle(image, (x2, y2), 10, (160,32,255), cv2.FILLED)
      cv2.line(image, (x1, y1), (x2, y2), (160,32,255), 3)
      koyubi_distance = math.hypot(x2 - x1, y2 - y1)

      xmin, xmax = min(xl), max(xl)
      ymin, ymax = min(yl), max(yl)
      box = xmin, ymin, xmax, ymax
      cv2.rectangle(image, (box[0] - 20, box[1] - 20), (box[2] + 20, box[3] + 20), (255, 255, 0), 2)
      area = (box[2] - box[0]) * (box[3] - box[1]) // 100

    # #じゃんけん判定
    #   if koyubi_distance < 50 and hitosasi_distance < 50 and nakayubi_distance < 50 and kusuriyubi_distance < 50 and oyayubi_distance != 0:
    #     print("グー")
    
    #   if koyubi_distance < 50 and hitosasi_distance > 100 and nakayubi_distance > 100 and kusuriyubi_distance < 50 and oyayubi_distance != 0:
    #     print("チョキ")

    #   if koyubi_distance > 50 and hitosasi_distance > 100 and nakayubi_distance > 100 and kusuriyubi_distance > 100 and oyayubi_distance != 0:
    #     print("パー")

      if keyboard.is_pressed('p'):
        wav_file_path = "C:\Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo\Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo\jyanken.wav" # ファイルのPath
        fs, data = wav.read(wav_file_path) # サンプリング周波数(fs)とデータを取得
        sd.play(data, fs)
        time.sleep(4)
        # 1から3の間でランダムな整数を1つ出力
        jyanken_ai = random.randint(1, 3)
        if jyanken_ai == 1:
           jyanken_ai_gu_set()
           print("AI：グー")
        if jyanken_ai == 2:
           jyanken_ai_tyoki_set()
           print("AI：チョキ")
        if jyanken_ai == 3:
           jyanken_ai_pa_set()
           print("AI：パー")
        #じゃんけん判定
        if koyubi_distance < area/5 and hitosasi_distance < area/10 and nakayubi_distance < area/10 and kusuriyubi_distance < area/10 and oyayubi_distance != 0:
          print("自分：グー")
          jyanken_gu_set()
          if jyanken_ai == 1:
             print("draw")
             draws()
          if jyanken_ai == 2:
             print("win")
             kati()
          if jyanken_ai == 3:
             print("lose")
             make()
        if koyubi_distance < area/7 and hitosasi_distance > area/5 and nakayubi_distance > area/5 and kusuriyubi_distance < area/7 and oyayubi_distance != 0:
          print("自分：チョキ")
          jyanken_tyoki_set()
          if jyanken_ai == 1:
             print("lose")
             make()
          if jyanken_ai == 2:
             print("draw")
             draws()
          if jyanken_ai == 3:
             print("win")
             kati()
        if koyubi_distance > area/10 and hitosasi_distance > area/10 and nakayubi_distance > area/10 and kusuriyubi_distance > area/10 and oyayubi_distance != 0:
          print("自分：パー")
          jyanken_pa_set()
          if jyanken_ai == 1:
             print("win")
             kati()
          if jyanken_ai == 2:
             print("lose")
             make()
          if jyanken_ai == 3:
             print("draw")
             draws()
        

        

      cv2.imshow('MediaPipe Hands', image)
    
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()