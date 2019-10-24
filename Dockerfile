FROM python:3

RUN git clone https://github.com/NicoBeast98/SUDOKU.git
WORKDIR /docker

RUN pip install -r requirements.txt

CMD ["python", "./interfaz.py"]