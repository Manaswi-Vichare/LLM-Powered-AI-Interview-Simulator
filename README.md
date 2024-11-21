# LLM-Powered-AI-Interview-Simulator
This tool acts as a tool for practicing technical interviews in a simulated environment. It supports various interview types like coding, system design, machine learning, SQL, and logic. Users can run the service in demo mode or locally for a more personalized experience. The tool employs a speech-first interface using AI models for speech-to-text (STT), text-to-speech (TTS), and Large Language Models (LLM). Configuration is managed via a .env file, and it supports models from OpenAI, Hugging Face, and local setups. Legal disclaimers, usage responsibilities, and setup instructions are also detailed.

**Configure the environment:** \
Create the .env file from the provided example and edit the .env file to include your API keys for the models you wish to use: 
```
cp .env.openai.example .env 
nano .env
```
Example:
```
OPENAI_API_KEY=sk-YOUR_OPENAI_API_KEY
LLM_URL=https://api.openai.com/v1
LLM_TYPE=OPENAI_API
LLM_NAME=gpt-3.5-turbo
```

**Run the Application:** \
Install the dependencies:
```
pip install -r requirements.txt
```

Run the application:
```
python app.py
```
Access the application at http://localhost:7860.

**References:** \
[Github Repository](https://github.com/IliaLarchenko/Interviewer?tab=readme-ov-file)
