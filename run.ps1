# チャプター番号と解答番号を受け取る
Param(
    [String]$ChapterNumber, 
    [String]$AnswerNumber
    )

# 引数の確認
# Write-Host "Chapter Number: $ChapterNumber"
# Write-Host "Answer Number: $AnswerNumber"

# uv runで実行
uv run -m "chapter$ChapterNumber.ans$AnswerNumber"