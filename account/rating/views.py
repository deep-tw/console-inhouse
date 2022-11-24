from django.shortcuts import render,HttpResponseRedirect,redirect
from account.models import Rating , User

# def index(request):
#         ratings=Rating.objects.all()
#         breakpoint()
#         return render(request,'rating/retrieve_rating.html',{'dev_rating':ratings})  

def add_rating(request):
        role= str(request.user.role)
        rating_count=Rating.objects.filter(developer_name=request.user).count()
        print(rating_count)
        if rating_count >0:
                message="already rating provided you please update rating"
                return render(request,'rating/add_rating.html',locals())
        else:
                if request.method == 'POST':  
                        developer_rating=request.POST['developer_rating']
                        developer_name=request.user
                        created_by=request.user.username
                        updated_by=request.user.username
                        user_data =Rating.objects.create(developer_rating=developer_rating,developer_name=developer_name,
                                                        created_by=created_by,updated_by=updated_by)
                        user_data.save()
                        return redirect('developerdashboard')
                return render(request,'rating/add_rating.html',locals())

def retrieve_rating(request):
        ratings=Rating.objects.all()
        return render(request,'rating/retrieve_rating.html',{'dev_rating':ratings})   

def update_rating(request,id,userid):
        print("ratingid :",id ,'usrid :',userid)
        alldev=User.objects.filter(role=3)
        dev=None
        for d in alldev:
                dev=User.objects.get(id=userid)
        

        if request.method=="POST":
                developer_rating=request.POST['developer_rating']
                developer_name=dev
                created_by=request.user
                updated_by=request.user
                obj=Rating.objects.get(id=id)
                obj.developer_rating=developer_rating
                obj.developer_name=developer_name
                created_by=created_by
                updated_by=updated_by
                obj.save()
                return redirect('managerdashboard')
        ratings=Rating.objects.get(id=id)
        return render(request,'rating/update_rating.html',{'dev_rating':ratings})
                          

def delete_rating(request,id):
    ratings=Rating.objects.get(id=id)
    ratings.delete()
    return HttpResponseRedirect('/dashboard/retrieve_rating/')
