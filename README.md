# CommanderGPT

<p align="center">
  <img src="media/logo.jpeg" alt="CommanderGPT" width="400" height="400">
</p>

Welcome to the CommanderGPT repository! This project harnesses the power of OpenAI's GPT-3.5 language model to enable seamless automation of your desktop tasks using voice commands. With a simple voice instruction, you can effortlessly control your desktop environment and accomplish a wide range of automation tasks.

## Key Features

- **Easy Voice Control**: Command your desktop by speaking naturally. Use the provided hotword "commander" to activate the script, and effortlessly issue voice commands for various actions.

- **Bash Script Generation**: The script leverages OpenAI's GPT-3.5 model to generate precise Bash scripts based on your voice commands. These scripts act as the bridge between your voice instructions and desktop automation.

- **Versatile Automation**: Open applications, navigate through menus, simulate keyboard and mouse inputs, perform web searches, write code, save documents, and execute them — all through intuitive voice commands.

- **Interactive and Voice Modes**: Switch between interactive mode, where you can enter commands directly, and voice mode, which allows for a more natural and hands-free interaction.

- **Enhanced Desktop Integration**: The script intelligently switches between windows and ensures the appropriate actions are performed in the correct desktop environment.

- **Cross Platform**: Works on Linux & Mac & Windows.

## Prerequisites

To utilize this CommanderGPT, ensure the following dependencies are installed (You can install them using your Distro Package Manager):

- Python 3.x
- `python3-devel`
- `python-pyaudio`
- `espeak`

You will also need an OpenAI API key.

## Getting Started

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. Rename `config.yml.example` to `config.yml` and Update the file with your OpenAI API key. You can customize other parameters if needed.

4. Execute the script using the following command:

   ```
   python main.py
   ```

5. The script will actively listen for voice commands. Alternatively, you can switch to interactive mode by pressing the executing script with ```--interactive True``` arg and typing commands manually.

6. Use the hotword "commander" to activate the script and provide voice commands. For example, say "commander, open the web browser" to launch the web browser.

7. The script utilizes OpenAI's GPT-3.5 model to generate Bash scripts based on your voice commands. These scripts will be executed, automating the desired tasks on your desktop environment.

8. To exit the script, either type "quit" or "exit," or say the hotword followed by "quit" or "exit" (e.g., "commander, exit").

## Example Usage

Here are a few examples of voice commands you can use:

- **Example 1**: Open Firefox, open a new tab, and search for a Python tutorial.

- **Example 2**: Launch the Cheese App and take a picture.

- **Example 3**: Open LibreOffice Writer, compose a Shakespearean poem, and save the document.

Feel free to experiment with different commands and explore the limitless possibilities of CommanderGPT!

## Video Example

https://github.com/theonlyfoxy/CommanderGPT/assets/12250394/8bed8d6f-46bb-4444-87a9-f015bcb9fbb4


*Click the above to watch a video example showcasing the CommanderGPT in action.*

## Todo

- Feedback from Desktop: Improve the script to capture and process feedback from the desktop environment, enhancing the accuracy and reliability of voice commands and automation tasks. (PyAutoGUI LocateonScreen, Teseract OCR & Current Mouse Position Relative to Button, Change X/Y Cordinates Based on Screenshot)

- Additional Features: Explore and implement additional features to expand the capabilities of the CommanderGPT system.

## Limitations and Improvements

- The provided code is a simplified version and may require further implementation to handle exceptions, provide robust error handling, and ensure secure and reliable execution.

- Please note that the script assumes a GNOME desktop environment on Fedora. Modifying the generated Bash scripts may be necessary to support different desktop environments or operating systems.

## License

This code is licensed under the [MIT License](LICENSE).
