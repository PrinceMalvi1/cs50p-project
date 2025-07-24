from project import add_expense, get_summary

def test_add_expense():
    expenses = []
    add_expense(expenses, 25.0, "Food", "2025-07-20")
    assert expenses == [{"amount": 25.0, "category": "Food", "date": "2025-07-20"}]

def test_get_summary_single():
    expenses = [
        {"amount": 10.0, "category": "Transport", "date": "2025-07-20"},
        {"amount": 20.0, "category": "Transport", "date": "2025-07-21"},
    ]
    result = get_summary(expenses)
    assert result == {"Transport": 30.0}