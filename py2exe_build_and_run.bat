REM py2exe + run batch script
REM
REM Usage: must be executed from same directory as win_survey_script.py and win_survey_setup.py
REM
REM Description: builds python script according to setup.py into script.exe, cd's to dist directory, 
REM              runs, then cd's back to parent directory so it can be run again.

python win_survey_setup.py py2exe
cd dist
win_survey_script.exe
cd ..
