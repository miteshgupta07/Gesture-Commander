<h1 align="center">
  <img width="30" alt="vlc" src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/6cc78c35-1cb8-48df-b988-ddf95942c88b"> <img width="40" alt="youtube" src="https://github.com/miteshgupta07/VLC-Gesture-Commander/assets/111682782/39ae47da-b803-4a0d-b455-a38014204188"> Gesture Commander <img width="40" alt="youtube" src="https://github.com/miteshgupta07/VLC-Gesture-Commander/assets/111682782/39ae47da-b803-4a0d-b455-a38014204188"> <img width="30" alt="vlc" src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/6cc78c35-1cb8-48df-b988-ddf95942c88b">
 
</h1>

Gesture Commander uses computer vision techniques to interpret hand gestures and control Media Player like VLC and Youtube. Utilizing OpenCV for image processing and cvzone for hand detection, it provides an intuitive, hands-free way to interact with your media player.


## Features

- **Real-time Gesture Detection**: The system detects hand gestures in real-time using your webcam.
- **Seamless Media Player Integration**: Sends corresponding key presses to Media Player like VLC and Youtube based on detected gestures.
- **User-Friendly**: Easy-to-use interface with simple hand gestures for common media controls.

  
## Project Files

- `requirements.txt` - Lists the dependencies required to run the project.
- `main.py` - Contains the code to detect hand gestures.
- `Key_Control.py` - Includes functions to send key presses to Media Player.

## Gestures

- **Pause/Resume**: Use your left hand with all fingers and thumb touching together.<img src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/b40aecaf-6fe8-44ce-9806-6fe871e590cb" alt="Pause_Resume" width="65" height="65">
  

- **Forward/Backward Jump**: Use your right hand with the index finger and thumb touching each other.<img src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/76686e25-c501-454a-a0e5-9072f83ee7e3" alt="Forward/Backward" width="65" height="65">
  
- **Volume Up/Down**: Use your right hand with the index and middle finger moving in upward or downward directions. <img src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/f7371a73-88f2-435e-8cd3-de234dbedf61" alt="Pause_Resume" width="65" height="65">

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Gesture Commander.git
    cd Gesture Commander
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Make sure VLC Media Player is installed on your system and running.

2. Run the main script:
    ```sh
    python main.py
    ```

3. Use the specified hand gestures to control VLC Media Player and Youtube.


## Acknowledgements

- **OpenCV**: Powering Gesture Commander with robust image processing capabilities.
- **cvzone**: Providing efficient hand detection and tracking functionality for Gesture Commander.
- **Media Player**: Serving as the media platform for Gesture Commander's seamless integration.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes or improvements.
