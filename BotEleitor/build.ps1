$exclude = @("venv", "BotEleitor.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotEleitor.zip" -Force