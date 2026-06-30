# order.py - מחלקת הזמנה
from builtins import list, ValueError, Exception, range
from datetime import datetime
from menu_item import MenuItem
from order_item import OrderItem


class Order:
    """
    הזמנה שלמה של שולחן.
    
    שדות מחלקה:
        _order_counter (int): מונה הזמנות - עולה ב-1 בכל יצירה (פרטי)
        DEFAULT_TIP_PERCENT (float): אחוז טיפ ברירת מחדל (10.0)
    
    שדות מופע:
        _order_id (int): מזהה ייחודי (נקבע אוטומטית מהמונה)
        _table (Table): אובייקט השולחן
        _items (list): רשימת OrderItem
        _created_at (datetime): זמן פתיחת ההזמנה
        _is_closed (bool): האם ההזמנה נסגרה
    """
    
    _order_counter: int = 0
    DEFAULT_TIP_PERCENT: float = 10.0
    
    def __init__(self, table: Table):

        """
        אתחול הזמנה.
        
        דרישות:
        - להעלות את _order_counter ב-1
        - לשמור את הערך החדש של המונה ב-_order_id
        - לשמור את table ב-_table
        - לאתחל _items לרשימה ריקה
        - לשמור את הזמן הנוכחי ב-_created_at (datetime.now())
        - לאתחל _is_closed ל-False
        
        Args:
            table: אובייקט השולחן
        """
        Order._order_counter += 1
        self._order_id = Order._order_counter
        self._is_closed = False
        self._created_at = datetime.now()
        self._items = []
        self._table = table

    
    # --- Properties ---
    
    @property
    def order_id(self) -> int:
        """מחזיר את מזהה ההזמנה"""
        return self._order_id
    
    @property
    def table(self) -> Table:
        """מחזיר את אובייקט השולחן"""
        return self._table
    
    @property
    def items(self) -> list:
        """
        מחזיר עותק של רשימת הפריטים.
        
        דרישות:
        - להחזיר עותק (copy) ולא את הרשימה עצמה
        """
        return self._items.copy()
    
    @property
    def is_closed(self) -> bool:
        """מחזיר האם ההזמנה נסגרה"""
        return self._is_closed
    
    @property
    def created_at(self) -> datetime:
        """מחזיר את זמן יצירת ההזמנה"""
        return self._created_at
    
    # --- Methods ---
    
    def add_item(self, menu_item: MenuItem, quantity: int = 1, notes: str = "") -> OrderItem:
        if self.is_closed:
            raise Exception("Cannot add items to closed order")
        for i in range(len(self._items)):
            if menu_item.name == self._items[i].menu_item.name and menu_item._description == self._items[
                i].menu_item._description:
                self._items[i].quantity += quantity

                return self._items[i]

        self._items.append(OrderItem(menu_item, quantity, notes))
        return self._items[-1]




        """
        הוספת פריט להזמנה.
        
        דרישות:
        - אם ההזמנה סגורה, להעלות Exception עם הודעה "Cannot add items to closed order"
        - לבדוק אם הפריט כבר קיים (לפי שם ואותן הערות)
          - אם כן: להוסיף לכמות הקיימת
          - אם לא: ליצור OrderItem חדש ולהוסיף לרשימה
        - להחזיר את ה-OrderItem
        
        Args:
            menu_item: הפריט מהתפריט
            quantity: כמות
            notes: הערות
            
        Returns:
            ה-OrderItem שנוסף/עודכן
        """



    
    def remove_item(self, menu_item: MenuItem) -> bool:
        """
        הסרת פריט מההזמנה.
        
        דרישות:
        - אם ההזמנה סגורה, להעלות Exception עם הודעה "Cannot remove items from closed order"
        - לחפש פריט עם אותו menu_item ולהסיר אותו
        
        Returns:
            True אם נמצא והוסר, False אחרת
            """

        if self.is_closed:
            raise Exception("Cannot add items to closed order")

        for i in range(len(self._items)):
            if menu_item == self._items[i].menu_item:
                self._items.pop(i)
                return True
            return False


    def get_subtotal(self) -> float:
        """
        מחזיר סכום ביניים (לפני טיפ).
        
        Returns:
            סכום כל ה-subtotal של הפריטים

        """
        subtotal = 0.0
        for item in self._items:
            subtotal += item.subtotal
        return subtotal

    def get_total(self, tip_percent: float = None) -> float:
        """
        מחזיר סכום כולל עם טיפ.
        
        דרישות:
        - אם tip_percent הוא None, להשתמש ב-DEFAULT_TIP_PERCENT
        - לחשב: subtotal + (subtotal × tip_percent / 100)
        
        Args:
            tip_percent: אחוז טיפ (ברירת מחדל: None)
            
        Returns:
            סכום כולל טיפ
        """
        if tip_percent is None:
            tip_percent = Order.DEFAULT_TIP_PERCENT
        return  self.get_subtotal() + (self.get_subtotal() / 100) *  tip_percent

    
    def get_bill(self, tip_percent: float = None) -> str:
        """
        מחזיר חשבון מפורט כמחרוזת.
        
        דרישות:
        - כותרת עם מספר הזמנה ושולחן
        - רשימת כל הפריטים
        - סכום ביניים (Subtotal)
        - טיפ (Tip) - סכום ואחוז
        - סכום סופי (Total)
        
        הפורמט:
        ========================================
        Bill - Order #X
        Table: Y
        Time: HH:MM:SS
        ========================================
        (items list)
        ----------------------------------------
        Subtotal: $XX.XX
        Tip (X%): $XX.XX
        ========================================
        Total: $XX.XX
        ========================================
        
        Returns:
            חשבון מפורמט
        """
        sub_total = self.get_subtotal()
        tip_percent = self.get_total() - self.get_subtotal()
        tip = sub_total / tip_percent
        time = self._created_at
        list_items = self._items
        num = Order._order_counter
        table = self.table
        return ("=" * 30,
            f"bill - order {num}"
                f"table: {table}"
                f"time:{time}"
                "=" * 30,
                f"{list_items}"
                "-"* 30,
                f"subtotal: {sub_total}"
                f"tip {tip} :{tip_percent}"
                "=" * 30,
                f"totsl: {tip_percent + sub_total}"
                "=" * 30)

    
    def close(self):
        """
        סגירת ההזמנה.
        
        דרישות:
        - לסמן את ההזמנה כסגורה
        - לשחרר את השולחן (לקרוא ל-free)
        """
        self._is_closed = True
        self.table.free()
    
    # --- Class Methods ---
    
    @classmethod
    def get_total_orders(cls) -> int:
        """מחזיר כמה הזמנות נוצרו בסה"כ"""
        return Order._order_counter
    
    # --- Magic Methods ---
    
    def __len__(self) -> int:
        """מחזיר כמות פריטים בהזמנה"""
        return len(self._items)
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Order #X (Table Y) - Z items - Open/Closed"

        """
        coo = "CLOSED"
        if self.is_closed == True:
            coo = "OPEN"
        return f"order {self._order_counter} table{self.table} - {self.__len__()} items - {coo} "
