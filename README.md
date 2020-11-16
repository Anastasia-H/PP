Лабораторна робота №4

Дана лабораторна робота була створена у середовищі PyCharm.
Використовуючи інструмент pyenv версії 2.64.3 був інстальований інтерпретатор Python 3.7.0. У випадку, якщо pyenv та Python у вас не інстальовані, необхідно:
- відкрити командний рядок Windows (наприклад ви можете нажати комбінацію клавіш Windows+R, вести рядок 'cmd' і нажати Enter) і ввести команду
  pip install pyenv-win --target "%USERPROFILE%\.pyenv"
- відкрити PowerShell і ввести наступні команди
  [System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
  [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
- відкрити командний рядок Windows i ввести команду: pyenv install 3.7.0

Також за допомогою наступних команд:
- pip install flask
- pip install gevent
Були інстальовані фреймворк Flask, та WSGI-серевер Gevent. 

Окрім того (за допомогою команд 'virtualenv --python шлях_до_системного_інтерпретатора venv' та 'шлях_до_пточного_проекту/venv/Scripts/activate.bat') було створене віртуальне середовище для проекту.


Для того щоб клонувати даний репозиторій і запустити його в себе на комп’ютері, вам необхідно мати встановлений Git.
Якщо його у вас немає, то це можна зробити, перейшовши на наступні лінки:
- (для Windows) http://git-scm.com/download/win

Якщо ви хочете запустити проект у Visual Studio, то вам це потрібно зробити, склонувавши репозиторій (https://github.com/Anastasia-H/PP.git) у середовище. 

Для того, щоб коректно запустити наступний проект у PyCharm, вам необхідно:
1. Створити папку
2. Нажати на раніше створену папку правою кнопкою миші та вибрати опцію Git Bash here
3. У вікно, яке запуститься після попередніх дій, вписати наступну команду: 'git clone https://github.com/Anastasia-H/PP.git'
4. Відкрити папку і запустити проект за допомогою PyCharm

Після цього ви можете запускати проект.
Після запуску перейшовши за адресою http://localhost:5000/api/v1/hello-world-5, ви побачите текст 'Hello World 5'.

Якщо ви хочете перевірити версію пітона, або ж хочете переглянути який інтерпретатор використовує даний проект, вам необхідно:
1. Відкрити командний рядок Windows (наприклад ви можете нажати комбінацію клавіш Windows+R, вести рядок 'cmd' і нажати Enter)
2. Далі потрібно активувати віртуальне середовище ввівши наступну команду в командний рядок: 'шлях_до_папки_з_проектом\-\venv\Scripts\activate.bat'
3. Якщо все працює коректно, наступний рядок почнеться з '(venv)', тоді, щоб дізнатися версію пітону необхідно ввести команду 'python --version'
4. Щоб дізнатися місцезнаходження інтерпретатора потрібно ввести команду 'where python'

