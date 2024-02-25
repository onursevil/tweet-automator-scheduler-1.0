import tweepy
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest

def post_tweet(request):
    if request.method == 'GET':
        # Display the page with a simple input form for the tweet
        return render(request, "app/home.html")

    if request.method == 'POST':
        tweet_content = request.POST.get('tweet', '')

        if not tweet_content:
            # Return an error response if the tweet content is empty
            return JsonResponse({"error": "Tweet content cannot be empty"}, status=400)
        
        # Initialize Tweepy client
        client = tweepy.Client(
            consumer_key='...',
            consumer_secret='...',
            access_token='...',
            access_token_secret='...'
        )

        try:
            # Post tweet
            response = client.create_tweet(text=tweet_content)
            return JsonResponse({"success": "Tweet posted successfully", "tweet_id": response.data["id"]})
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=400)

def home(request):
    # You can implement your home view here
    return render(request, "app/home.html")
