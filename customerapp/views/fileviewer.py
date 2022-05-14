from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def fileupload(request):
    if request.method == 'POST' and request.FILES['uploadedfile']:
        getfile = request.FILES['uploadedfile']
        fss = FileSystemStorage()
        filename = fss.save(getfile.name, getfile)
        uploaded_file_url = fss.url(filename)
        return render(request, 'customerapp/fileviewer.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'customerapp/fileviewer.html')
