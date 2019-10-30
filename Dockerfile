FROM python:3

RUN git clone https://github.com/NicoBeast98/SUDOKU.git

WORKDIR /SUDOKU

RUN pip install -r requerimientos.txt

RUN python3 test_sudoku.py

CMD ["python3", "./interfaz.py"]
