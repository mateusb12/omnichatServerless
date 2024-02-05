from utils.corsBlocker import createResponseWithAntiCorsHeaders


def lambda_handler(event, context):
    print("Hello, World!")
    return createResponseWithAntiCorsHeaders("Hello from Python!", 200)