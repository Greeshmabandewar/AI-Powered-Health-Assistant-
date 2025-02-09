import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')


# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")



def healthcare_chatbot(user_input):
    # Simple rule-based keywords to respond
    if "symptom" in user_input:
        return "Your symptoms suggest you should consult a doctor.  Accurate diagnosis and treatment require a medical professional's expertise.  Don't rely on guesswork; seek professional medical advice for your health. "
    elif "appointment" in user_input:
        return "Can I help you schedule a doctor's appointment?  Professional medical advice is crucial for accurate diagnosis and treatment.  It's always best to seek expert guidance for health concerns."
    elif "medication" in user_input:
        return "Consistent use of your prescribed medication is crucial for successful treatment and recovery. 1   Interrupting your medication schedule by skipping doses or stopping prematurely can negatively impact your health. 2   Should you have any questions regarding your medication, including side effects or dosage, promptly consult your physician.  Your doctor is best equipped to provide guidance for your optimal well-being"
    elif "headache" in user_input:
        return "Many headaches respond well to simple self-care strategies.  Hydration is key, as dehydration can be a common trigger.  Resting in a calm, darkened space can ease discomfort, particularly for migraines.  Applying a compress, either cold or warm, can offer relief by numbing pain or relaxing muscles.  Stress management techniques like deep breathing, meditation, or massage can help prevent tension headaches.  Reducing screen time can minimize eye strain, another frequent cause.  Over-the-counter pain relievers can be an option, but use them cautiously.  Regular, healthy sleep is also important for headache prevention.  If your headaches are frequent, severe, or worsen, it's essential to see a doctor for diagnosis and treatment."
    elif "fever" in user_input: 
        return "Fevers, often a sign of infection, can frequently be managed at home.  Staying well-hydrated is crucial, as fever can lead to dehydration.  Resting in a cool, comfortable space aids recovery.  Light clothing and a cool compress on the forehead can offer relief.  Warm liquids like herbal tea or soup can be soothing.  Over-the-counter medications such as paracetamol or ibuprofen can help reduce fever if necessary.  A lukewarm sponge bath may also be helpful.  However, if the fever continues, becomes very high, or is accompanied by severe symptoms, it's important to consult a doctor for diagnosis and treatment."
    else:
      
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
       
        return response[0]['generated_text']


# Streamlit web app interface
def main():
    st.title("AI- Powered Health Assistant Chatbot")
    

    user_input = st.text_input("Share your medical problem ?", "")

    
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
           
            with st.spinner("Processing please wait..."):
                response = healthcare_chatbot(user_input)
            print("response ",response)
            print("=======================================================")
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Enter your query.")
if __name__ == "__main__":
    main()
