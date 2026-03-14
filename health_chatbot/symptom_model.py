from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_data = [

("high fever headache joint pain muscle pain rash nausea vomiting fatigue", "dengue"),

("fever chills sweating headache fatigue nausea vomiting body ache", "malaria"),

("frequent urination increased thirst fatigue blurred vision weight loss hunger", "diabetes"),

("high blood pressure headache dizziness nosebleeds chest pain fatigue", "hypertension"),

("persistent cough chest pain weight loss night sweats fever fatigue", "tuberculosis"),

("high fever stomach pain weakness loss appetite diarrhea constipation", "typhoid"),

("watery diarrhea dehydration nausea vomiting muscle cramps weakness", "cholera"),

("fever cough sore throat body ache fatigue headache runny nose", "influenza"),

("fever cough breathing difficulty loss taste smell fatigue sore throat", "covid"),

("chest pain breathing difficulty cough fever chills fatigue", "pneumonia"),

("wheezing shortness breath chest tightness coughing fatigue", "asthma"),

("cough mucus chest discomfort fatigue breathing difficulty", "bronchitis"),

("yellow skin abdominal pain nausea fatigue dark urine", "hepatitis"),

("itchy skin rash redness swelling dryness irritation", "skin allergy"),

("joint stiffness pain swelling reduced mobility fatigue", "arthritis"),

("burning stomach pain bloating nausea vomiting indigestion", "gastritis"),

("burning stomach pain nausea bloating heartburn weight loss", "peptic ulcer"),

("severe headache nausea sensitivity light vision problems", "migraine"),

("fatigue pale skin dizziness shortness breath weakness", "anemia"),

("sadness loss interest fatigue sleep problems anxiety", "depression")

]

texts = [t[0] for t in training_data]
labels = [t[1] for t in training_data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_disease(symptoms):

    X_test = vectorizer.transform([symptoms])

    probs = model.predict_proba(X_test)[0]

    diseases = model.classes_

    results = []

    for i in range(len(diseases)):
        results.append((diseases[i], probs[i]))

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:3]