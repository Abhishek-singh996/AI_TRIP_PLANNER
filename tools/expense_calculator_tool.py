from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night: str, total_days: float) -> float:
            """Calculate total hotel cost"""
            try:
                # Convert price_per_night to float if it's a string
                price = float(price_per_night) if isinstance(price_per_night, str) else price_per_night
                return self.calculator.multiply(price, total_days)
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid inputs for estimate_total_hotel_cost: price_per_night={price_per_night}, total_days={total_days}, error={e}")
        
        @tool
        def calculate_total_expense(*costs: float) -> float:
            """Calculate total expense of the trip"""
            return self.calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]