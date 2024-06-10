import time
# this function MUST return a response, as it will be passed back to the server
# the response will be jsonified before being sent back (this isn't handled by this function)
def handle_challenge(payload_in_bytes):    
    ## example timeout to process
    time.sleep(2)
    ## Example response
    response = {"message": "Challenge handled (contains example timeout for 2 seconds)"}
    return response