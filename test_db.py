import db_helper

print("▶️ Starting DB test")
result = db_helper.get_order_status(40)
print("✅ Final result:", result)
