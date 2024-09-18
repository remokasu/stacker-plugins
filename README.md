## 概要
これは、RPN計算機ソフト [Stacker](https://github.com/remokasu/stacker) のプラグイン集です。

Stacker の最新バージョンには対応していない可能性があります。

マジメに使うためのものではなく、Stacker の拡張機能を試すためのものです。

## 使い方

必要なプラグイン以外は削除してください。

Stackerの plugins ディレクトリ下に、必要なプラグインをコピーしてStackerを再インストールしてください。

再インストールせずに使用する場合は、pluginsディレクトリと同じ階層に cd してから stacker を実行してください。


## 内容

- matrix.py: numpy による行列計算プラグイン。Stackerの既存の演算を numpy で行列計算に対応させます。

- np_math.py: numpy による数学関数プラグイン。Stackerの既存の演算を numpy で数学関数に対応させます。

- whos.py: numpy による変数表示プラグイン。

- unit_conveter.py: 単位変換プラグイン。

- sh.py: シェルコマンド実行プラグイン。Stacker の REPL でシェルコマンドを実行します。linux 環境でのみ使用可能です。