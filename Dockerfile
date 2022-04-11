FROM python:3.8
COPY src/word-sequence.py /tmp/
CMD ["python", "/tmp/three-word-sequence.py", "src/test/resources/mobydick.txt"]
