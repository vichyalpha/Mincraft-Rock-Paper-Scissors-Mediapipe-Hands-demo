# Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo

English README

JAPANESE README is here

[README_JAPANESE](https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/README_JP.md)

This API can play rock-paper-scissors with mincraft.

It uses mediapipe for image recognition and can play rock-paper-scissors with a virtual AI based on information from a webcam.

VOICEBOX is used for voice.



This API uses minecraft_remote by Naohiro2g.

　mediapipe (provided by google) https://mediapipe-studio.webapps.google.com/home

　VOICEBOX https://voicevox.hiroshiba.jp

　Naohiro2g https://github.com/Naohiro2g
 
　mincraft_remote https://github.com/Naohiro2g/minecraft_remote 
 
<img width=“1300” alt=“image” src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/image(1).png">
<img width=“1300” alt=“image” src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/image(2).png">
<img width=“1300” alt=“image” src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/image.png">
<img width=“500” alt=“image” src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%20(21).png">
# Prepare to play rock-paper-scissors

https://github.com/user-attachments/assets/d277dcee-fd45-4726-96e3-6c43e534381c

1. install Forge 1.16.5
　　　https://files.minecraftforge.net/net/minecraftforge/forge/index_1.16.5.html

   ![Download (3)](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/e2e9de27-5113-4a02-807b-1e4da3dc1f91)

2. install RemoteControllerMod-1.16.5 v0.05
　　　https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3363255

    ![download (4)](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/65c0c363-52e1-41f4-9b71-cf71aded1235)

3. start mincraft(forge1.16.5)

![NetherUpdateArtwork](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/28acd239-7094-43ac-8a8f-f79a9329ea85)

Run hands_mincraft.py !

![Python-logo-notext svg (1)](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/ae62b1b0-3ac0-458c-b5bc-93e8705a64d5)

====> Done!

# How to do janken

　Janken fields are generated at x=0 and z=0.
 
 Generate the world in minecraft super flat and run hands_mincraft.py. (It may take a few seconds to run.)
 
 Put your hand close to the webcam and play rock-paper-scissors (go, choki, par).
 
 Press “p” on the keyboard, and Zundamon of VOICEBOX will say “Goo first, then Jankenpon”.
 
 Then you can play rock-paper-scissors in Minecraft.
   
# How Image Recognition Works
　<img width=“500” alt=“image” src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%20(21).png">
 
Using mediapipe's hands_demo, detect 20 singular points on the finger.

Calculate the distance between each point and determine the shape of the hand.

# Examples of possible applications
　Rock-paper-scissors with two players
 
 　  Possible because mediapipe can recognize up to two or more moves. However, it is difficult because it is impossible to identify whose move it is.
   
　Sign language expression
 
 　It is possible to create a sign language by changing the singularity of a hand. However, it is necessary to create a large number of singular point combinations, and there is a possibility of many misrecognitions.
  


# Development environment

python 3.12.0 (poetry)
 https://www.python.org/downloads/release/python-3116/
 
forge 1.16.5
 https://files.minecraftforge.net/net/minecraftforge/forge/index_1.16.5.html

RemoteControllerMod 1.16.5 v0.05
 https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3363255
