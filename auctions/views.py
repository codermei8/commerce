from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing

def listing(request, id):
    listing = Listing.objects.get(pk=id)
    inWatchlist = request.user in listing.watchlist.all()
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "inWatchlist": inWatchlist
    })

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(isActive = True),
        "categories": Category.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        imageURL = request.POST["image_url"]
        category = request.POST["category"]
        currentUser = request.user
        categoryData = Category.objects.get(categoryName = category)
        listing = Listing(
            title = title, 
            description = description,
            price = price,
            imageURL = imageURL,
            category = categoryData,
            owner = currentUser
        )
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html", {
            "categories": Category.objects.all()
        })

def filter(request):
    if request.method == "POST": 
        category = request.POST["category"]
        categoryType = Category.objects.get(categoryName = category)
        listings = Listing.objects.filter(category = categoryType)
        return render(request, "auctions/filter.html", {
            "listings": listings,
            "category": categoryType
        })

def addWatchlist(request, id):
    listing = Listing.objects.get(pk=id)
    curUser = request.user
    listing.watchlist.add(curUser)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def removeWatchlist(request, id):
    listing = Listing.objects.get(pk=id)
    curUser = request.user
    listing.watchlist.remove(curUser)
    return HttpResponseRedirect(reverse("listing",args=(id, )))

def displayWatchlist(request): 
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html")

def addComment(request):
    currentUser = request.user
    listing = Listing.objects.get(pk=id)
    message = request.POST["newComment"]

    newComment = Comment(
        author = currentUser,
        listing = listing,
        message = message
    )