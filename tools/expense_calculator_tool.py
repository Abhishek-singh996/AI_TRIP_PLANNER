from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool
import re

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()
    
    def _extract_number(self, value):
        """Extract numeric value from string, handling currency symbols, commas, spaces, etc."""
        if isinstance(value, (int, float)):
            return float(value)
        
        if isinstance(value, str):
            # Remove currency symbols, commas, spaces, and other non-numeric characters except decimal point and minus sign
            # Keep digits, decimal points, and minus signs
            cleaned = re.sub(r'[^\d.-]', '', value.strip())
            # Handle empty string
            if not cleaned:
                raise ValueError(f"Cannot extract number from: {value}")
            return float(cleaned)
        
        return float(value)

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night: str, total_days: float) -> float:
            """Calculate total hotel cost. price_per_night can be a number or string with currency symbols/formatting."""
            try:
                # Extract numeric value from price_per_night (handles strings with currency, commas, etc.)
                price = self._extract_number(price_per_night)
                # Ensure total_days is also a number
                days = self._extract_number(total_days)
                return self.calculator.multiply(price, days)
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid inputs for estimate_total_hotel_cost: price_per_night={price_per_night}, total_days={total_days}, error={e}")
        
        @tool
        def calculate_total_expense(costs: List[float]) -> float:
            """Calculate total expense of the trip. Pass costs as a list of numbers.
            
            Args:
                costs: A list of cost values (can be numbers or strings with formatting)
                
            Returns:
                float: The total sum of all costs
            """
            try:
                # Extract numeric values from list elements (handles strings with currency, commas, etc.)
                float_costs = [self._extract_number(cost) for cost in costs]
                return self.calculator.calculate_total(*float_costs)
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid inputs for calculate_total_expense: costs={costs}, error={e}")
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense. total_cost can be a number or string with currency symbols/formatting."""
            try:
                # Extract numeric values (handles strings with currency, commas, etc.)
                cost = self._extract_number(total_cost)
                days_count = int(self._extract_number(days))
                return self.calculator.calculate_daily_budget(cost, days_count)
            except (ValueError, TypeError) as e:
                raise ValueError(f"Invalid inputs for calculate_daily_expense_budget: total_cost={total_cost}, days={days}, error={e}")
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]