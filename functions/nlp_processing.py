import spacy
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("en_core_web_sm")

model = SentenceTransformer('all-MiniLM-L6-v2')

intents = {
    "open_notepad": ["open notepad", "start notepad", "launch notepad"],
    "open_calculator": ["open calculator", "start calculator", "launch calc"],
    "find_ip": ["find ip", "what is my ip address", "find my ip address"],
    "open_cmd": ["open command prompt", "start cmd", "launch terminal"],
    "open_camera": ["open camera", "start camera", "launch camera"],
    "weather": ["what's the weather like", "tell me the weather", "weather update"],
    "wikipedia": ["search on Wikipedia", "lookup Wikipedia", "Wikipedia search"],
    "google": ["search on Google", "find on Google", "Google search"],
    "youtube": ["play on YouTube", "open YouTube", "search YouTube"],
    "news": ["latest news", "what's in the news", "current headlines"],
    "joke": ["tell me a joke", "make me laugh", "say something funny"],
    "advice": ["give me an advice", "motivation", "inspire me"],
    "set_reminder": ["Set my reminder","Can you set a reminder"],
    "add_todo": ["Add to my todo","Add these to my list"],
    "show_todo": ["Show my to do list","What is in my list"],
    "send_email": ["Send an email"],
    "send_whatsapp": ["Send whatsapp"],
    
}

intent_embeddings = {key: model.encode(value, convert_to_tensor=True) for key, value in intents.items()}


def recognize_intent(user_input):
    """
    Recognizes the intent of user input using sentence similarity.
    """
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    
    best_match = None
    highest_similarity = 0.0
    
    for intent, embeddings in intent_embeddings.items():
        similarity = util.pytorch_cos_sim(user_embedding, embeddings).max().item()
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = intent

    return best_match if highest_similarity > 0.5 else "unknown"
