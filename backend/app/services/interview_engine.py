from typing import Dict, Any, List

INTERVIEW_QUESTION_BANK = {
    "Technical": {
        "AI Engineer": [
            "Explain the difference between Supervised, Unsupervised, and Reinforcement Learning with real-world examples.",
            "What is Retrieval-Augmented Generation (RAG) and how does it prevent LLM hallucinations?",
            "How do Transformer models compute Self-Attention? What is the mathematical intuition behind Scaled Dot-Product Attention?",
            "What is the difference between PyTorch `nn.Module` and raw tensor operations? How does autograd compute gradients?",
            "How would you deal with an imbalanced dataset in a machine learning classification problem?"
        ],
        "Software Developer": [
            "What is the difference between process and thread? How does asynchronous programming work in JavaScript / Python?",
            "Explain RESTful API best practices and how HTTP GET differs from POST, PUT, and PATCH.",
            "What are database indexes? How do B-Trees optimize database search operations, and what is the trade-off of indexing?",
            "Explain the SOLID principles of Object-Oriented Software Design.",
            "How do React `useState` and `useEffect` hooks manage component lifecycle and state updates?"
        ]
    },
    "HR": {
        "General": [
            "Tell me about yourself, your educational background, and why you are interested in this role.",
            "Where do you see yourself professionally in 3 to 5 years?",
            "What is your greatest technical strength, and what is one area you are working to improve?",
            "Describe a time when you had to work under tight project deadlines or high pressure.",
            "Why do you want to join our company specifically?"
        ]
    },
    "System Design": {
        "General": [
            "How would you design a scalable URL shortener service like Bit.ly?",
            "How would you design a real-time Chat application supporting 1 million active users?",
            "Design a distributed rate limiter to protect public API endpoints from DDoS attacks.",
            "How would you design a Retrieval-Augmented Generation (RAG) backend that processes 10,000 PDFs daily?"
        ]
    }
}

def get_next_question(target_role: str, interview_type: str, question_index: int) -> str:
    category = INTERVIEW_QUESTION_BANK.get(interview_type, INTERVIEW_QUESTION_BANK["Technical"])
    role_questions = category.get(target_role, category.get("General", category.get("Software Developer", [])))
    
    if question_index < len(role_questions):
        return role_questions[question_index]
    return "Thank you! You have completed all questions in this interview session."

def evaluate_answer(question: str, user_answer: str) -> Dict[str, Any]:
    ans_length = len(user_answer.strip())
    
    if ans_length < 20:
        score = 4.0
        strengths = ["Attempted to provide an answer."]
        weaknesses = ["Answer is very brief and lacks depth or technical details."]
        improved = f"In response to '{question}', provide a structured answer explaining key concepts, practical trade-offs, and an example implementation."
    elif ans_length < 80:
        score = 6.5
        strengths = ["Addresses the primary core concept."]
        weaknesses = ["Could include more specific technical terms and concrete examples."]
        improved = f"To score higher on '{question}', state the core definition, explain the underlying mechanism step-by-step, and reference a real-world scenario."
    else:
        score = 8.5
        strengths = ["Comprehensive answer with solid technical vocabulary.", "Clear explanation of concepts and context."]
        weaknesses = ["Minor: Could explicitly highlight trade-offs or alternative edge cases."]
        improved = f"Excellent answer! To make it top 1%: mention exact metrics, specific framework tools, and architectural edge cases."

    return {
        "score": score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "improved_answer_sample": improved
    }
