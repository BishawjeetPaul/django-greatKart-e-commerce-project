from django.shortcuts import render, redirect
from . models import Category



# this fucntion work is show all the categories.
def view_category(request):
    categories = Category.objects.all()
    return render(request, 'category/category-panel.html', {'categories': categories})


# this function work is add the category.
def add_category(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')
        category_image = request.FILES.get('category_image')

        category_model = Category(category_name=category_name, description=description, category_image=category_image)
        category_model.save()
    
        # messages.success(request, "Add category successfully.")
        return redirect('view-category')
    # else:
    #     messages.error(request, "Fail to add category.")
    #     return redirect('admin-panel-add-category')
    params = {'categories': categories}
    return render(request, 'category/add-category.html', params)


# this function work is edit particular category.
def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'category': category,
        'id': category_id
    }

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category_name = request.POST.get('category_name')
        description = request.POST.get('description')
        category_image = request.FILES.get('category_image')

        category = Category.objects.get(id=category_id)
        category.category_name = category_name
        category.description = description
        category.category_image = category_image
        category.save()
        return redirect('view-category')
    return render(request, 'category/edit-category.html',context)


# this function work is delete particular category.
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('view-category')
