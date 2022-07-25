from typing import Optional

def format_hello(source: Optional[str] = None) -> str:
    if source is None:
        source = __name__
    
    return f"Hello from {source}"

def say_hello():
    print(format_hello(__name__))
