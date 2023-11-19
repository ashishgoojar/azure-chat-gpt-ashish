# chatapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
import openai
key="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"
openai.api_key = key

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        print(user_input)
        # Use OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        chat_response = response.choices[0].text.strip()
        print(chat_response)
        return JsonResponse({'response': chat_response})

    return render(request, 'chatapp/chat.html')
