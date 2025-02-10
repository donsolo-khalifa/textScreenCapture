# Screen Capture OCR

This script was made to copy text from videos I watch.

The script  allows you to capture screen regions and extract text using OCR (Optical Character Recognition). Simply press the Print Screen key, select an area on your screen, and the extracted text will be automatically copied to your clipboard.

## Features

- Screen region selection with visual feedback
- Automatic text extraction using EasyOCR
- Clipboard integration for instant access to extracted text
- Simple keyboard shortcut (Print Screen) to activate
- Support for English text recognition
- Visual feedback during area selection
- Error handling and user notifications

## Prerequisites

- Python 3.6 or higher
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/donsolo-khalifa/textScreenCapture.git
cd textScreenCapture
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Press the Print Screen key to activate the selection mode
3. Click and drag to select the area containing text you want to extract
4. Release the mouse button to process the selected area
5. The extracted text will be automatically copied to your clipboard
6. Press Escape at any time to cancel the selection

## Controls

- **Print Screen**: Activate selection mode
- **Click and Drag**: Select area for text extraction
- **Escape**: Cancel selection
- **Mouse Release**: Process selected area

## Error Handling

- The application will show a warning if the selected area is too small
- Error messages will be displayed if any issues occur during processing
- The application will safely close the selection window in case of errors

## Dependencies

- easyocr: For text recognition
- numpy: For image processing
- pynput: For keyboard monitoring
- tkinter: For GUI components
- Pillow (PIL): For screen capture
- pyperclip: For clipboard operations

## Contributing

Feel free to open issues or submit pull requests with improvements.
