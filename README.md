# AIConverse
<h3>AIConverse: Your Intelligent Conversation Companion, seamlessly blending advanced AI to understand and respond to your every query with personalized, insightful answers. <br/>
  "Revolutionizing communication, AIConverse offers a dynamic, interactive experience, adapting and learning from each interaction to make conversations more engaging and informative."</h3>
<br>

![Screenshot (267)](https://github.com/crazytrain328/AIConverse/assets/113792434/e59aa488-1c61-49d9-bf32-46be7d58b1b9)

<h2>To Run this Project </h2> 


1) Download This Repository.
   ```bash
   git clone https://github.com/crazytrain328/AIConverse.git
   ```
2) Install Virtual Environment for Python
   ```bash
   pip install virtualenv
   ```
3) Create New Virtual Environment.
   ```bash
   virtualenv env
   ```
4) Make sure you have Python and pip installed</br>
   To Install Python:
   ```bash
   https://realpython.com/installing-python/
   ```
   To install pip:
   ```bash
   python get-pip.py
   ```
5) Install Django
   ```bash
   pip install django
   ```
4) Create A New Django Project.
   ```bash
   django-admin startproject AIConverse.
   ```
5) Create a New App chatbot.
   ```bash
   django-admin startapp chatbot
   ```
5) Delete all the created files inside main AIConverse folder and copy and paste the Files in This repository.
6) Copy the env folder inside main AIConverse folder.
7) Change the working directory to AIConverse
   ```bash
      cd AIConverse
   ```  
8) Activate the Virtual Environment.<br>
   i) Windows
      ```bash
         env\scripts\activate.ps1
      ```
   ii) Linux
      ```bash
         source env\bin\activate.ps1
9) Download all the requirements
    ```bash
      pip install -r requirements.txt
10) Put the OpenAI API key:
    Go to chatbot/views.py
    And paste your API key in the openai_api_key variable.  
11) Start the Server.
   ```bash
      python manage.py runserver
   ```
12) Go to the below URL to run the project.
    ```bash
    http://127.0.0.1:8000/
    ```  
