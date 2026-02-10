## TASK 5: SENTIMENT ANALYSIS WEB APPLICATION

    A web-based application that analyzes user-entered text and classifies its
    sentiment as Positive, Negative, or Neutral using Natural Language Processing.


## PROJECT FEATURES
    - Text sentiment analysis
    - Polarity and subjectivity calculation
    - Interactive web interface
    - Animated background UI
    - Color-coded sentiment output

## FOLDER STRUCTURE
Task5_Sentiment_Analysis_WebApp/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── background.mp4
│
├── screenshots/
│   ├── homepage.png
│   ├── positive_result.png
│   ├── negative_result.png
│   ├── neutral_result.png
│   └── project_structure.png
│
├── README.md
└── sentiment_report.txt

## SYSTEM REQUIREMENTS
    - Python 3.8 or above
    - Internet connection

## INSTALL REQUIRED PACKAGES
    Open Command Prompt / Terminal and run:
        pip install flask textblob
        python -m textblob.download_corpora

## HOW TO RUN THE PROJECT
    1. Open terminal inside project folder.
    2. Run the command:
        ** python app.py **

3. Open browser and visit:
    http://127.0.0.1:5000/

## OUTPUT
    - Displays sentiment classification
    - Shows polarity and subjectivity values
    - Results highlighted with colors

## IMPORTANT NOTES
    - Enter clear English sentences for better accuracy.
    - Do not rename template or static folders.
    - Background video is optional but recommended.
