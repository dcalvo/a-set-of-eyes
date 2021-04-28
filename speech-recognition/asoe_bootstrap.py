import os.path
import subprocess
import multiprocessing
import time
import speechConverter as speech_py

# This script runs NVDA and the speech recognition script in parallel.

NVDA_EXE_PATH = "/Program Files (x86)/NVDA/nvda.exe"

# Run NVDA Executable
def runNVDA():
    subprocess.call([NVDA_EXE_PATH], shell=True)

# Run Speech Recognition script
def runSpeechRecognition():
    speech_py.main()

def main():
    print("Locating NVDA Executable...")
    # TODO: Add logic to install NVDA execulable
    if os.path.isfile(NVDA_EXE_PATH):
        print("Found!")
        print("Running NVDA Executable...")
        nvda = multiprocessing.Process(target=runNVDA)
        nvda.start()
        # Wait while NVDA is starting
        # TODO: Start speech recognition when NVDA finishes loading
        time.sleep(17)
        print("Running speech recognition in parallel...")
        speech_recognition = multiprocessing.Process(target=runSpeechRecognition)
        speech_recognition.start()
        while True:
            # TODO: Find a way to interrupt execution asynchrously
            should_quit = input("Press q to quit")
            if should_quit.lower() == "q":
                speech_recognition.join()
                nvda.join()
                print("Closing program")
                return
    else: 
        print("Unable to find NVDA executable... Closing program")





if __name__ == "__main__":
	main()
