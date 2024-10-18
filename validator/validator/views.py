schema = {
'exactFields': True,
'fields': [
    {
        'name': 'Columna 1',
        'type': 'number',
        'minimum': 100,
        'maximum': 999999999 
        },
    {
        'name': 'Columna 2',
        'type': 'string',
        'format' : 'email'
        },
    {
        'name': 'Columna 3',
        'type': 'string',
        'enum' : ['CC', 'TI']
        },
    {
        'name': 'Columna 4',
        'type': 'number',
        'minimum': 500000,
        'maximum': 1500000
        },
    {
        'name': 'Columna 5',
        'type': 'string'
        }
    ]
}

from pycsvschema.checker import Validator
from django.core.files.temp import NamedTemporaryFile
from django.core import files
from .forms import UploadFileForm
from django.shortcuts import render

def handle_uploaded_file(f):
    with NamedTemporaryFile(delete=True) as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.seek(0)
        with NamedTemporaryFile(delete=True) as output:
            v = Validator(csvfile=destination.name, schema=schema, errors='coerce',output=output.name)
            try: 
                v.validate()
            except IndexError:
                errors = "Tienes mas columnas de las esperadas (esperadas: 5)"
            output.seek(0)
            errors = output.read()
            return {'errors': errors}
    

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return render(request, "index.html", handle_uploaded_file(request.FILES["file"]));
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})
