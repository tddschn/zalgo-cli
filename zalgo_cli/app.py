#!/usr/bin/env python3

import gradio as gr
from zalgo_cli import zalgo, __version__

def generate_zalgo(string, adds_per_char, char_limit, amount, one_per_line, codepoints_str):
    results = []
    codepoints_to_add = [int(cp, 16) for cp in codepoints_str.strip().split()] if codepoints_str else None
    
    if char_limit != 0:
        adds_per_char = (char_limit - len(string)) // len(string)

    for _ in range(amount):
        zalgo_text = zalgo(string, adds_per_char, codepoints_to_add)
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
        
        with gr.Row():
            codepoints_str = gr.Textbox(label="Codepoints to Add (space-separated hex values, e.g., '0x036D 0x0368')", value="")
        
        output = gr.Textbox(label="Zalgo Text Output", show_copy_button=True)
        
        generate_button = gr.Button("Generate")
        generate_button.click(
            fn=generate_zalgo, 
            inputs=[input_string, adds_per_char, char_limit, amount, one_per_line, codepoints_str], 
            outputs=output
        )
        
        examples = [
            ["Hello World | Click me and hit the Generate button a few times to get different results", 1, 0, 1, False, ""],
            ["tc", 2, 20, 2, True, "0x036D 0x0368"]
        ]
        
        gr.Examples(examples=examples, inputs=[input_string, adds_per_char, char_limit, amount, one_per_line, codepoints_str])
    
    return app

def main() -> None:
    app = gradio_app()
    app.launch(share=True)

if __name__ == '__main__':
    main()
