@echo off
set PY_FILE="C:\Users\sCs\PycharmProjects\nopcommerceApp"
python %PY_FILE%
pause

set PYTEST_ARGS=-v -s -m "sanity" --html=./Reports/report_edge.html testCases/ --browser edge
pytest %PYTEST_ARGS%


