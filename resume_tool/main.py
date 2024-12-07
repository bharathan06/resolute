import os
from dotenv import load_dotenv
import pinecone
import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

# Step 1: Load Environment Variables
load_dotenv(dotenv_path=".env")  

# Step 2: Pinecone Setup
def initialize_pinecone():
    api_key = os.getenv("PINECONE_API_KEY")
    environment = "us-west1-gcp"  #us-east-1
    if not api_key:
        raise ValueError("PINECONE_API_KEY not found in .env file.")

    pinecone.init(api_key=api_key, environment=environment)
    index_name = "my-vector-index"

    # Check if the index exists, create it if not
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=512)  
        print(f"Created Pinecone index: {index_name}")
    else:
        print(f"Pinecone index '{index_name}' already exists.")
    return index_name

# Step 3: LangChain Setup
def initialize_langchain():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")
    openai.api_key = openai_api_key

    # Initialize LangChain with OpenAI model
    llm = ChatOpenAI(model="gpt-3.5-turbo")  # Replace with the model you prefer
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
