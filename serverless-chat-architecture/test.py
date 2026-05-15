try:
    import langchain
    print(f"LangChain is successfully installed. Version: {langchain.__version__}")
except ImportError:
    print("Error: LangChain is not installed in the current Python environment.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")