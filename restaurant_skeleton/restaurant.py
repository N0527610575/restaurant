# restaurant.py - מחלקת המסעדה הראשית

from menu import Menu
from table import Table
from order import Order
from menu_item import MenuItem


class Restaurant:
    """
    המחלקה הראשית - מנהלת את כל המסעדה.
    
    שדות מופע:
        _name (str): שם המסעדה
        _menu (Menu): אובייקט התפריט
        _tables (list): רשימת השולחנות
        _active_orders (list): רשימת הזמנות פעילות
        _closed_orders (list): רשימת הזמנות שנסגרו
        _total_revenue (float): סה"כ הכנסות
    """
    
    def __init__(self, name: str):
        """
        אתחול מסעדה.
        
        דרישות:
        - לשמור את name ב-_name
        - ליצור Menu חדש ולשמור ב-_menu
        - לאתחל _tables, _active_orders, _closed_orders לרשימות ריקות
        - לאתחל _total_revenue ל-0.0
        
        Args:
            name: שם המסעדה
        """
        raise NotImplementedError("Implement this method")
    
    # --- Properties ---
    
    @property
    def name(self) -> str:
        """מחזיר את שם המסעדה"""
        raise NotImplementedError("Implement this method")
    
    @property
    def menu(self) -> Menu:
        """מחזיר את אובייקט התפריט"""
        raise NotImplementedError("Implement this method")
    
    # --- Table Management ---
    
    def add_table(self, table: Table):
        """הוספת שולחן למסעדה"""
        raise NotImplementedError("Implement this method")
    
    def get_table(self, number: int) -> Table:
        """
        שליפת שולחן לפי מספר.
        
        Returns:
            השולחן אם נמצא, None אחרת
        """
        raise NotImplementedError("Implement this method")
    
    def get_all_tables(self) -> list:
        """מחזיר עותק של רשימת כל השולחנות"""
        raise NotImplementedError("Implement this method")
    
    def get_free_tables(self) -> list:
        """מחזיר רשימת שולחנות פנויים"""
        raise NotImplementedError("Implement this method")
    
    def get_occupied_tables(self) -> list:
        """מחזיר רשימת שולחנות תפוסים"""
        raise NotImplementedError("Implement this method")
    
    # --- Order Management ---
    
    def open_order(self, table_number: int) -> Order:
        """
        פתיחת הזמנה חדשה לשולחן.
        
        דרישות:
        - לבדוק שהשולחן קיים (אם לא, ValueError עם "Table X does not exist")
        - לבדוק שהשולחן פנוי (אם תפוס, ValueError עם "Table X is already occupied")
        - לסמן את השולחן כתפוס
        - ליצור Order חדש ולהוסיף לרשימת ההזמנות הפעילות
        
        Args:
            table_number: מספר השולחן
            
        Returns:
            ההזמנה החדשה
            
        Raises:
            ValueError: אם השולחן לא קיים או תפוס
        """
        raise NotImplementedError("Implement this method")
    
    def get_active_orders(self) -> list:
        """מחזיר עותק של רשימת הזמנות פעילות"""
        raise NotImplementedError("Implement this method")
    
    def get_order_by_table(self, table_number: int) -> Order:
        """
        מחזיר הזמנה פעילה לפי מספר שולחן.
        
        Returns:
            ההזמנה אם נמצאה, None אחרת
        """
        raise NotImplementedError("Implement this method")
    
    def close_order(self, order: Order, tip_percent: float = None) -> float:
        """
        סגירת הזמנה וחישוב סכום לתשלום.
        
        דרישות:
        - לבדוק שההזמנה ברשימת ההזמנות הפעילות (אם לא, ValueError עם "Order not found in active orders")
        - לחשב את הסכום הסופי
        - לקרוא ל-close של ההזמנה
        - להעביר מרשימת הפעילות לסגורות
        - להוסיף את הסכום ל-_total_revenue
        
        Args:
            order: ההזמנה לסגירה
            tip_percent: אחוז טיפ (ברירת מחדל: None)
            
        Returns:
            הסכום הסופי לתשלום
        """
        raise NotImplementedError("Implement this method")
    
    # --- Statistics (Bonus) ---
    
    def get_total_revenue(self) -> float:
        """מחזיר סה"כ הכנסות"""
        raise NotImplementedError("Implement this method")
    
    def get_orders_count(self) -> int:
        """מחזיר כמות הזמנות שנסגרו"""
        raise NotImplementedError("Implement this method")
    
    def get_average_order_value(self) -> float:
        """
        מחזיר ממוצע סכום הזמנה.
        
        Returns:
            ממוצע, או 0.0 אם אין הזמנות
        """
        raise NotImplementedError("Implement this method")
    
    def get_most_popular_item(self) -> tuple:
        """
        מחזיר את הפריט שהוזמן הכי הרבה.
        
        דרישות:
        - לעבור על כל ההזמנות הסגורות
        - לספור כמה פעמים כל פריט הוזמן
        - להחזיר את הפריט עם הספירה הגבוהה ביותר
        
        Returns:
            (item_name, count) או (None, 0) אם אין נתונים
        """
        raise NotImplementedError("Implement this method")
    
    def get_revenue_by_category(self) -> dict:
        """
        מחזיר הכנסות מחולקות לפי קטגוריה.
        
        Returns:
            מילון {category: amount}
        """
        raise NotImplementedError("Implement this method")
    
    # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Restaurant 'name' - X tables, Y menu items"
        """
        raise NotImplementedError("Implement this method")
