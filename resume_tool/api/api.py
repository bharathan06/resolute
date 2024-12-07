from ninja import NinjaAPI

# Create an instance of NinjaAPI
api = NinjaAPI()

# Example endpoint
@api.get("/hello")
def hello_world(request):
    return {"message": "Hello, world!"}
