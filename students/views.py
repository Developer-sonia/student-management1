from django.shortcuts import render, get_object_or_404, redirect  # Import necessary functions
from django.contrib import messages  # Import Django's messages framework
from .models import Student  # Import the Student model
from .forms import StudentForm  # Import the Student form

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student added successfully!")  # Success message
            return redirect('student_list')
        else:
            messages.error(request, "❌ Failed to add student. Please check the form.")  # Error message
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student updated successfully!")  # Success message
            return redirect('student_list')
        else:
            messages.error(request, "❌ Failed to update student. Please check the form.")  # Error message
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "❌ Record deleted!")  # Success message
    return redirect('student_list')

