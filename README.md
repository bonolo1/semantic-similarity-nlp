# Semantic Similarity

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)

## Project Description <a name="project_description"><a>
The purpose of this is to review the output of semantic similarity in Natural Language Processing (NLP) to analyse and see how it works.

## Installation <a name="installation"><a> 

There are two different ways to run the program: using Docker or a virtual environment.

### Docker

You can either use docker on your desktop or by using Docker Playground. Descriptions for using both options are included.

**Run container using Desktop**

1. If don't already have Docker installed on your desktop, install Docker on your desktop.

2. Once installed, enter the following command in the terminal:

```
docker run bonolor/semantic-similarity-nlp
```

**Run container using Docker Playground**

1. Go to Docker Playground at the following link and enter "Start": https://labs.play-with-docker.com/.

2. Add a new instance.
  
3. Enter the following command in the terminal:

```
docker run -i bonolor/semantic-similarity-nlp
```

### Virtual Environment

1. Download the followiing files in the repository: semantic.py and requirements.txt.

2. Create a project folder named "semantic_similarity".
 
3. Move and save the downloaded files to the semantic_similarity folder.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the semantic_similarity folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal (use relevant python version):
   
  ```
  python3.11 -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the garden_ai directory (if you are not already in the directory):
  
  ```
  cd semantic_similarity
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. If prompted to upgrade pip, enter:

  ```
  pip install --upgrade pip
  ```

11. Install language maodel:

  ```
  python -m spacy download en_core_web_md

  ```
  
  _Note: Check to ensure that the virtual environment has been activated_

12. Select semantic.py and run the program.

## Usage <a name="usage"><a>

Shows the output of similarity scores to demontrate how semantic similary works.
