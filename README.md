This is a virtual assistant which can perform function like telling time, searching anything from wikipedia(100 words), opening google or sending email to an person
STEPS TO FOLLOW IN COMMAND PROMPT
S1: cd Desktop                                       #to get into desktop
S2: mkdir projects                                   #to create a directory called projects in desktop
S3: cd projects                                      #getinto projects
S4: mkdir virass                                     #to create a folder called virass (virtualassistant) 
S5: pip install virtualenv                           #install virtual environment
S6: virtualenv mohith                                #creates a virtual environment named mohith
S7: .\mohith\Scripts\activate                        #activates the virtual environment
S8: cd virass                                        #enters into virass folder
S9: pip list                                         #lists all packages
S10: pip install gTTS                                #to install google text to speech
S11: pip install SpeechRecognition                   #to install SpeechRecognition
S12: pip install PyAudio                             #to install pyaudio
S13: pip install playsound==1.2.2                    #installs playsound
S14: pip install BeautifulSoup4                      #installs beautifulsoup which is used to scrap info from webpages
S15: pip freeze                                      #lists versions of all packages
S16: pip freeze > requirements.txt                   #to dump all packages into that file
S17: (mohith) C:\Users\Name\Desktop\projects\virass>notepad va.py        #creates a file named va with py extension if not present allready
S18: we write code into the va.py file using IDLE
S19: (mohith) C:\Users\Name\Desktop\projects\virass>python va.py         #to execute the file
