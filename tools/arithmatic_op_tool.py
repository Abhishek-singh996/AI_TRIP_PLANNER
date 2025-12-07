import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

@tool
def multiply(a, b) -> float:
    """
    Multiply two numbers safely.
    """
    try:
        a = float(a)
        b = float(b)
        return a * b
    except Exception as e:
        raise ValueError(f"Invalid inputs for multiply: a={a}, b={b}, error={e}")


@tool
def add(a, b) -> float:
    """
    Add two numbers safely.
    """
    try:
        return float(a) + float(b)
    except Exception as e:
        raise ValueError(f"Invalid inputs for add: a={a}, b={b}, error={e}")

@tool
def currency_converter(from_curr: str, to_curr: str, value) -> float:
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_curr, to_curr)
    rate = float(response['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return float(value) * rate
