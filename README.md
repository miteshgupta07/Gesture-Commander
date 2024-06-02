<h1 align="center">🎥 GestureVLC 🎥</h1>

GestureVLC uses computer vision techniques to interpret hand gestures and control VLC Media Player. Utilizing OpenCV for image processing and cvzone for hand detection, it provides an intuitive, hands-free way to interact with your media player.


## Features

- **Real-time Gesture Detection**: The system detects hand gestures in real-time using your webcam.
- **Seamless VLC Integration**: Sends corresponding key presses to VLC Media Player based on detected gestures.
- **User-Friendly**: Easy-to-use interface with simple hand gestures for common media controls.

  
## Project Files

- `requirements.txt` - Lists the dependencies required to run the project.
- `main.py` - Contains the code to detect hand gestures.
- `VLC_Control.py` - Includes functions to send key presses to VLC Media Player.

## Gestures

- **Pause/Resume**: Use your left hand with all fingers and thumb touching together.
- **Forward/Backward Jump**: Use your right hand with the index finger and thumb touching each other.
- **Volume Up/Down**: Use your right hand with the index and middle finger moving in upward or downward directions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/GestureVLC.git
    cd GestureVLC
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

- **OpenCV**: Powering GestureVLC with robust image processing capabilities.
- **cvzone**: Providing efficient hand detection and tracking functionality for GestureVLC.
- **VLC Media Player**: Serving as the media platform for GestureVLC's seamless integration.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes or improvements.
