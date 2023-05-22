import subprocess
import time
import argparse
import yaml
import speech_recognition as sr
import pyttsx3
import openai

config = yaml.safe_load(open("config.yml"))

openai.api_key = config["API_Key"]

# Hotword to activate the speech recognition
HOTWORD = config["HOTWORD"]

preprompt_text = (
    f"I want you to act like a Desktop Automation. I will give you Instruction and you will return Python code. "
    f"Do not provide any explanations. Do not respond with anything except the code. "
    f"Do not include any typographical mark in respond. You can use PyAutoGUI for controlling mouse and keyboard. "
    f"My OS is {config['OS']} and My desktop environment is {config['Desktop_ENV']}. Always put delay between instructions. "
)

threat_preprompt_text = (
    f"I want you to act like a Threat Intelligence. "
    f"I will give you python script and you score the risk of the script execution from 0 to 10. "
    f"Do not provide any explanation outside of the question, do not give an introduction or conclusion, just give me the plain numerical score with no explanations. "
)

engine = pyttsx3.init()

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interactive", help="Interactive Mode", default=False)
args = parser.parse_args()
interactive_mode = args.interactive


def voice_recognition():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Speak Now.")
            try:
                audio = r.listen(source)
                return r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            time.sleep(10)

def threat_intelligence(python_code):
        threat_result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": threat_preprompt_text + python_code}]
        )
        threat_score = int(threat_result.choices[0].message.content)
        if threat_score > config["Threat_Barrier"]:
                engine.say("This is an Avengers Level Threat. Do you want to proceed?")
                engine.runAndWait()
                
                if interactive_mode:
                    if input("This is an Avengers Level Threat. Do you want to proceed? Type Yes/No:").lower() == "yes":
                        return True
                    else: 
                        return False
                else:
                    if voice_recognition().lower() == "yes":
                        return True
                    else:
                        return False
        elif threat_score < config["Threat_Barrier"]:
            return True
        # Threat Level is Ambiguous
        else:
            return False


def execute_command(python_code):
    try:
        engine.say("Executing Command")
        engine.runAndWait()

        with open('last_command.py', 'w') as f:
            f.write(python_code)
        subprocess.call(["python", "last_command.py"])

        engine.say("Execution Done")
        engine.runAndWait()
    except Exception as e:
        print("An error occurred:", e)


prompts = ["", ""]
while True:
    if interactive_mode:
        prompt = input("Type your command here, or quit:")
    else:
        prompt = voice_recognition()

        print(prompt)
        prompts.append(prompt)

        if HOTWORD in prompts[-1].lower():
            print("Commander mode activated. Listening for command...")
            engine.say("Listening for command")
            engine.runAndWait()
            continue

    if prompt.lower() in ['quit', 'exit']:
        engine.say("Shutting Down")
        engine.runAndWait()
        break

    if interactive_mode or HOTWORD in prompts[-2].lower():
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": preprompt_text + prompt}]
        )

        python_code = completion.choices[0].message.content.replace('super', 'win')

        if threat_intelligence(python_code):
            execute_command(python_code)
        else:
            engine.say("Execution Canceled")
            engine.runAndWait()


    time.sleep(config["Next_CMD_Delay"])
