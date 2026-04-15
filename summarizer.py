"""
Core summarization logic using Hugging Face Transformers
"""
from transformers import BartTokenizer, BartForConditionalGeneration

# Load model and tokenizer globally (only once)
print("Loading DistilBART model...")
model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
print("Model loaded successfully!")


def generate_summary(text, min_len=30, max_len=120):
    """
    Generate summary from input text using DistilBART model
    
    Args:
        text (str): Input text to summarize
        min_len (int): Minimum length of summary
        max_len (int): Maximum length of summary
    
    Returns:
        str: Generated summary or error message
    """
    # Check if text is empty
    if not text or text.strip() == "":
        return "⚠️ Please enter some text to summarize."
    
    # Truncate very long text (to prevent memory issues)
    max_input_chars = 1500
    if len(text) > max_input_chars:
        text = text[:max_input_chars]
        truncation_warning = f"⚠️ Input truncated to {max_input_chars} characters.\n\n"
    else:
        truncation_warning = ""
    
    try:
        # Tokenize input
        inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)
        
        # Generate summary
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=int(max_len),
            min_length=int(min_len),
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        
        # Decode summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return truncation_warning + summary
    
    except Exception as e:
        return f"❌ Error generating summary: {str(e)}"
