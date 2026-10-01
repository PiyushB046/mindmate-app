# 🧠 MindMate

A mental health companion app built with Streamlit. Chat with a locally running Llama 3 model, or play short games that look at how you answer and estimate the mood behind your words.

> **Not a medical tool.** MindMate is a learning project. Its predictions are rough guesses from a simple text model and are not a diagnosis. If you are struggling, please reach out to a mental health professional or a local helpline.

## Features

- **💬 Chatbot**: talk to MindMate, powered by Llama 3 running on your own machine through [Ollama](https://ollama.com). Nothing you type leaves your computer.
- **🎯 Trivia**: answer a mix of fun and wellbeing questions in your own words. Each answer is classified by the mood model.
- **🟰 This or That**: pick between two options and see the mood predicted for each choice.
- **💭 Cognitive Reframe**: type a negative thought and the chatbot rewrites it as a kinder, more constructive one.

## How it works

| Part | What it does |
|---|---|
| `app.py` | Streamlit UI with the Chatbot and Games tabs |
| `chatbot_llama.py` | Sends prompts to the local Ollama API (`llama3`) |
| `ml_model.py` | Loads the saved model and predicts a label for a piece of text |
| `train_model.py` | Trains the mood classifier and saves it to `models/` |
| `utils.py` | Loads the game questions from `data/` |
| `data/` | Question sets for the games (JSON) |
| `models/` | Trained classifier and TF-IDF vectorizer |

The mood classifier is a TF-IDF vectorizer (top 5,000 terms) feeding a Logistic Regression model. It labels text as one of four classes: **Normal**, **Anxiety**, **Depression** or **Stress**.

## Getting started

You need Python 3.10+ and [Ollama](https://ollama.com/download).

1. Clone the repo and install the dependencies:

   ```bash
   git clone https://github.com/PiyushB046/mindmate-app.git
   cd mindmate-app
   pip install -r requirements.txt
   ```

2. Download the chat model and make sure Ollama is running:

   ```bash
   ollama pull llama3
   ```

3. Start the app:

   ```bash
   streamlit run app.py
   ```

Trivia and This or That work without Ollama, since they only use the saved classifier. The Chatbot tab and the Cognitive Reframe game need Ollama running at `http://localhost:11434`.

## Retraining the model

A trained model is already included in `models/`, so this step is optional.

The training data is not stored in this repo. `train_model.py` expects a CSV with `statement` and `status` columns at:

```
Mental-Health-Classification-Dataset/data/combined_data.csv
```

The original file had about 53,000 labelled statements. Put your copy at that path, then run:

```bash
python train_model.py
```

This prints a classification report and overwrites the files in `models/`.

## Tech stack

Python · Streamlit · scikit-learn · Ollama (Llama 3) · pandas
