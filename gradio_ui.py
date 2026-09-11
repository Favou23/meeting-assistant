### gradio ui configuration 
import os 
import gradio as gr
from main import process_meeting 


# custom_css = """
# /* Main application background */
# .gradio-container {
#     background: #f5f7fb !important;
#     max-width: 1200px !important;
#     margin: auto !important;
# }

# /* Main title */
# #app-title {
#     text-align: center;
#     font-size: 36px !important;
#     font-weight: 700 !important;
#     margin-bottom: 5px !important;
# }

# /* Subtitle */
# #app-subtitle {
#     text-align: center;
#     color: #667085 !important;
#     font-size: 16px !important;
#     margin-bottom: 30px !important;
# }

# /* Cards */
# .output-card {
#     background: white !important;
#     border: 1px solid #e4e7ec !important;
#     border-radius: 14px !important;
#     padding: 18px !important;
# }

# /* Process button */
# #process-button {
#     background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
#     color: white !important;
#     border: none !important;
#     border-radius: 10px !important;
#     font-size: 16px !important;
#     font-weight: 600 !important;
#     min-height: 48px !important;
# }

# /* Button hover */
# #process-button:hover {
#     opacity: 0.9 !important;
# }

# /* Section headings */
# .section-title {
#     font-size: 20px !important;
#     font-weight: 600 !important;
#     color: #101828 !important;
# }

# /* Audio input */
# .audio-box {
#     background: white !important;
#     border: 2px dashed #c7d2fe !important;
#     border-radius: 14px !important;
# }

# /* Download area */
# .download-box {
#     background: white !important;
#     border: 1px solid #e4e7ec !important;
#     border-radius: 14px !important;
#     padding: 15px !important;
# }
# """

# with gr.Blocks(css=custom_css) as demo:  <------- use this if youre going to add back the ui

with gr.Blocks() as demo:

    gr.Markdown("# 🎙️ Meeting Assistant")

    gr.Markdown(
        "Upload a meeting recording and generate a transcript and structured meeting minutes."
    )

    audio_input = gr.Audio(
        sources=["upload"],
        type="filepath",
        label="Meeting Audio"
    )

    process_button = gr.Button("Process Meeting")

    with gr.Row():

        transcript_output = gr.Textbox(
            label="Transcript",
            lines=20
        )

        summary_output = gr.Markdown(
            label="Meeting Summary"
        )

    download_file = gr.File(
        label="Download Meeting Minutes"
    )

    process_button.click(
        fn=process_meeting,
        inputs=audio_input,
        outputs=[
            transcript_output,
            summary_output,
            download_file
        ]
    )

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)