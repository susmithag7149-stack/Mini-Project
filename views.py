from django.shortcuts import render

def home(request):
    response = ""

    if request.method == "POST":
        message = request.POST.get("message")

        if "hello" in message.lower():
            response = "Hello! How can I help you?"
        elif "name" in message.lower():
            response = "I am a Django Chatbot."
        elif "bye" in message.lower():
            response = "Goodbye!"
        else:
            response = "Sorry, I don't understand."

    return render(request, "home.html", {"response": response})