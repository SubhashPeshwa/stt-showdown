# Ultimate Showdown of all Cloud STT APIs

## Cloud STT comparisons for audio transcription (specifically streaming transcription over ulaw/alaw/slin16)

Speech APIs in consideration:-

1. Google Cloud Speech to Text (Only ever used this before starting the project)
2. Google Dialogflow (Uses the same underlying secret sauce as Cloud Speech)
3. Twilio Autopilot (Fingers crossed)
4. Azure STT (No great expectations here)
5. AWS Transribe (I know this will be bad)
6. rev.ai (Curious)
7. assemblyai (Very Curious)
8. IBM Watson (As old as Ollivander)

Created on : 14th Jan, 2022 (1 month to Valentine's day, anxiety onset to begin soon)
ToDo: Get tests to run every fornight and update readme with latest and to add old reports to changelog


## What I learnt from this:-

1. Using noxfiles for python version compatibility tests
2. Circle CI - Because only AzDo and bitbucket in enterprises
3. Ensuring coverage.py isn't ignored after day-2
4. Sphinx autodoc generation - maybe someday, someone will read it

## Reinforced my prior learnings:-

1. Better folder/file/funtion naming conventions - File/Class -> Entities/Nouns, Methods - Action on entities/Verbs, Variables -> Attributes of entity/Nouns [Not sure, I just made this up, gotta ask the gurus]
2. Better use of classes as opposed to just using badly named functions
3. Of **args and **kwargs and yield operators
