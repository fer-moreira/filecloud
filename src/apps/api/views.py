from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.conf import settings

def proto_uploader (request):
    if request.method.upper() == "POST":

        file = request.FILES['file'] if 'file' in request.FILES else None
        file_content = ContentFile(file.read())

        fout_path = settings.FILE_SYSTEM_DIR + "/%s" %file.name
        
        fout = open(fout_path, "wb+")
        
        try:
            for chunk in file_content.chunks(): fout.write(chunk)
            fout.close()
        except Exception as r:
            fout.close()
            raise
        

        print("File storage sucessfuly, path: %s" %fout_path)

        return HttpResponse("<p>OK!</p>", status=200)
    else:
        return HttpResponse("<p>NO!</p>", status=403)
