import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import openai
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain

# Step 1: Load Environment Variables
load_dotenv(dotenv_path=".env")  

# Step 2: Pinecone Setup
def initialize_pinecone():
    api_key = os.getenv("PINECONE_API_KEY")
    environment = "us-east-1"  #us-east-1
    if not api_key:
        raise ValueError("PINECONE_API_KEY not found in .env file.")

    # pinecone.init(api_key=api_key, environment=environment)
    # index_name = "my-vector-index"

    # # Check if the index exists, create it if not
    # if index_name not in pinecone.list_indexes():
    #     pinecone.create_index(index_name, dimension=512)  
    #     print(f"Created Pinecone index: {index_name}")
    # else:
    #     print(f"Pinecone index '{index_name}' already exists.")
    # return index_name
    pc= Pinecone(
        api_key=api_key
    )
    index_name = "my-vector-index"
    dimension = 512  # Specify your vector dimension here
    metric = "cosine"  # or 'euclidean', based on your use case
    region = "us-west-1"

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
        print(f"Created Pinecone index: {index_name}")
    else:
        print(f"Pinecone index '{index_name}' already exists.")
    return index_name


# Step 3: LangChain Setup
def initialize_langchain():
    openai_api_key = os.getenv("GOOGLE_API_KEY")
    if not openai_api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file.")
    openai.api_key = openai_api_key

    # Initialize LangChain with OpenAI model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # Replace with the model you prefer
    conversation = ConversationChain(llm=llm)
    return conversation

# Step 4: Main Functionality
if __name__ == "__main__":
    # Initialize Pinecone
    print("Initializing Pinecone...")
    pinecone_index_name = initialize_pinecone()

    # Initialize LangChain
    print("Initializing LangChain...")
    conversation_chain = initialize_langchain()

    # Test LangChain with a sample query
    print("Testing LangChain...")
    user_input = "Hello, how can I use LangChain with Pinecone?"
    response = conversation_chain.predict(input=user_input)
    print(f"LangChain Response: {response}")

    # Your application logic here (e.g., querying Pinecone, extending features)
