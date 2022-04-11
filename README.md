## Objective

create a program executable from the command line that when given text(s) will return 100 of most common three word sequences in descending order of frequency.

## Prerequisites

$ py --version <br />
Python 3.8.6

## Clone Project

git clone https://github.com/bsachin12/three-word-sequences.git

## Running the application

py src/word-sequence.py src/test/resources/mobydick.txt <br />


## Docker

#Build the Docker Image <br />

docker build three-word-sequences . <br />

#Run Docker image <br />

docker run -it --rm --name running-sequences three-word-sequences
