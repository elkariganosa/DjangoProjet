from django.shortcuts import render, HttpResponseRedirect
from.forms import StudentRegistration
from.models import User

# Create your views here.
# cette fonctionn permet d'ajouter et afficher les informations d'un utilisateurs
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'etudiant/addandshow.html',{'from':fm,'stu':stud})

   #cette fonction permet de modifier  les informations
def update_data(request, id):
    if request.method =='POST':
        pi =User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valide():
            fm.save()
    else:
         pi= User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)

    return render(request, 'etudiant/updatestudent.html',{'form':fm})
    # Votre logique de mise à jour des données ici
    return HttpResponse("Mise à jour des données")
    return HttpResponse("Méthode non autorisée.")



  #cette fontion permet de supprimer les donnees
def delete_data(request,id):
    if request.method == 'POST':
       pi= User.objects.get(pk=id)
       pi.delete()
    return  HttpResponseRedirect('/')