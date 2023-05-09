from django.shortcuts import render

from products.models import number,prod,nomob,noacc,noall,acc,all,mobile

# Create your views here.
def add(request):
    if request.method == 'POST':
        img = request.POST.get('img')
        title = request.POST.get('title')
        disc = request.POST.get('disc')
        price = request.POST.get('price')
        cat =request.POST.get('cat')
        if cat=='0':
            x = number.objects.get(id=1) 
            x.no = x.no + 1 # 4
            x.save()
            prod.objects.create(img=img,title=title,disc=disc,price=price)
        if cat =='1':
            mob = nomob.objects.get(id=1)
            mob.no = mob.no + 1
            mob.save()
            mobile.objects.create(img=img,title=title,disc=disc,price=price)
        if cat =='2':
            acc1 = noacc.objects.get(id=1)
            acc1.no = acc1.no + 1
            acc1.save()
            acc.objects.create(img=img,title=title,disc=disc,price=price)
            
        noall1 =  noall.objects.get(id=1)
        noall1.no = noall1.no + 1
        noall1.save()
        all.objects.create(img=img,title=title,disc=disc,price=price)     
    return render(request, 'add.html', {})

def shop(request): 
    nu = number.objects.get(id=1).no 
    img = [ prod.objects.get(id=i).img for i in range(1,nu + 1)]
    title = [prod.objects.get(id=i).title for i in range(1,nu + 1)]
    disc = [prod.objects.get(id=i).disc for i in range(1,nu + 1)]
    price = [prod.objects.get(id=i).price for i in range(1,nu + 1)]
    kol = zip(img,title,disc,price)
    con = {
        'products':kol
    }
    return render(request,'template.html', con)
    
def mobile1(request):
    nomob1 = nomob.objects.get(id=1).no
    img1 = [mobile.objects.get(id=i).img for i in range(1,nomob1) ]
    title1 = [mobile.objects.get(id=i).title for i  in range(1,nomob1) ]
    disc1 = [mobile.objects.get(id=i).disc for i in range(1,nomob1)]
    price1 = [ mobile.objects.get(id=i).price for i in range(1,nomob1) ]
    kol = zip(img1,title1,disc1,price1)
    con = {'products':kol}
    return render(request,'mobile.html',con)

def access(request):
    noacc1 = noacc.objects.get(id=1).no
    img2 =[ acc.objects.get(id=i).img for i in range(1,noacc1+1) ]
    title2 =[acc.objects.get(id=i).title for i in range(1,noacc1+1)]
    disc2 =[acc.objects.get(id=i).disc for i in range(1,noacc1+1)]
    price2 =[acc.objects.get(id=i).price for i in range(1,noacc1+1)]
    kol = zip(img2,title2,disc2,price2)
    con = {'products':kol}
    return render(request,'acc.html', con)
    
def allf(request):
    noall1 = noall.objects.get(id=1).no
    img3 = [all.objects.get(id=i).img for i in range(1,noall1+1)]
    title3 = [all.objects.get(id=i).title for i in range(1,noall1+1)]
    disc3 = [all.objects.get(id=i).disc for i in range (1,noall1+1)]
    price3 = [all.objects.get(id=i).price for i in range(1,noall1+1)]
    kol= zip(img3,title3,disc3,price3)
    con ={'products':kol}
    return render(request, 'allshop.html', con)
    
def main(request):
    return render(request,'index.html', {})
