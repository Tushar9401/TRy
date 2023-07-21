import frappe 

@frappe.whitelist()
def get_book_details():
    return frappe.db.sql(f"""SELECT * FROM tabAuthor;""",as_dict=True)