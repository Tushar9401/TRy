import frappe 

@frappe.whitelist()
def get_book_details():
    return frappe.db.sql(f"""SELECT name1,author FROM tabBook;""",as_dict=True)