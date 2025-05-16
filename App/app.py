from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import textwrap

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model and tokenizer once
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

def generate_paragraph(prompt, max_length=200, temperature=0.7, top_p=0.9):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return textwrap.fill(result, width=100)

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "generated_text": None})

@app.post("/", response_class=HTMLResponse)
async def generate_text(request: Request, prompt: str = Form(...)):
    generated_text = generate_paragraph(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "generated_text": generated_text, "prompt": prompt})
