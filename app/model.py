import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from .utils.abbreviations import ABBREVIATIONS
import re

class Summarizer:
    def __init__(self, model_path, tokenizer_path):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = T5ForConditionalGeneration.from_pretrained(model_path).to(self.device)
        self.tokenizer = T5Tokenizer.from_pretrained(tokenizer_path)

    @staticmethod
    def clean_text(text):
        text = re.sub(r'\r\n', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'<.*?>', '', text)
        return text
    

    @staticmethod
    def format_summary(text):
        text = text.strip()
        if not text:
            return text

        
        text = re.sub(r'([.!?;:])\s*([A-Za-z])', r'\1 \2', text)
        text = re.sub(r'([.!?])\s*([A-Za-z])', r'\1 \2', text)

    
        text = text[0].upper() + text[1:]

        
        if text and text[0].isalpha():
            text = text[0].upper() + text[1:]
        
        def capitalize_after_punct(match):
            punct = match.group(1)
            letter = match.group(2)
            return f"{punct} {letter.upper()}"

        text = re.sub(r'([.!?])\s*([a-z])', capitalize_after_punct, text)
        
        for key, value in ABBREVIATIONS.items():
            text = re.sub(rf'\b{key}\b', value, text, flags=re.IGNORECASE)

        text = re.sub(r'\s+', ' ', text).strip()

        if text and not text[-1] in '.!?':
            text += '.'

        return text


    def summarize(self, text):
        text = self.clean_text(text)
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
        inputs = {key: value.to(self.device) for key, value in inputs.items()}

        outputs = self.model.generate(
            inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            max_length=200,
            num_beams=5,
            early_stopping=True,
            min_length=50,
            no_repeat_ngram_size=3
        )
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        summary = self.format_summary(summary)
        return summary