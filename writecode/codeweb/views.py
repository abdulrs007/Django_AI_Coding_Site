import openai
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Code


def home(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'kotlin',
                 'markup', 'markup-templating', 'matlab', 'mongodb', 'objectvec', 'perl', 'php', 'powershell', 'python',
                 'r', 'regex', 'ruby', 'rust', 'sql', 'swift', 'typescript', 'yaml']

    if request.method == "POST":
        code = request.POST.get('code', '').strip()
        lang = request.POST.get('lang', '')

        if not code:
            return render(request, 'home.html', {
                "lang_list": lang_list,
                "code": code,
                "lang": lang,
                "alert_message": "Please enter some code before submitting."
            })

        # Check to confirm a programming langauage is selected
        if lang == "Select Language":
            # messages.success(request, "Hey! You Forgot to Select a Language..")
            return render(request, 'home.html', {"lang_list": lang_list, "code": code, "lang": lang,
                                                 "alert_message": "Hey! You Forgot to Select a Language.."})
        else:
            # OPENAI
            openai.api_key = settings.OPENAI_API_KEY

            # Make an API request
            try:
                messages = [
                    {
                        "role": "system",
                        "content": (
                            f"You are an expert {lang} developer. "
                            f"Please return only the corrected {lang} code—no explanations or extra text."
                        )
                    },
                    {
                        "role": "user",
                        "content": code
                    }
                ]

                result = openai.chat.completions.create(
                    model="gpt-4",
                    messages=messages,
                    temperature=0,
                    max_tokens=2000,
                )
                ai_output = result.choices[0].message.content

                # Save To Database
                record = Code(question=code, code_answer=ai_output, language=lang, user=request.user)
                record.save()

            except Exception as e:
                ai_output = f"Error from OpenAI: {e}"

            return render(request, 'home.html', {
                "lang_list": lang_list, "code": code, "response": ai_output, "lang": lang
            })

    return render(request, 'home.html', {"lang_list": lang_list})


def suggest(request):
    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'kotlin',
                 'markup', 'markup-templating', 'matlab', 'mongodb', 'objectvec', 'perl', 'php', 'powershell', 'python',
                 'r', 'regex', 'ruby', 'rust', 'sql', 'swift', 'typescript', 'yaml']

    if request.method == "POST":
        code = request.POST.get('code', '').strip()
        lang = request.POST.get('lang', '')

        if not code:
            return render(request, 'suggest.html', {
                "lang_list": lang_list,
                "code": code,
                "lang": lang,
                "alert_message": "Please enter some code before submitting."
            })

        # Check to confirm a programming language is selected
        if lang == "Select Language":
            # messages.success(request, "Hey! You Forgot to Select a Language..")
            return render(request, 'suggest.html', {"lang_list": lang_list, "code": code, "lang": lang,
                                                    "alert_message": "Hey! You Forgot to Select a Language.."})
        else:
            # OPENAI
            openai.api_key = settings.OPENAI_API_KEY

            # build a system prompt that enforces the target language
            system_prompt = (
                f"You are an expert {lang} developer. "
                f"When given a request, respond only with {lang} code snippets—"
                "no explanations or extra text."
            )

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": code},
            ]

            # Make an API request
            try:
                result = openai.chat.completions.create(
                    model="gpt-4",
                    messages=messages,
                    temperature=0.7,  # adjust for more/less creativity
                    max_tokens=1000,
                )
                ai_output = result.choices[0].message.content

                # Save To Database
                record = Code(question=code, code_answer=ai_output, language=lang, user=request.user)
                record.save()

            except Exception as e:
                ai_output = f"Error from OpenAI: {e}"

            return render(request, 'suggest.html', {
                "lang_list": lang_list, "code": code, "response": ai_output, "lang": lang
            })

    return render(request, 'suggest.html', {"lang_list": lang_list})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successful..")
            return redirect('home')
        else:
            messages.success(request, "error logging In, Please Try Again..")
            return redirect('home')

    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # add a flash message
            messages.success(request, "You have registered successfully! Welcome aboard.")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {"form": form})


def history(request):
    if request.user.is_authenticated:
        code = Code.objects.filter(user_id=request.user.id)
        return render(request, 'history.html', {"code":code})
    else:
        messages.success(request, "You Must Be Logged In To View This Page!")
        return redirect('home')


def delete_history(request, History_id):
    history = Code.objects.get(pk=History_id)
    history.delete()
    messages.success(request, "Deleted successfully..")
    return redirect('history')
