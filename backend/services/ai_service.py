import logging
from google import genai
from backend.core.config import settings

logger = logging.getLogger(__name__)

class AIProcessingError(Exception):
    pass

class AIService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate_ui_component(self, prompt: str):
        try:
            logger.info(f"Requesting AI generation for prompt: '{prompt}'")
            
            # AI ko ekdum strict instructions de rahe hain
            # AI ko ab hum Coder ke sath-sath Pro Designer bhi bana rahe hain!
            system_instruction = (
                "You are an expert React developer and a Senior UI/UX Designer. "
                "You MUST return ONLY valid, raw React JSX code. "
                "CRITICAL DESIGN RULES: "
                "1. ONLY use Tailwind CSS classes for styling. NEVER use raw CSS, inline styles, or <style> tags. "
                "2. The UI MUST be beautiful, modern, and premium. "
                "3. Use flexbox/grid to properly align and center elements on the screen. "
                "4. Use generous padding (p-4, p-8), smooth shadows (shadow-lg, shadow-2xl), rounded corners (rounded-2xl), and modern color palettes (e.g., gradients, slate/gray dark modes). "
                "5. Make buttons interactive with hover states (hover:bg-..., transition-all, transform). "
                "DO NOT include conversational text, explanations, or markdown formatting (like ```jsx). "
                "Always start with imports (e.g., import React from 'react';) and end with 'export default App;'. "
                "Use 'lucide-react' for modern icons."
            )
            
            final_prompt = f"{system_instruction}\n\nUser Request: {prompt}"

            response = self.client.models.generate_content(
                model='gemini-3.6-flash',
                contents=final_prompt
            )
            
            # AI ki hoshiyari (markdown backticks) ko saaf karne ka filter
            clean_code = response.text.strip()
            if clean_code.startswith("```"):
                lines = clean_code.split('\n')
                if lines[0].startswith("```"):
                    lines = lines[1:]  # Upar wala ```jsx hatao
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1] # Neeche wala ``` hatao
                clean_code = '\n'.join(lines)
                
            return clean_code
            
        except Exception as e:
            logger.error(f"Error during AI generation: {str(e)}")
            raise AIProcessingError(f"Generation failed: {str(e)}")

ai_service = AIService()