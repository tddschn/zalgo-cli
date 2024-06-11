#!/usr/bin/env python3

import gradio as gr
from zalgo_cli import zalgo, __version__

def generate_zalgo(string, adds_per_char, char_limit, amount, one_per_line):
    results = []
    if char_limit != 0:
        adds_per_char = (char_limit - len(string)) // len(string)

    for _ in range(amount):
        zalgo_text = zalgo(string, adds_per_char)
        results.append(zalgo_text)
    
    if one_per_line:
        return "\n".join(results)
    else:
        return "\t".join(results)

def gradio_app():
    with gr.Blocks() as app:
        gr.Markdown(f"# Zalgo Text Generator | Z̐ȃļg̡ò | [GitHub](https://github.com/tddschn/zalgo-cli) | Version {__version__}")
        
        with gr.Row():
            input_string = gr.Textbox(label="String to Zalgo-fy")
        
        with gr.Row():
            adds_per_char = gr.Number(label="Additions per Character", value=1)
            char_limit = gr.Number(label="Character Limit (0 for no limit)", value=0)
        
        with gr.Row():
            amount = gr.Number(label="Amount of Zalgo Text to Generate", value=1)
            one_per_line = gr.Checkbox(label="Output One Zalgo-fied String Per Line", value=False)
        
        output = gr.Textbox(label="Zalgo Text Output")
        
        generate_button = gr.Button("Generate")
        generate_button.click(
            fn=generate_zalgo, 
            inputs=[input_string, adds_per_char, char_limit, amount, one_per_line], 
            outputs=output
        )
    
    return app

def main() -> None:
    app = gradio_app()
    app.launch(share=True)

if __name__ == '__main__':
    main()