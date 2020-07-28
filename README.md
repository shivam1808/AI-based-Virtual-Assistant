# AI-based-Virtual-Assistant
In today’s world of automation, everyone wants to have an automated tool which make their day to day life very easy. Day to day work involve opening any application present in system, play and control music, solve mathematical expressions, search on web, sending mail, setting reminders, getting daily news updates, weather details, etc. Everyone gets bored and tired doing same thing manually. People need automation in their life.

We build an __Automated AI based Virtual Assistant__ to perform all the above-mentioned jobs and many more. It will reduce workload and will do ones work in just single voice command. No virtual assistant is available for both Linux and Windows. This virtual assistant has facility to listen to your commands and speak the response of your statement. You can turn off/on these facilities on your choice. These instructions are stored in a sqlite database so that any action performed can be store in database for further use. Conversation is not hardcoded as other chatbots might have. In this we train our model on manually build dataset for conversation.
<br>This virtual assistant has features like:<br>
->	Sending text message to a contact number,<br>
->	Control Music,<br>
->	Search Google or YouTube,<br>
->	Play Games,<br>
->	Send Email to Contacts,<br>
->	Set Alarm or Reminders,<br>
->	Wallpaper change facility, <br>
->	Usual conversation, etc<br>

## Technologies Used: 
__TFLearn:__ Deep learning library featuring a higher-level API for TensorFlow. We used TFLearn library to build and train our model for conversation just like chatbots. 
These chatbots derive from a form of artificial intelligence called __Natural Language Processing (NLP)__. One particularly important aspect of NLP that is used for programming a chatbot are the concepts of stemming and tokenization. Lancaster stemming library from NLTK package is used to collapse distinct word forms.
We connect our virtual assistant to __sqlite database__ so that execution of commands or instruction can be done very easily.
We used different __python libraries__ such as speech_recognition, Wikipedia, wolframalpha, file_search, etc. for the purpose to attain automation.

## Requirements:

-> Ananconda Navigator
-> Make sure you install these packages before moving forward to other python libraries-

`sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools`

You can run `pip install -r requirements.txt` to install them all.

## Installation:

`conda create -n env_name python==3.6` : Create a python3.6 environment for better compatibilty with other libraries.

You can run `pip install -r requirements.txt` to install them all.

Run `python start.py` : to start the virtual assistant


## Conclusion: 
We have built an Artificial Intelligence based Virtual Assistant for both Linux and Windows with the integration of sqlite database, NLP and TFLearn.

## Future Scope: 
Graphical User Interface (GUI) and few more features will be added in the upcoming version of this Virtual Assistant.
