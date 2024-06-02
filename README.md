<h1 align="center">🎥 VLC Gesture Commander 🎥</h1>

VLC Gesture Commander uses computer vision techniques to interpret hand gestures and control VLC Media Player. Utilizing OpenCV for image processing and cvzone for hand detection, it provides an intuitive, hands-free way to interact with your media player.


## Features

- **Real-time Gesture Detection**: The system detects hand gestures in real-time using your webcam.
- **Seamless VLC Integration**: Sends corresponding key presses to VLC Media Player based on detected gestures.
- **User-Friendly**: Easy-to-use interface with simple hand gestures for common media controls.

  
## Project Files

- `requirements.txt` - Lists the dependencies required to run the project.
- `main.py` - Contains the code to detect hand gestures.
- `VLC_Control.py` - Includes functions to send key presses to VLC Media Player.

## Gestures


<img src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/03a090ee-5595-466f-9130-eb7c2bbf8110" alt="Volume Up/Down" width="50" height="50">
<img src="https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/e0d228af-fde7-4fbd-b7b0-bf017cd8b74f" alt="Forward/Backward" width="50" height="50">
![Forward_Backward](https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/76686e25-c501-454a-a0e5-9072f83ee7e3)
![Pause_Resume](https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/b40aecaf-6fe8-44ce-9806-6fe871e590cb)
![Volume](https://github.com/miteshgupta07/Gesture-Control-Media-Player-Using-Computer-Vision/assets/111682782/f7371a73-88f2-435e-8cd3-de234dbedf61)


- **Pause/Resume**: Use your left hand with all fingers and thumb touching together.

- **Forward/Backward Jump**: Use your right hand with the index finger and thumb touching each other.
- **Volume Up/Down**: Use your right hand with the index and middle finger moving in upward or downward directions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/VLC Gesture Commander.git
    cd VLC Gesture Commander
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

3. Use the specified hand gestures to control VLC Media Player.


## Acknowledgements

- **OpenCV**: Powering VLC Gesture Commander with robust image processing capabilities.
- **cvzone**: Providing efficient hand detection and tracking functionality for VLC Gesture Commander.
- **VLC Media Player**: Serving as the media platform for VLC Gesture Commander's seamless integration.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes or improvements.
