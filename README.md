# README

## 概要

LightSwitcherは、RaspberryPiに接続されたDCサーボモーターを制御するAPIサーバーです。

DCサーボモーターを照明のスイッチに固定することで、物理的にスイッチをオンオフすることができます。

これにより、照明をIot化することができます。

## 環境

* 言語 : Python 3.8

* WEBフレームワーク : Flask 1.1.2, Flask-RESTX 0.2.0

* OS : Raspbian Buster

## 使用方法

照明をオンにする場合、サーバーのURL(IPアドレス)のルートパスにJSONデータ{"param": "ON"}をPOSTリクエストで送信します。

照明をオフにする場合、サーバーのURL(IPアドレス)のルートパスにJSONデータ{"param": "OFF"}をPOSTリクエストで送信します。


## 実行方法

### 事前準備

下記のコマンドを実行し、5 Interfacing Options -> P8 Remote GPIOからRemote GPIOをenabledにしてください。 

`sudo raspi-config`

以降の事前準備の作業は、setup.shを実行することで省略できます。

Dockerのインストール

`curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh`

pigpioのインストール

`sudo apt install -y pigpio && pip3 install pigpio`

pigpioデーモンの起動(起動していない場合 or デーモンの起動を自動化していない場合)

`sudo gpiod`

pigpioデーモンの起動の自動化

`sudo systemctl enable pigpiod.service && sudo reboot`

### ビルド

`docker build -t light_switcher .`

### 起動

`docker run -d -p 80:80 --net host light_switcher`

## ライセンス

MIT

