# 洞窟物語+ (Nintendo Switch) - スペイン語翻訳パッチ (ファン翻訳)

<p align="left">
  <img src="https://img.shields.io/badge/翻訳ステータス-56%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="翻訳 56%">
  <img src="https://img.shields.io/badge/MOD翻訳-5%25-brightgreen?style=for-the-badge&logo=googletranslate&logoColor=white" alt="Mod 5%">
  
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja">
    <img src="https://img.shields.io/badge/ライセンス-CC%20BY--NC--SA%204.0-lightgrey?style=for-the-badge&logo=creativecommons&logoColor=white" alt="ライセンス CC BY-NC-SA 4.0">
  </a>
</p>

Nintendo Switch版『洞窟物語+』をスペイン語でプレイするための翻訳パッチリポジトリへようこそ！

このプロジェクトは、Switch版独自の追加要素や改善点（迷宮の階段追加やジェンカの仔犬運搬システムなど）を維持しつつ、スペイン語圏のプレイヤーに最高の体験を届けることを目的としています。また、移植版におけるバグの修正も行っています。

---

## 🛠️ プロジェクトの現状
* **メインストーリー:** 開発中（56%）。
* **MOD & 追加コンテンツ:** 未翻訳（協力者募集中！）。
* **互換性:** Nintendo Switch 実機および **doukutsu-rs** で動作確認済み。

## 💻 技術情報
* **ベースエンジン:** Nicalisによる **C++** 実装（Cave Story+ バージョン）。
* **スクリプティング:** 本リポジトリの `.tsc` ファイルは、Switch版のスクリプトインタプリタと完全な互換性があります。
* **デバッグ環境:** **doukutsu-rs**（Rust版エンジン）を使用してネイティブテストを行い、ダイアログの流動性やイベントの安定性を確認しています。
* **ファイル管理:** *Everything* を使用してクリーンアップを行い、翻訳に必要なテキストと画像アセットのみを抽出しています（未変更の .pxm や .pxe は含みません）。

## ⚠️ ローカライズに関する注意点
Switch版のフォントレンダリングの制限により、文字化けやクラッシュを避けるため以下のルールを適用しています：
* **アクセント記号の省略:** スペイン語特有のアクセント記号（á, é, í, ó, ú）は使用していません。
* **「Ñ」文字の置き換え:** 別の表現や「n」に置き換えています。
* **グラフィック:** **YES / NO** などのUI画像（.png）は、個別に手動で編集・ローカライズしています。

---

## 📂 リポジトリの構成
本リポジトリにはファンが作成した編集ファイルのみが含まれており、オリジナルの著作物は配布していません：
* `/data/*.tsc`: 翻訳済みイベントスクリプト。
* `/data/Stage/*.png`: UIおよび画像内テキスト。
* `pxm`、`pxe`、`nso`、`tbl`、`nro` などのゲームバイナリをアップロードすることは**厳禁**です。

---

## ⚖️ ライセンスと免責事項

本プロジェクトは **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** ライセンスの下で配布されています。

**免責事項:** これは非営利のファンプロジェクトです。開発元の Studio Pixel および Nicalis とは一切関係ありません。本リポジトリにはゲーム本体、C++ソースコード、実行ファイルなどは含まれていません。使用には正規のゲームソフトが必要です。

---

## 🤝 クレジット
* **オリジナル開発:** [Studio Pixel](https://www.studiopixel.jp/) (天谷大輔 氏)
* **パブリッシャー/移植:** [Nicalis, Inc.](https://www.nicalis.com/)
* **翻訳・編集:** [EdwarlyGamer999+](https://www.youtube.com/@EdwarlyGamer999plusxd)

## 💬 コラボレーション
MOD（風の砦、ネメシスチャレンジなど）の翻訳や、メインストーリーのブラッシュアップに協力いただける方は、ぜひリポジトリのフォークやプルリクエストをお願いします！
