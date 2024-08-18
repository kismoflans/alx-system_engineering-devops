#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests

def number_of_subscribers(subreddit):
    """
    Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if the subreddit is invalid or an error occurs
    """
    # Set the custom User-Agent header
    headers = {'User-Agent': 'xica369'}
    # Construct the URL for the Reddit API request
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        # Make the GET request to the Reddit API with no redirects allowed
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response and get the number of subscribers
            return response.json().get("data", {}).get("subscribers", 0)
    except Exception as e:
        pass  # Catch all exceptions and simply return 0
    
    # If the status code is not 200 or an error occurs, return 0
    return 0
