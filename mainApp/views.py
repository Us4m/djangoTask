from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


from django.db.models import Q

def student_list(request):
    search_term = request.GET.get('search_term')
    if search_term:
        students = Student.objects.filter(
            Q(name__icontains=search_term) | Q(roll_number__icontains=search_term)
        )
    else:
        students = Student.objects.all()

    context = {'students': students}
    return render(request, 'student_list.html', context)
