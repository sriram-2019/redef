from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def qr_redirect(request):
    """Redirects to link2 if accessed from a Kivy app, otherwise to link1. Stores in session properly."""

    # Update session only if new values are provided
    if "link1" in request.GET:
        request.session["link1"] = request.GET["link1"]
    if "link2" in request.GET:
        request.session["link2"] = request.GET["link2"]

    # Save session explicitly
    request.session.modified = True  

    # Debugging: Print stored session data
    print("Updated Session Data:", request.session.items())

    # Ensure values exist in session before redirecting
    link1 = request.session.get("link1")
    link2 = request.session.get("link2")

    # If no valid links exist, return an error or a default fallback page
    if not link1 or not link2:
        return HttpResponseRedirect("https://yourdomain.com/error-page")  # Replace with an appropriate error page

    # Detect Kivy app from User-Agent
    user_agent = request.headers.get("User-Agent", "").lower()
    if "kivyapp" in user_agent or "android" in user_agent:
        return HttpResponseRedirect(link2)  # Redirect to link2 for Kivy users
    return HttpResponseRedirect(link1)  # Redirect to link1 for others
