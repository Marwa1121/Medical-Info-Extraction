import json
from .llm_model import MedicalNLPModel
from .models import MedicalReportDetails

# Load model once
nlp_model = MedicalNLPModel()

def extract_medical_details(report: str):
    prompt_messages = [
        {
            "role": "system",
            "content": "\n".join([
                "You are an expert medical NLP parser.",
                "You will receive a raw medical report in natural language.",
                "Your task is to extract structured information as per the provided Pydantic schema.",
                "The output must strictly follow JSON format and match the schema attributes.",
                "Keep the report's original language.",
                "Do not include explanations or headers—output only clean JSON."
            ])
        },
        {
            "role": "user",
            "content": "\n".join([
                "## Medical Report:",
                report.strip(),
                "",
                "## Pydantic Schema:",
                json.dumps(MedicalReportDetails.model_json_schema(), ensure_ascii=False),
                "",
                "## Extracted JSON:",
                "```json"
            ])
        }
    ]

    prompt = nlp_model.tokenizer.apply_chat_template(prompt_messages, tokenize=False, add_generation_prompt=True)
    response_text = nlp_model.generate_response(prompt)

    try:
        response_json = json.loads(response_text)
        return {"status": "success", "data": response_json}
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON output."}
