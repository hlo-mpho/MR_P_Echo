import os
import time
from gtts import gTTs

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')
    time.sleep(2)

def introduction():
    speak("Hello, I'm Echo, your smart assistant for Mr Price! How can I assist you today?")
    time.sleep(4)

def product_recommendations():
    speak("Sure! What type of products are you interested in?")
    category = input("Please specify the product category (e.g., electronics, fashion, homeware): ").lower()
    speak(f"Let me find the best {category} for you!")
    time.sleep(2)
    speak(f"I have found the top-rated {category} products for you. Please check the Mr Price app or website for details.")

def discounts_and_offers():
    speak("Great! Let me fetch the best discounts and offers available for you.")
    time.sleep(2)
    speak("Here are the top discounts: Up to 50% off on selected fashion items and up to 30% off on electronics. Check your Mr Price app for more details.")

def order_tracking():
    speak("Please provide your order number, and I will check the status for you.")
    order_number = input("Enter your order number: ").strip()
    speak(f"Your order number {order_number} is currently being processed. You will receive a notification once it is shipped.")

def display_faq():
    speak("Here are some frequently asked questions:")
    faqs = {
        "1. What are your store hours?": "Our stores are open from 9 AM to 9 PM from Monday to Saturday, and from 10 AM to 6 PM on Sundays.",
        "2. What is your return policy?": "You can return items within 30 days of purchase with a valid receipt. Terms and conditions apply.",
        "3. Do you offer delivery?": "Yes, we offer delivery for online purchases. You can check delivery options at checkout.",
        "4. How can I track my order?": "You can track your order using the tracking number provided in your order confirmation email or by contacting customer support."
    }
    for question, answer in faqs.items():
        print(f"{question}\nAnswer: {answer}\n")
        speak(question)
        speak(answer)
        time.sleep(1)

def handle_query():
    speak("You can ask me anything about Mr Price, and I'll do my best to assist!")
    query = input("Please type your question: ").lower()
    responses = {
        "store hours": "Our stores are open from 9 AM to 9 PM from Monday to Saturday, and from 10 AM to 6 PM on Sundays.",
        "return policy": "You can return items within 30 days of purchase with a valid receipt. Terms and conditions apply.",
        "delivery options": "Yes, we offer delivery for online purchases. Check the available options at checkout."
    }
    for key in responses:
        if key in query:
            speak(responses[key])
            break
    else:
        speak("Sorry, I don't have an answer for that at the moment. Please check our website or contact customer support.")

def invalid_choice():
    speak("Sorry, I didn't understand your choice. Please try again.")

def customer_interaction():
    while True:
        print("How can I assist you today? Please select one of the following options:")
        print("1. Product recommendations")
        print("2. Discounts and offers")
        print("3. Order tracking")
        print("4. FAQ")
        print("5. Ask a query")
        print("6. Exit")
        
        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            product_recommendations()
        elif choice == '2':
            discounts_and_offers()
        elif choice == '3':
            order_tracking()
        elif choice == '4':
            display_faq()
        elif choice == '5':
            handle_query()
        elif choice == '6':
            speak("Thank you for using Echo! Have a great day!")
            break
        else:
            invalid_choice()

if __name__ == "__main__":
    introduction()
    customer_interaction()
