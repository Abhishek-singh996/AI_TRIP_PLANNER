class Calculator:
    @staticmethod
    def multiply(a, b) -> float:
        """
        Multiply two numbers safely. Handles string, int, and float inputs.

        Args:
            a: The first number (can be int, float, or string).
            b: The second number (can be int, float, or string).

        Returns:
            float: The product of a and b.
        """
        try:
            a = float(a)
            b = float(b)
            return a * b
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid inputs for multiply: a={a}, b={b}, error={e}")
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """
        Calculate sum of the given list of numbers

        Args:
            x (list): List of floating numbers

        Returns:
            float: The sum of numbers in the list x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Calculate daily budget

        Args:
            total (float): Total cost.
            days (int): Total number of days

        Returns:
            float: Expense for a single day
        """
        return total / days if days > 0 else 0
    
    