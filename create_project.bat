@echo off

REM Создание необходимых папок
mkdir ProjectFolder
cd ProjectFolder
mkdir static
mkdir templates

REM Создание main.py
echo. > main.py
echo from flask import Flask, render_template, request >> main.py
echo. >> main.py
echo app = Flask(__name__) >> main.py
echo. >> main.py
echo @app.route('/') >> main.py
echo def index(): >> main.py
echo     return render_template('index.html') >> main.py
echo. >> main.py
echo if __name__ == '__main__': >> main.py
echo     app.run() >> main.py

REM Создание index.html
echo. > templates\index.html
echo ^<!DOCTYPE html^> >> templates\index.html
echo ^<html^> >> templates\index.html
echo ^<head^> >> templates\index.html
echo     ^<title^>Моя текстовая RPG^</title^> >> templates\index.html
echo ^</head^> >> templates\index.html
echo ^<body^> >> templates\index.html
echo     ^<h1^>Добро пожаловать в мою текстовую RPG!^</h1^> >> templates\index.html
echo ^</body^> >> templates\index.html
echo ^</html^> >> templates\index.html

REM Создание style.css
echo. > static\style.css
echo /* Общие стили */ >> static\style.css
echo body { >> static\style.css
echo   font-family: Arial, sans-serif; >> static\style.css
echo   background-color: #f1f1f1; >> static\style.css
echo } >> static\style.css
echo. >> static\style.css
echo h1 { >> static\style.css
echo   font-size: 24px; >> static\style.css
echo   color: #333; >> static\style.css
echo   margin-bottom: 20px; >> static\style.css
echo } >> static\style.css

REM Создание script.js
echo. > static\script.js
echo $(document).ready(function() { >> static\script.js
echo     // Ваш JavaScript код здесь >> static\script.js
echo }); >> static\script.js

echo Готово! Созданы папки и файлы для вашего проекта Flask.
pause
