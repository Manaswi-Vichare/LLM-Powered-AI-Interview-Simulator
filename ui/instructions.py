import gradio as gr

from utils.ui import get_status_color

INTRO = """
# Welcome to the AI Interviewer Bot!
This tool provides a platform to simulate realistic technical interviews, helping you sharpen your skills in areas like coding, machine learning, system design, and more. While it offers an interactive way to refine your interview techniques, it complements, rather than replaces, rigorous preparation such as studying algorithms and solving coding challenges.
"""

INTERFACE = """
# Interface

The AI Interviewer supports various interview formats, including Coding, System Design, Machine Learning System Design, Math, Statistics, Logic, SQL, and ML Theory. Each format is designed to target specific skill sets and knowledge areas. Additionally, you can select the Custom interview option to focus on any topic of your choice, where the AI will create a problem based on your input. Here’s how to use the interface effectively:

### Setting

Adjust the interview settings to specify the difficulty level, topic, and any particular requirements. Start the interview by clicking the **"Generate a problem"** button.

### Problem Statement
The AI will present a problem after you initiate the session.

### Solution
This section is where the interaction happens:
- **Code/Solution Area**: On the left side, you will find a space to write your solution. For codding problem you can use any language, although syntax highlighting is only available for Python and SQL.
- **Communication Area**: On the right, this area includes:
  - **Chat History**: Displays the entire dialogue history, showing messages from both you and the AI interviewer. Your recognized speech will be shown here before being sent to the AI.
  - **Audio Record Button**: Use this button to record your responses. Press to start recording, speak your thoughts, and press stop to send your audio. Wait until everything you said is transcribed and then click stop. Your message will be sent to the chat, along with a snapshot of your code or any notes from solution text area."

Interact with the AI just as you would with a live interviewer. Offer clear and concise responses, providing updates regularly instead of lengthy monologues. All your interactions, including code explanations, will be recorded, with the AI's replies displayed in the chat and read aloud. Respond to follow-up questions and follow the AI's guidance as needed.

Once the interview is completed, or if you decide to end it early, click the **"Finish the interview"** button.

### Feedback
Comprehensive feedback will be available in this section once the interview concludes, offering insights into your performance and highlighting areas where you can improve.
"""


def get_instructions_ui(llm, tts, stt, default_audio_params):
    with gr.Tab("Instruction", render=False) as instruction_tab:
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown(INTRO)
            with gr.Column(scale=1):
                space = "&nbsp;" * 10

                tts_status = get_status_color(tts)
                gr.Markdown(f"TTS status: {tts_status}{space}{tts.config.tts.name}", elem_id="tts_status")

                stt_status = get_status_color(stt)
                gr.Markdown(f"STT status: {stt_status}{space}{stt.config.stt.name}", elem_id="stt_status")

                llm_status = get_status_color(llm)
                gr.Markdown(f"LLM status: {llm_status}{space}{llm.config.llm.name}", elem_id="llm_status")

        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown(INTERFACE)
            with gr.Column(scale=1):
                chat_example = gr.Chatbot(
                    label="Chat", show_label=False, show_share_button=False, value=[["Candidate message", "Interviewer message"]]
                )
                audio_input_example = gr.Audio(interactive=True, **default_audio_params)

    return instruction_tab
