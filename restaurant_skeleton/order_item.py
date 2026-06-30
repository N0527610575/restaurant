# order_item.py - מחלקת פריט בהזמנה
from builtins import ValueError, isinstance

from menu_item import MenuItem , Appetizer , Beverage



class OrderItem:
    """
    פריט בודד בהזמנה - מכיל MenuItem + כמות + הערות.
    
    שדות מופע:
        _menu_item (MenuItem): הפריט מהתפריט (פרטי)
        _quantity (int): כמות (פרטי)
        _notes (str): הערות מיוחדות (פרטי)
    """
    
    def __init__(self, menu_item: MenuItem, quantity: int = 1, notes: str = ""):
        """
        אתחול פריט בהזמנה.
        
        דרישות:
        - לשמור את menu_item ב-_menu_item
        - להשתמש ב-setter של quantity (לולידציה)
        - לשמור את notes ב-_notes
        
        Args:
            menu_item: הפריט מהתפריט
            quantity: כמות (ברירת מחדל: 1)
            notes: הערות (ברירת מחדל: מחרוזת ריקה)
        """
        self._menu_item = menu_item
        self.quantity = quantity
        self.notes = notes


    
    # --- Properties ---
    
    @property
    def menu_item(self) -> MenuItem:
        """מחזיר את הפריט מהתפריט"""
        return self._menu_item
    
    @property
    def quantity(self) -> int:
        """מחזיר את הכמות"""
        return self._quantity
    
    @quantity.setter
    def quantity(self, value: int):
        """
        קובע את הכמות.
        
        דרישות:
        - אם הכמות קטנה מ-1, להעלות ValueError עם הודעה "Quantity must be at least 1"
        """
        if value < 1:
            raise ValueError("Quantity must be at least 1")
        self._quantity = value
    
    @property
    def notes(self) -> str:
        """מחזיר את ההערות"""
        return self._notes
    
    @notes.setter
    def notes(self, value: str):
        """קובע את ההערות"""
        self._notes = value
    
    @property
    def subtotal(self) -> float:
        """
        מחזיר סכום ביניים (מחיר × כמות).
        
        דרישות:
        - אם לפריט יש מתודת get_total_price (כמו Appetizer, Beverage), להשתמש בה
        - אחרת, להשתמש ב-price רגיל
        - להכפיל בכמות
        
        Returns:
            מחיר × כמות
        """
        if isinstance(self._menu_item,Appetizer):
             return self.menu_item.get_total_price(self._menu_item) * self._quantity
        if isinstance(self._menu_item,Beverage):
             return self.menu_item.get_total_price(self._menu_item) * self._quantity
        else:
            return self._menu_item._price * self._quantity


    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "quantity x name = $subtotal" או "quantity x name = $subtotal (notes)"
        """
        return f"{self._quantity} * {self._name} = {subtotal()}"
