from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class MedicalNLPModel:
    def __init__(self, model_id="Qwen/Qwen2.5-1.5B-Instruct", device="cuda"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=None
        )

    def generate_response(self, prompt: str, max_tokens=1024):
        inputs = self.tokenizer([prompt], return_tensors="pt").to(self.device)

        with torch.no_grad():
            generated = self.model.generate(inputs.input_ids, max_new_tokens=max_tokens)

        return self.tokenizer.batch_decode(generated[:, inputs.input_ids.shape[-1]:], skip_special_tokens=True)[0]
