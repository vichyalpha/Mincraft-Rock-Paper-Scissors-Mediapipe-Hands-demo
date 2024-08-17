# Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo

Japanese README

English READMEはこちら
[README_ENGLISH](https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/README_EN.md)

このAPIはmincraftでじゃんけんをすることができます。

じゃんけんを画像認識するためにmediapipeを使用し、Webカメラなどからの情報をもとに仮想のAIとじゃんけんをすることができます。

また音声として、VOICEBOXを使用しています。



※このAPIはNaohiro2g様のminecraft_remoteを使用しています。

　mediapipe(google提供)　https://mediapipe-studio.webapps.google.com/home

　VOICEBOX様　https://voicevox.hiroshiba.jp

　Naohiro2g様　https://github.com/Naohiro2g
 
　mincraft_remote https://github.com/Naohiro2g/minecraft_remote 
 
<img width="1300" alt="image" src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/image(1).png">
<img width="1300" alt="image" src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/image(2).png">
<img width="1300" alt="image" src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/image.png">
<img width="500" alt="image" src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%20(21).png">
# じゃんけんをするための準備

https://github.com/user-attachments/assets/d277dcee-fd45-4726-96e3-6c43e534381c

1. Forge 1.16.5をインストール
　　　https://files.minecraftforge.net/net/minecraftforge/forge/index_1.16.5.html

   ![ダウンロード (3)](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/e2e9de27-5113-4a02-807b-1e4da3dc1f91)

2. RemoteControllerMod-1.16.5 v0.05　をインストール
　　　https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3363255

    ![ダウンロード (4)](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/65c0c363-52e1-41f4-9b71-cf71aded1235)

3. mincraft(forge1.16.5)を起動

![NetherUpdateArtwork](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/28acd239-7094-43ac-8a8f-f79a9329ea85)

4. hands_mincraft.pyを実行

![Python-logo-notext svg (1)](https://github.com/vichyalpha/Maze-Generation_vichy_f/assets/107329825/ae62b1b0-3ac0-458c-b5bc-93e8705a64d5)

===>完了！

# じゃんけんのやり方

　じゃんけんのフィールドはx=0、z＝0に生成されます。
 
 マインクラフトのスーパーフラットでワールドを生成し、hands_mincraft.pyを実行します。（実行には数秒かかることがあります。）
 
 webカメラに手を近づけ、じゃんけんの手（グー、チョキ、パー）にします。
 
 キーボードの”p”を押すと、VOICEBOXのずんだもんが「最初はグー、じゃんけんぽん」といいます。
 
 そして、マインクラフトでじゃんけんができます。
   
# 画像認識の仕組み
　<img width="500" alt="image" src="https://github.com/vichyalpha/Mincraft-Rock-Paper-Scissors-Mediapipe-Hands-demo/blob/main/image/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%20(21).png">
 
mediapipeのhands_demoを用いて、指の特異点20個を検出する。

各点の距離を計算し、手の形を判定する。

# 実演動画

 https://github.com/user-attachments/assets/8a6877cb-d3a4-439c-9835-b46bc3e52b73 

# 応用できる例
　・２人でのじゃんけん
 
 　  mediapipeは2つ以上の手まで認識できるので可能。しかし、誰の手なのかが判別できないため困難。
   
　・手話を表現
 
 　手の特異点の変化で作ることは可能。しかし、大量に特異点の組み合わせを作る必要があり、誤認も多い可能性がある。
  


# 開発環境

python 3.12.0 (poetry)
 https://www.python.org/downloads/release/python-3116/
 
forge 1.16.5
 https://files.minecraftforge.net/net/minecraftforge/forge/index_1.16.5.html

RemoteControllerMod 1.16.5 v0.05
 https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3363255
