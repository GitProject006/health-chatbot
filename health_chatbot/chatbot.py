import json
import random
import os
from symptom_model import predict_disease

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "diseases.json")

with open(file_path) as f:
    diseases = json.load(f)

def get_response(user_input):

    user_input = user_input.lower()

   

    greetings = ["hi", "hello", "hey", "hii", "good morning", "good evening"]

    if any(g in user_input for g in greetings):
        responses = [
            "Hey there! 👋 I'm your health buddy 🤖 How can I help you today?",
            "Hello! 😊 Tell me your symptoms or ask about a disease.",
            "Hi! 👋 I'm here to help with health questions."
        ]
        return random.choice(responses)

    if "how are you" in user_input:
        return "I'm doing great 😊 Thanks for asking! How are you feeling today?"

    if "thank" in user_input:
        return "You're welcome 😊 Always here to help!"

    if "who are you" in user_input:
        return "I'm an AI health chatbot 🤖 I can explain diseases, symptoms and common medicines."

    if "bye" in user_input:
        return "Take care! 👋 Stay healthy!"

   

    if "antacid" in user_input or "acidity" in user_input or "gas" in user_input or "heartburn" in user_input:

        return """
For acidity or stomach acid problems, common antacid medicines include:

💊 Calcium Carbonate (Tums)  
💊 Aluminum Hydroxide + Magnesium Hydroxide (Maalox)  
💊 Magnesium Hydroxide (Milk of Magnesia)  
💊 Omeprazole  
💊 Pantoprazole  

These medicines help reduce stomach acid and relieve heartburn.

⚠️ Always consult a doctor or pharmacist before using medication regularly.
"""

    if "fever medicine" in user_input or "medicine for fever" in user_input:

        return """
Common medicines used to reduce fever:

💊 Paracetamol (Acetaminophen)  
💊 Ibuprofen  
💊 Aspirin (for adults)

These medicines help lower body temperature and relieve pain.

⚠️ Drink plenty of fluids and rest. Seek medical advice if fever persists.
"""

    if "cough medicine" in user_input:

        return """
Common medicines for cough include:

💊 Dextromethorphan (cough suppressant)  
💊 Guaifenesin (expectorant)  
💊 Codeine-based syrups (prescription)  

Home remedies:
🍯 Honey with warm water  
☕ Ginger tea

⚠️ Persistent cough should be checked by a doctor.
"""

    if "cold medicine" in user_input or "common cold medicine" in user_input:

        return """
Common medicines for common cold:

💊 Paracetamol  
💊 Antihistamines (Cetirizine, Loratadine)  
💊 Decongestants (Pseudoephedrine)

Helpful remedies:
🍵 Warm fluids  
🛌 Rest

These help reduce symptoms like runny nose and body ache.
"""

    if "headache medicine" in user_input or "migraine medicine" in user_input:

        return """
Common medicines for headache or migraine:

💊 Paracetamol  
💊 Ibuprofen  
💊 Naproxen  
💊 Sumatriptan (for migraine)

Rest in a quiet room and drink water to help relieve headaches.
"""

    if "allergy medicine" in user_input:

        return """
Common medicines for allergies:

💊 Cetirizine  
💊 Loratadine  
💊 Fexofenadine  
💊 Diphenhydramine

These antihistamines reduce itching, sneezing and runny nose.
"""

    if "diarrhea medicine" in user_input:

        return """
Common medicines for diarrhea:

💊 Oral Rehydration Solution (ORS)  
💊 Loperamide  
💊 Bismuth Subsalicylate  

Important:
💧 Drink plenty of fluids to avoid dehydration.
"""

    if "pain medicine" in user_input:

        return """
Common pain relief medicines:

💊 Paracetamol  
💊 Ibuprofen  
💊 Diclofenac  
💊 Naproxen

These medicines reduce pain and inflammation.

⚠️ Do not exceed recommended dosage.
"""

    if "nausea medicine" in user_input or "vomiting medicine" in user_input:

        return """
Common medicines for nausea and vomiting:

💊 Ondansetron  
💊 Domperidone  
💊 Metoclopramide

Drink clear fluids and eat light food.
"""

    

    for disease in diseases:

        if disease.lower() in user_input:

            d = diseases[disease]

            symptoms = ", ".join(d["symptoms"])
            prevention = ", ".join(d["prevention"])

            return f"""
🩺 <b>{disease.title()}</b>

<b>Description:</b><br>
{d['description']}<br><br>

<b>Symptoms:</b><br>
{symptoms}<br><br>

<b>Causes:</b><br>
{d['causes']}<br><br>

<b>Prevention:</b><br>
{prevention}<br><br>

<b>Treatment:</b><br>
{d['treatment']}
"""

    predictions = predict_disease(user_input)

    if predictions:

        response = "Hmm 🤔 based on your symptoms it might be:<br><br>"

        for disease, prob in predictions:
            percent = round(prob * 100)
            response += f"🩺 {disease.title()} — {percent}% chance<br>"

        response += "<br>You can type the disease name if you want more details 🙂"

        return response

 

    return "I'm not sure I understood that 🤔 Try asking about symptoms, diseases, or medicines."
