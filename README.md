# talker ・　listenerコマンド
## 機能説明
* パブリッシャを持つtalkerノードが/countupというトピックを介してリスナーを持つlistenerノードへメッセージを受け渡しています。
* メッセージは、listenerノードへ受け渡すたびに1ずつ足されていくInt16型の整数を0.5秒間隔で受け渡しています。
* トピック : 異なるノード同士がメッセージを送受信するための通信方法です。1対1だけではなく1対多での送受信が可能であり、リスナーは、パブリッシャが指定したトピック名と同じトピック名を指定することで特定のメッセージを受信することが出来ます。


## インストール
* インストールをする前に下記のコマンドでホームディレクトリにワークスペースを作成してください
```
mkdir -p ros2_ws/src
```
* ワークスペースを作成した後、src ディレクトリに移動し、以下のコマンドを使用して mypkg リポジトリをローカルのディレクトリにクローンします。
```
git clone git@github.com:tougokataita/mypkg.git
```

## 実行方法
### 実行方法1  : 端末を2つ使用します。
	* 端末1 : ros2_ws ディレクトリに移動後、下記のコマンドでビルド、実行することが出来ます。
```
colcon build
ros2 run mypkg talker
```
* 端末2 : 下記のコマンドで実行することが出来ます。
```
ros2 run mypkg listener
```
* **実行例** 
* 端末1  (実行後、端末1には何も表示されません)
```
ros2 run mypkg talker

```
* 端末2
```
ros2 run mypkg listener
[INFO] [1703692973.128299537] [listener]: Listen: 20
[INFO] [1703692973.620228071] [listener]: Listen: 21
[INFO] [1703692974.120428514] [listener]: Listen: 22
[INFO] [1703692974.620360669] [listener]: Listen: 23
[INFO] [1703692975.119980587] [listener]: Listen: 24
[INFO] [1703692975.620456621] [listener]: Listen: 25
[INFO] [1703692976.120546765] [listener]: Listen: 26
[INFO] [1703692976.619804995] [listener]: Listen: 27
[INFO] [1703692977.120254738] [listener]: Listen: 28
```

### 実行方法2
* ros2_wsディレクトリに移動後、下記のコマンドでビルド、実行することが出来ます。
```
colcon build
ros2 launch mypkg talk_listen.launch.py
```
* **実行例**
```
ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/abcd/.ros/log/2023-12-28-01-17-51-025393-taruto105-32471
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [32473]
[INFO] [listener-2]: process started with pid [32475]
[listener-2] [INFO] [1703693872.213204045] [listener]: Listen: 0
[listener-2] [INFO] [1703693872.700736138] [listener]: Listen: 1
[listener-2] [INFO] [1703693873.200199349] [listener]: Listen: 2
[listener-2] [INFO] [1703693873.700284806] [listener]: Listen: 3
[listener-2] [INFO] [1703693874.200831414] [listener]: Listen: 4
[listener-2] [INFO] [1703693874.700822301] [listener]: Listen: 5
[listener-2] [INFO] [1703693875.200776849] [listener]: Listen: 6
[listener-2] [INFO] [1703693875.699988081] [listener]: Listen: 7
[listener-2] [INFO] [1703693876.200870426] [listener]: Listen: 8
[listener-2] [INFO] [1703693876.700249228] [listener]: Listen: 9
[listener-2] [INFO] [1703693877.201117346] [listener]: Listen: 10
```

## テスト環境
* Ubuntu22.04
* Python
* ROS2 Humble
## 著作権
* このソフトウェアパッケージは，3条項BSDライセンスの下，再配布および使用が許可されます。
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Tougo Kataita
