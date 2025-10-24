# NLP100本ノック2025

## 環境構築
- windows11前提

1. uvのインストール
    ```powershell
    $env:Path = "C:\Users\khira\.local\bin;$env:Path"   (powershell)
    ```
    - PATHを通すよう指示が出るので従う。
2. 再起動（PATH設定の反映）
3. インストールを確認
    ```powershell
    uv
    ```
4. 仮想環境の作成
    ```powershell
    uv venv --python 3.11 
    ```
5. 仮想環境の有効化
    ```powershell
    .venv\Scripts\activate
    ```
6. 依存関係の同期
    ```powershell
    uv sync
    ```