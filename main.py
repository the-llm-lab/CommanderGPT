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

engine = pyttsx3.init()

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interactive", help="Interactive Mode", default=False)
args = parser.parse_args()
interactive_mode = args.interactive


def voice_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now.")
        audio = r.listen(source)
    return r.recognize_google(audio)


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
        try:
            prompt = voice_recognition()
            print(prompt)
        except sr.UnknownValueError:
            print("Could not understand audio")
            time.sleep(10)
            continue
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            time.sleep(60)
            continue

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

        execute_command(python_code)

    time.sleep(config["Next_CMD_Delay"])
