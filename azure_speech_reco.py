# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
import time
import wave
import string
import warnings
  
  
# displaying the warning message 
warnings.warn('Warning! Breath levels are under the optimal standard! Please contact your doctor!')
print('Breath measuring conclusion.')
#PSEUDOCODE AND RATIONALIZATION:
#add the timer function to the code, explain to the customer the logic behind it:
#If the time of silence is too long, we will print out a warning and notify the Client
#
from timeit import default_timer as timer

start = timer()
# ...
end = timer()
print(end - start) # Time in seconds

#Modules needed to determine the time lenght
# <code>f
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "99f5a3ce35b44828adb752fd6b43bf7a", "North Europe"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
result = speech_recognizer.recognize_once()

# Checks result.

#Solution:
#the standard recording time for the Speech recognition is 15 seconds, I would suggest modifying the time to 
#a lower value so that the Customer receives the warning message if we have, let's say 3 seconds of pause
#between words, then the application would stop running and we could  print out a new warning message
#Doing so, would imply that I get the code from a different git repo available online for the Azure Speech Recognition
#this is the quickest and most effective solution in my opinion.
#It would be the standard code, but with a personalized time limit for voice recognition.

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
# </code>
