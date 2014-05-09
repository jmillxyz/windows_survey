REM py2exe + run batch script
REM
REM Usage: must be executed from same directory as win_survey_script.py and win_survey_setup.py
REM
REM Description:    1) builds python script according to setup.py into script.exe
REM                 2) cd to dist directory
REM                 3) run script.exe (which outputs win_survey_result.txt
REM                 4) open win_survey_result.txt in notepad++
REM                 5) cd back to parent directory so it can be run again

python win_survey_setup.py py2exe
cd dist
win_survey_script.exe
cd ..
