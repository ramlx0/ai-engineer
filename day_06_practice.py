from pydantic import BaseModel, Field ,field_validator

class LLMRequest(BaseModel):
    prompt: str
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=150, gt=0, le=4096)

    @field_validator('prompt')
    @classmethod
    def check_prompts_not_empty(cls , value : str ) -> str:
        if not value.strip():
            raise ValueError('prompt not empty')
        return value
    # broken prompt test
try:
    bad_prompt = LLMRequest(prompt='')
    print('bad payload', bad_prompt)
except Exception as e:
    print('\n caught black prompt' , e)

        


    
# Valid Data
valid_data = LLMRequest(prompt="explain rag", temperature=0.7, max_tokens="200")

# Exporting data
print("As Python Dict:", valid_data.model_dump())
print("As JSON String:", valid_data.model_dump_json())

