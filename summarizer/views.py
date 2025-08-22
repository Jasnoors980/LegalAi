from django.shortcuts import render
from .forms import DocumentForm
from .utils.get_text import get_text
from .utils.summarize import load_summarizer, summarize_text
from .utils.translator import load_translator, translate_text
import tempfile
import os
from .utils.extract_citations import extract_legal_citations
from mainApp.models import Document

# Load once at the top of your views.py
summarizer, summarizer_tokenizer = load_summarizer()

def index(request):
    summary = None
    translated = None
    citations = None

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['document']
            lang = form.cleaned_data['language']

            ext = os.path.splitext(file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                for chunk in file.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name

            try:
                text = get_text(tmp_path)
                summary = summarize_text(summarizer, summarizer_tokenizer, text)  # ✅ pass tokenizer here
                citations = extract_legal_citations(text)

                if lang:
                    translator_fn = load_translator(lang)
                    translated = translate_text(translator_fn, summary)

                if request.user.is_authenticated:
                    Document.objects.create(
                        user=request.user,
                        file=file,
                        extracted_text=text,
                    )

            except Exception as e:
                summary = f"Error: {str(e)}"

        return render(request, 'index.html', {
            'form': form,
            'summary': summary,
            'translated': translated,
            'citations': citations,
        })

    else:
        form = DocumentForm()

    return render(request, 'index.html', {
        'form': form,
        'summary': summary,
        'translated': translated,
        'citations': citations,
    })
