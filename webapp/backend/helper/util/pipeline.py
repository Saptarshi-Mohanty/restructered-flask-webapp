from helper.connector.connection import stat

def get_all():
    r = stat.find()
    return r

def get_first_name(name):
    r = stat.find({"FirstName": name})
    return r

def sort_name_all():
    name_pipeline = [{"$sort": {"FirstName": 1}}]
    r = stat.aggregate(name_pipeline)
    return r

def sort_rating_all():
    rating_pipeline = [{"$sort": {"Current Employee Rating": -1}}]
    r = stat.aggregate(rating_pipeline)
    return r

def sort_name(name):
    name_pipeline = [{"$match": {"FirstName": name}}, {"$sort": {"LastName": 1}}]
    r = stat.aggregate(name_pipeline)
    return r

def sort_rating(name):
    rating_pipeline = [{"$match": {"FirstName": name}}, {"$sort": {"Current Employee Rating": -1}}]
    r = stat.aggregate(rating_pipeline)
    return r

def insert_user(fname, lname, email, password, empid, title):
    stat.insert_one({"FirstName": fname, "LastName": lname, "Title": title, "ADEmail": email, "EmpID": empid, "password": password})

def check_user(email):
    check_pipeline = [{"$match": {"ADEmail": email}}]
    r = stat.aggregate(check_pipeline)
    return r