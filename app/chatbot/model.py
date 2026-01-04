from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "microsoft/phi-2"

# Load once at startup
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    dtype=torch.float32,
    low_cpu_mem_usage=False
)

model.to("cpu")
model.eval()


def generate_reply(message: str, history=None, max_new_tokens=40):
    if history is None:
        history = []

    # ✅ Phi-2 expects plain text, not chat tokens
    prompt = ""

    for h in history:
        prompt += f"User: {h}\nAssistant: {h}\n"

    prompt += f"User: {message}\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
            repetition_penalty=1.1,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    # Decode only new tokens
    reply = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    return reply.strip()




