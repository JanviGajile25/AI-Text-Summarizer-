"""
Gradio UI for AI Text Summarizer
Imports core logic from summarizer.py
"""
import gradio as gr
import time
from summarizer import generate_summary


def count_words(text):
    """Count words in text"""
    if not text:
        return 0
    return len(text.split())


def summarize_with_stats(input_text, min_length, max_length, progress=gr.Progress()):
    """
    Wrapper function that adds statistics to the summary
    
    Args:
        input_text: Text to summarize
        min_length: Minimum length of summary
        max_length: Maximum length of summary
        progress: Gradio progress tracker
    
    Returns:
        Tuple of (summary, stats_html)
    """
    if not input_text or input_text.strip() == "":
        return "⚠️ Please enter some text to summarize.", ""
    
    progress(0.2, desc="Preparing text...")
    
    # Count original words
    original_word_count = count_words(input_text)
    
    progress(0.4, desc="Generating summary...")
    
    # Generate summary using core logic
    start_time = time.time()
    summary_text = generate_summary(input_text, min_length, max_length)
    elapsed_time = time.time() - start_time
    
    progress(0.9, desc="Processing response...")
    
    # Calculate statistics
    summary_word_count = count_words(summary_text)
    compression_ratio = (1 - summary_word_count / original_word_count) * 100 if original_word_count > 0 else 0
    
    # Create stats HTML
    stats_html = f"""
    <div style="padding: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-top: 10px;">
        <h3 style="color: white; margin: 0 0 10px 0;">📊 Summary Statistics</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px;">
            <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                <div style="color: #fff; font-size: 12px; opacity: 0.9;">Original Words</div>
                <div style="color: #fff; font-size: 24px; font-weight: bold;">{original_word_count}</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                <div style="color: #fff; font-size: 12px; opacity: 0.9;">Summary Words</div>
                <div style="color: #fff; font-size: 24px; font-weight: bold;">{summary_word_count}</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                <div style="color: #fff; font-size: 12px; opacity: 0.9;">Compression</div>
                <div style="color: #fff; font-size: 24px; font-weight: bold;">{compression_ratio:.1f}%</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 8px;">
                <div style="color: #fff; font-size: 12px; opacity: 0.9;">Time Taken</div>
                <div style="color: #fff; font-size: 24px; font-weight: bold;">{elapsed_time:.1f}s</div>
            </div>
        </div>
    </div>
    """
    
    progress(1.0, desc="Complete!")
    
    return summary_text, stats_html


def clear_all():
    """Clear all inputs and outputs"""
    return "", "", "", 30, 130


def update_word_count(text):
    """Update word count display"""
    count = count_words(text)
    if count == 0:
        return "📝 Word count: 0"
    elif count > 1024:
        return f"📝 Word count: {count} ⚠️ (Will be truncated to 1500 characters)"
    else:
        return f"📝 Word count: {count}"


# Example texts for demonstration
examples = [
    [
        "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, "
        "and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. "
        "During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest "
        "man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York "
        "City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the "
        "addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler "
        "Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing "
        "structure in France after the Millau Viaduct.",
        30,
        130
    ],
    [
        "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural "
        "intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "
        "intelligent agents: any device that perceives its environment and takes actions that maximize its chance "
        "of successfully achieving its goals. Colloquially, the term artificial intelligence is often used to "
        "describe machines that mimic cognitive functions that humans associate with the human mind, such as "
        "learning and problem solving.",
        20,
        100
    ],
    [
        "Climate change refers to long-term shifts in temperatures and weather patterns. These shifts may be natural, "
        "but since the 1800s, human activities have been the main driver of climate change, primarily due to the burning "
        "of fossil fuels like coal, oil, and gas. Burning fossil fuels generates greenhouse gas emissions that act like "
        "a blanket wrapped around the Earth, trapping the sun's heat and raising temperatures. The main greenhouse gases "
        "that are causing climate change include carbon dioxide and methane. These come from using gasoline for driving "
        "a car or coal for heating a building, for example. Clearing land and cutting down forests can also release carbon dioxide.",
        25,
        120
    ]
]

# Custom CSS for better styling
custom_css = """
.gradio-container {
    font-family: 'Inter', sans-serif;
}
.main-header {
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 30px;
    border-radius: 15px;
    color: white;
    margin-bottom: 20px;
}
"""

# Create Gradio interface
with gr.Blocks(css=custom_css, title="AI Text Summarizer") as demo:
    
    # Header
    gr.HTML("""
        <div class="main-header">
            <h1 style="margin: 0; font-size: 2.5em;">📝 AI Text Summarizer</h1>
            <p style="margin: 10px 0 0 0; font-size: 1.2em; opacity: 0.95;">
                Transform long articles into concise summaries using DistilBART AI
            </p>
        </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📥 Input Text")
            
            input_text = gr.Textbox(
                label="",
                placeholder="Paste your article, document, or long text here...\n\nTip: Works best with 100-1000 words of formal text like news articles, research papers, or blog posts.",
                lines=12,
                max_lines=20,
                show_label=False
            )
            
            word_count_display = gr.Markdown("📝 Word count: 0")
            
            # Update word count on text change
            input_text.change(
                fn=update_word_count,
                inputs=input_text,
                outputs=word_count_display
            )
            
            gr.Markdown("### ⚙️ Summary Settings")
            
            with gr.Row():
                min_length = gr.Slider(
                    minimum=10,
                    maximum=100,
                    value=30,
                    step=5,
                    label="📏 Min Length",
                    info="Minimum words in summary"
                )
                max_length = gr.Slider(
                    minimum=50,
                    maximum=300,
                    value=130,
                    step=10,
                    label="📏 Max Length",
                    info="Maximum words in summary"
                )
            
            with gr.Row():
                summarize_btn = gr.Button(
                    "✨ Generate Summary", 
                    variant="primary", 
                    size="lg",
                    scale=2
                )
                clear_btn = gr.Button(
                    "🗑️ Clear", 
                    variant="secondary",
                    size="lg",
                    scale=1
                )
        
        with gr.Column(scale=1):
            gr.Markdown("### 📤 Generated Summary")
            
            output_text = gr.Textbox(
                label="",
                placeholder="Your AI-generated summary will appear here...",
                lines=12,
                max_lines=20,
                show_label=False
            )
            
            stats_display = gr.HTML("")
    
    # Examples section
    gr.Markdown("---")
    gr.Markdown("### 💡 Try These Examples")
    gr.Examples(
        examples=examples,
        inputs=[input_text, min_length, max_length],
        outputs=[output_text, stats_display],
        fn=summarize_with_stats,
        cache_examples=False,
        label=""
    )
    
    # Info section
    gr.Markdown("---")
    with gr.Row():
        with gr.Column():
            gr.HTML("""
                <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #667eea;">
                    <h3>🤖 About the AI Model</h3>
                    <ul>
                        <li><strong>Model:</strong> DistilBART (sshleifer/distilbart-cnn-12-6)</li>
                        <li><strong>Type:</strong> Abstractive Summarization</li>
                        <li><strong>Training:</strong> CNN/DailyMail dataset</li>
                        <li><strong>Capability:</strong> Generates new sentences (not just extraction)</li>
                        <li><strong>Speed:</strong> Optimized for fast local inference</li>
                    </ul>
                </div>
            """)
        
        with gr.Column():
            gr.HTML("""
                <div style="background: #e7f3ff; padding: 15px; border-radius: 10px; border-left: 4px solid #2196F3;">
                    <h3>💡 Tips for Best Results</h3>
                    <ul>
                        <li>Use formal text (news, articles, papers)</li>
                        <li>Input at least 100 words for good summaries</li>
                        <li>First request may take 20-30 seconds</li>
                        <li>Adjust length sliders based on input size</li>
                    </ul>
                </div>
            """)
    
    gr.Markdown("""
        ---
        <div style="text-align: center; color: #666; padding: 20px;">
            <p>⚡ Powered by Hugging Face Transformers | 🚀 Built with Gradio</p>
            <p style="font-size: 0.9em;">Running locally with DistilBART - No API required!</p>
        </div>
    """)
    
    # Connect button to function
    summarize_btn.click(
        fn=summarize_with_stats,
        inputs=[input_text, min_length, max_length],
        outputs=[output_text, stats_display]
    )
    
    # Connect clear button
    clear_btn.click(
        fn=clear_all,
        inputs=[],
        outputs=[input_text, output_text, stats_display, min_length, max_length]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()
