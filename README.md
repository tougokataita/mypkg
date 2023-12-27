# talker ・　listenerコマンド
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
* 実行方法1
  実行方法1では端末を2つ使用します。
* 端末1
  ros2_ws ディレクトリに移動し、下記のコマンドでビルド、実行することができます。
```
colcon build
ros2 run mypkg talker
```
* 端末2 
  下記のコマンドで実行することが出来ます。
```
ros2 run mypkg listener
```
* 実行例
* 端末1
```
colcon build

Starting >>> mypkg
Starting >>> person_msgs
Finished <<< person_msgs [1.25s]
Finished <<< mypkg [1.47s]

Summary: 2 packages finished [2.96s]
```

```
ros2 run mypkg talker

```
* 端末1には何も表示されません
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

* 実行方法2


## テスト環境
* Ubuntu20.04
* Python
* テスト済みバージョン: 3.7 ~ 3.10
## 著作権
* このソフトウェアパッケージは，3条項BSDライセンスの下，再配布および使用が許可されます。
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
* [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson4.md)
* © 2023 Tougo Kataita
